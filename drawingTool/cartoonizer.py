import cv2
import datetime
import numpy as np

def cam():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("./images/screen_capture.jpg", frame)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def cartoonizer():
    num_down = 2       # number of downsampling steps
    num_bilateral = 7  # number of bilateral filtering steps
    
    img_rgb = cv2.imread("./images/screen_capture.jpg")
 
    # downsample image using Gaussian pyramid
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
    
    # repeatedly apply small bilateral filter instead of
    # applying one large filter
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9,
                                        sigmaColor=9,
                                        sigmaSpace=7)
    
    # upsample image to original size
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)

    # convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    rows, cols, channels = img_rgb.shape
    roi = img_color[0:rows, 0:cols]

    # detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY,
                                    blockSize=9,
                                    C=2)

    img_median = cv2.medianBlur(img_edge, 5)
    edge_compare = np.concatenate((img_edge, img_median), axis=1)
    cv2.imshow("edge_compare", edge_compare)
    ret, mask = cv2.threshold(img_median, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # convert back to color, bit-AND with color image
    img_edge = cv2.cvtColor(img_median, cv2.COLOR_GRAY2RGB)
    #img_cartoon = cv2.bitwise_and(img_color, img_edge)

    img_cartoon_bg = cv2.bitwise_and(roi, roi, mask = mask)
    img_cartoon_fg = cv2.bitwise_and(img_edge, img_edge, mask = mask_inv)
    dst = cv2.add(img_cartoon_fg, img_cartoon_bg)
    img_color[0:rows, 0:cols] = dst

    # display
    #cv2.imshow("original", img_rgb)
    #cv2.imshow("edge", img_edge)
    #cv2.imshow("mask_inv", mask_inv)
    #cv2.imshow("color", img_color)
    #cv2.imshow("mask", mask)
    #cv2.imshow("cartoon", img_rgb)
    result_compare = np.concatenate((img_rgb, img_color), axis=1)
    cv2.imshow("result_compare", result_compare)
    cv2.waitKey(0)
    now = datetime.datetime.now()
    cv2.imwrite("./images/screen_capture_cartoonized_mask_%s.jpg" % now, mask)
    cv2.imwrite("./images/screen_capture_cartoonized_%s.jpg" % now, img_rgb)
    cv2.destroyAllWindows()

cam()
cartoonizer()
