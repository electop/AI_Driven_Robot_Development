import cv2
 
num_down = 2       # number of downsampling steps
num_bilateral = 7  # number of bilateral filtering steps
 
img_rgb = cv2.imread("640px-Brad_Pitt_2012.jpg")

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
ret, mask = cv2.threshold(img_edge, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# convert back to color, bit-AND with color image
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
#img_cartoon = cv2.bitwise_and(img_color, img_edge)

img_cartoon_bg = cv2.bitwise_and(roi, roi, mask = mask)
img_cartoon_fg = cv2.bitwise_and(img_edge, img_edge, mask = mask_inv)
dst = cv2.add(img_cartoon_fg, img_cartoon_bg)
img_rgb[0:rows, 0:cols] = dst

# display
#cv2.imshow("original", img_rgb)
#cv2.imshow("edge", img_edge)
#cv2.imshow("mask_inv", mask_inv)
#cv2.imshow("color", img_color)
cv2.imshow("mask", mask)
cv2.imshow("cartoon", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
