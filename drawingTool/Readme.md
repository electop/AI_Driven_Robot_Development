## DrawingTool
  ### History
    DrawigTool
    1. v0.001 : 2019-08-23 12:35 by Bongchae Kim
    2. v0.002 : 2019-08-25 11:45 by Bongchae Kim
    3. v0.003 : 2019-09-06 11:34 by Bongchae Kim
    4. v0.004 : 2019-09-09 19:09 by Bongchae Kim
    5. v0.005 : On going

  ### User scenarios
    1. User can import an image file. It's necessary to draw picture as a sketch.
    2. User can get G-codes with a sketch.
    3. User can define the thickness of the line. Of course, it will be also implemented to be able to draw with G-codes, considering the thickness.

  ### Figures
<img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/Screenshot%20from%202019-08-27%2003-17-05.png?raw=true"><br>

## Cartoonizer
  ### History
    1. v0.001 : 2019-08-23 08:31 by Ju-hwan Yoo
    2. v0.002 : On going

  ### User scenarios
    1. User can get cartoon image from web cam device.

  ### Figures
  #### e.g.1
  ##### ▶ Source
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/img_example.jpg"><br>
  ##### ▶ Edge mask
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/Screenshot%20from%202019-09-01%2009-03-38.png"><br>
  ##### ▶ Gaussian pyramid + Edge mask
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/Screenshot%20from%202019-09-01%2009-03-29.png"><br>
  #### e.g.2
  ##### ▶ Source
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/screen_capture.jpg"><br>
  ##### ▶ Edge mask
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/screen_capture_cartoonized_mask_2019-09-01%2010:24:24.272818.jpg"><br>
  ##### ▶ Gaussian pyramid + Edge mask
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/screen_capture_cartoonized_2019-09-01%2010:24:24.272818.jpg"><br>
  #### e.g.3
  ##### ▶ Edge mask (vs) Edge mask + Median blur
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/Screenshot%20from%202019-09-02%2008-02-05.png"><br>
  ##### ▶ Source (vs) Gaussian pyramid + Edge mask + Median blur
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/Screenshot%20from%202019-09-02%2008-01-49.png"><br>

## Drawing Bot Desk design
  ### History
    1. V.0.001 : 2019-09-12 I added laser cutting design for desk.
    
  ### Figures
  #### Design Images
  ##### ▶ Top
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/plate_top-20190911.png?raw=true"><br>
  ##### ▶ Back
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/plate_back-20190911.png?raw=true"><br>
  ##### ▶ Front
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/plate_front-20190911.png?raw=true"><br>
  ##### ▶ Right
  <img src="https://github.com/electop/AI_Driven_Robot_Development/blob/master/drawingTool/images/plate_right-20190911.png?raw=true"><br>

## SW Update Requirement
  ### History
    1. V.0.002 : 2019-10-05 List for requirements
  #### 수정 필요 리스트
    1. Drawing Bot Serial Port 찾아서 붙이는 기능 (현재는 하드 코딩 되어 있음)
    2. Gcode 파일 별도 생성 필요 프로그램 오픈하면서 gcode 파일을 생성하게 되어 있고 여기에 바로 작성
    3. 당장은 바꾸지 않아도 되나 곡선을 그리면 펜이 내려온 상태에서 얻어지는 점 숫자가 너무 많아짐
       이를 근사화해서 곡선으로 (현재는 점에서 점으로 직선 형태) 변화하는 방법이 필요 (CAD 기술인데 잘 안찾아짐)
    4. 사진 찍었을 때 그림으로 만드는 파라메터 최적화
    5. 잘못그린 것 되돌리는 기능 (이건 복잡한게 지금 gcode에 바로 작성하게 되어 있어 이것도 돌려야 함)
    6. 기본 배경 gcode 확보 (간단하면서도 미적 감각이 있는 배경... 샹제리제 거리 또는 메이커 페어 관련)
    7. 혹시 웹캠을 쓸 경우 여러개의 카메라에서 웹캠을 찾아 선택하는 기
   
  
