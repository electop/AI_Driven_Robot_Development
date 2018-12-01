https://www.printedsolid.com/blogs/news/installing-marlin-1-1-6-on-your-cr-10s-with-mesh-bed-leveling

<div class="ten columns alpha blog_content">
      <p><strong>Important note about customer support of CR-10S Marlin update blog posts<span>.  These posts were written by David Randolph as a free community contribution.  He's happy to have provided this contribution when Creality would not.  Unfortunately, we do not have unlimited time and cannot provide support if you have any issues with this process.  Please read the instructions carefully and consider your skill level.  If you run into any issues, we suggest posting comments on this blog post as many users </span><span>hang out regularly and will offer help.  Checking into the various Facebook CR-10 Communities is also an option.  </span></strong></p>
<p> </p>
<p> </p>
<p><strong>UPDATE! </strong>We have added notes for the new version of Marlin 1.1.7 as well as a new download of the source and hex files. Enjoy</p>
<p> </p>
<p>Before we start: This is for the <a href="https://printedsolid.com/products/cr10s">CR-10S</a> and not the CR-10. Don’t use this firmware or follow these instructions for the CR-10. It is a different board and uses different settings.The older CR-10 uses a MELZI board which has less memory so in order to get it to work you will have to remove a lot of options to get everything to fit.</p>
<p>The firmware for the CR-10S is based on Marlin <a href="http://marlinfw.org">http://marlinfw.org</a> which is an open source project and as such means you can modify the source code as you want. While this article will be long and involved, I will get right to the point and just give you the .hex file and you can go ahead and just install it and close out this page. This version has mesh bed leveling, baby stepping and EEPROM storage enabled.</p>
<p>Inside the zip is a file called instructions.pdf on how to flash your firmware.</p>
<p> <a href="https://cdn.shopify.com/s/files/1/0887/0138/files/CR-10S-Marlin_By_PrintedSolid.zip?18225442472906648344">CR-10S 1.1.6 Firmware Source Code and Hex Files</a></p>
<p><a href="https://cdn.shopify.com/s/files/1/0887/0138/files/CR-10S-Marlin_By_PrintedSolid_117.zip?18225442472906648344"> CR-10S 1.1.7 Firmware Source Code and Hex Files</a></p>
<p>However, if you’re still reading this then we will go ahead and get moving. Let’s install and configure the software and give you a quick lesson on what we will be doing.</p>
<ol>
<li>You will need to download and install the Arduino IDE. <a href="https://www.arduino.cc/en/Main/Software">https://www.arduino.cc/en/Main/Software</a>
</li>
<li>Next you will need to download and install the U8glib library. <a href="https://bintray.com/olikraus/u8glib/download_file?file_path=u8glib_arduino_v1.18.1.zip">https://bintray.com/olikraus/u8glib/download_file?file_path=u8glib_arduino_v1.18.1.zip</a> and then from inside Arduino go to <em>sketch&gt;include library&gt;add zip library </em>and select the zip file. This is a library used to run the LCD display.</li>
<li>A preference we should setup inside of Arduino is to show line numbers. This will help us guide our way through the code and I will be referring to line numbers and the variable names for version 1.1.6. If you are reading this and using a different firmware version then line numbers may have changed but most likely the variable names will be the same. Now in the Arduino software go to <em>File&gt;Preferences</em> and put a check mark in the box next to Display Line Number.</li>
<li>Finally you need to download the 1.1.6 firmware <a href="http://marlinfw.org/meta/download/">http://marlinfw.org/meta/download/</a> and unzip the folder. Don’t rename the folder or move the files around inside it. You can put it anywhere you like to work on it. Go into the folders till you find Marlin.ino and open that file from inside Arduino IDE. It will open the full project and put all the files into separate tabs along the top.</li>
</ol>
<p>Now we are ready to get to work modifying things. Most of the work we will be doing will be in <em>Configuration.h </em>but we will be touching a few other ones. I will call those out later on. In Arduino if a line is “commented” this means that the instructions on that line are ignored. Marlin is well written and most of what we be doing is uncommenting an option or changing a value of something. To uncomment a line you just remove the two forward slashes // at the beginning of the line. To comment out a line you will just and // at the start of the line.</p>
<h1>Configurations.h</h1>
<p>Line 114: <strong>#define BAUDRATE 115200 </strong></p>
<p><em>This is the speed that it communicates over USB. It could be one of the faster speeds but honestly this is enough.</em></p>
<p>Line 122: <strong>#define MOTHERBOARD BOARD_RAMPS_14_EFB</strong></p>
<p><em>There are many boards that support Marlin and this is one of them. It is based off the very popular board RAMPS.</em></p>
<p>Line 127: <strong>#define CUSTOM_MACHINE_NAME "CR-10S"</strong></p>
<p><em>When your machine starts up this is the name that is displayed in the bottom left of the screen. It can be anything you want between the quotes, even Printer McPrintface if you like.</em></p>
<p>Line 286: (Line 289 in Marlin 1.1.7) <strong>#define TEMP_SENSOR_0 1</strong></p>
<p><em>This sets the type of sensor used for measuring the hotend temperature. For the stock hotend you will use “1” and for an E3Dv6 hotend you will use “5”  </em></p>
<p>Line 291:  (Line 294 in Marlin 1.1.7) <strong>#define TEMP_SENSOR_BED 5</strong></p>
<p><em>This sets the bed sensor for the stock bed.</em></p>
<p>Line 325: (Line 328 in Marlin 1.1.7) <strong>#define HEATER_0_MAXTEMP 250</strong></p>
<p><em>This is the limit for how hot your hotend will go. For the stock hotend you should set it for 250 and for an E3Dv6 hotend you can set it to 300.</em></p>
<p>Line 330: (Line 333 in Marlin 1.1.7) <strong>#define BED_MAXTEMP 120</strong></p>
<p><em>This is the limit for how hot your bed will go. In this case we can set it to 120 but honestly you will be lucky to ever go above 80c.</em></p>
<p>Line 442: (Line 446 in Marlin 1.1.7) <strong>#define THERMAL_PROTECTION_HOTENDS</strong></p>
<p>Line 443: (Line 447 in Marlin 1.1.7)<strong> #define THERMAL_PROTECTION_BED<br></strong></p>
<p><em>These two lines are what protects your machine from thermal runaway. While they are already uncommented I wanted to still point them out so you know to pay attention to them.</em></p>
<p>Line 528: (Line 532 in Marlin 1.1.7) <strong>#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 400, 95 }</strong></p>
<p><em>This is the amount of steps your printer has to use to move a specific distance. Things like drivers, motors, gearing, screws can change these numbers but the ones above are good for a stock CR-10S. These can be tuned later from the control screen thanks to the EEPROM settings we will be enabling later.</em></p>
<p>Line 535: (Line 539 in Marlin 1.1.7) <strong>#define DEFAULT_MAX_FEEDRATE          { 2500, 2500, 100, 25 }</strong></p>
<p><em>This is the fastest the machine will move in all directions. </em></p>
<p>Line 553:  (Line 557 in Marlin 1.1.7) <strong>#define DEFAULT_ACCELERATION          575</strong></p>
<p><em></em>Acceleration is the rate of change of speed.  It is defined in mm/s^2.  Your printer slows down when changing direction and then speeds back up again in straight lines.  This line is the acceleration the printer will make during printing moves.  575 is fairly slow, but for a printer like the CR10S with a big moving bed, it will help prevent <a href="https://printedsolid.com/blogs/news/a-solid-foundation-for-high-quality-corners">ringing</a>.  </p>
<p>Line 554: (Line 558 in Marlin 1.1.7) <strong>#define DEFAULT_RETRACT_ACCELERATION  1000</strong></p>
<p><em>This is the acceleration applied to your extruder retraction.  You want this as high as it can go before the filament starts stripping out to help prevent strining.</em></p>
<p>Line 555: (Line 559 in Marlin 1.1.7) <strong>#define DEFAULT_TRAVEL_ACCELERATION   1000</strong></p>
<p><em>This is the acceleration of your printer when it is not printing.  Since it is not printing at the time, it can be a little higher since you won't be able to see the ringing.  If it is too high, you could see skipped steps and layer shifts.</em></p>
<p>Line 745: (Line 751 in Marlin 1.1.7) <strong>#define INVERT_X_DIR false</strong></p>
<p>Line 746: (Line 752 in Marlin 1.1.7) <strong>#define INVERT_Y_DIR false</strong></p>
<p>Line 747: (Line 753 in Marlin 1.1.7) <strong>#define INVERT_Z_DIR true</strong></p>
<p><em>These 3 line define the direction of each axis. If your machine moves in the opposite direction of what you expect then change it to true or false.</em></p>
<p>Line 777: (Line 783 in Marlin 1.1.7) <strong>#define X_BED_SIZE 300</strong></p>
<p>Line 778: (Line 784 in Marlin 1.1.7) <strong>#define Y_BED_SIZE 300</strong></p>
<p>Line 786: (Line 792 in Marlin 1.1.7) <strong> #define Z_MAX_POS 400</strong></p>
<p><em>This is where we set the actual bed size of your printer and the Z height.</em></p>
<p>Line 801: (Line 827 in Marlin 1.1.7) Uncomment <strong>#define FILAMENT_RUNOUT_SENSOR</strong></p>
<p><em>This will enable the filament sensor. </em></p>
<p>Line 803: (Line 829 in Marlin 1.1.7) <strong>#define FIL_RUNOUT_INVERTING true</strong></p>
<p><em>Here we are changing the way the switch on the filament sensor works.</em></p>
<p>Line 855: (Line 876 in Marlin 1.1.7) Uncomment<strong> #define MESH_BED_LEVELING</strong></p>
<p><em>This is the fun part. No probe, no hardware. This allows you to level the bed at multiple points manually and it will create a 3D mesh of the surface to allow you to print on an uneven bed.  It will use the manual bed leveling as defined <a href="http://marlinfw.org/docs/features/unified_bed_leveling.html">here</a>. </em></p>
<p>Line 874:  (Line 986 in Marlin 1.1.7) <strong>#define GRID_MAX_POINTS_X 3</strong></p>
<p><em>We are setting this to 3 which means it will have you level 3 times along the X axis and 3 times along the Y axis for a total of 9 points. If you set this to 5 then it would mean you have to adjust level 25 times on the bed. 3 is a really good number for this.</em></p>
<p>Line 956: (Line 997 in Marlin 1.1.7) Uncomment<strong> #define LCD_BED_LEVELING<br></strong></p>
<p><em>This adds the option to run mesh bed leveling to the LCD screen.</em></p>
<p>Line 964:  (Line 1005 in Marlin 1.1.7) Uncomment<strong> #define LEVEL_BED_CORNERS<br></strong></p>
<p><em>This adds the option to level the corners of your bed before running mesh leveling.</em></p>
<p>Line 1018: (Line 1116 in Marlin 1.1.7) <strong> </strong>Uncomment<strong> #define EEPROM_SETTINGS</strong></p>
<p><em>This allows you to adjust things like offsets and steps and store them.</em></p>
<p>Line 1019: (Line 1117 in Marlin 1.1.7)<strong> </strong>Uncomment<strong> #define DISABLE_M503</strong></p>
<p><em>This is a command that shows the settings as they were set in the firmware and not the ones you changed in the EEPROM. We are disabling this to save some memory.</em></p>
<p>Line 1050 (Line 1148 in Marlin 1.1.7):<strong> #define PREHEAT_1_TEMP_HOTEND 205</strong></p>
<p>Line 1051 (Line 1149 in Marlin 1.1.7):<strong> #define PREHEAT_1_TEMP_BED     60</strong></p>
<p>Line 1052 (Line 1150 in Marlin 1.1.7):<strong> #define PREHEAT_1_FAN_SPEED     0</strong></p>
<p>Line 1054 (Line 1152 in Marlin 1.1.7):<strong> #define PREHEAT_2_TEMP_HOTEND 250</strong></p>
<p>Line 1055 (Line 1153 in Marlin 1.1.7):<strong> #define PREHEAT_2_TEMP_BED     80</strong></p>
<p>Line 1056 (Line 1154 in Marlin 1.1.7):<strong> #define PREHEAT_2_FAN_SPEED     0</strong></p>
<p><em>The lines 1050-1056 set the temps and fan speeds for the menu items to preheat for PLA and ABS.</em></p>
<p>Line 1232: (Line 1330 in Marlin 1.1.7): Uncomment <strong>#define SDSUPPORT</strong></p>
<p><em>This enables the SD card slot so you can print from SD.</em></p>
<p>Line 1257: (Line 1355 in Marlin 1.1.7): Uncomment <strong>#define ENCODER_PULSES_PER_STEP 1</strong></p>
<p><em>Leave this at 1 for the CR-10S</em></p>
<p>Line 1263 (Line 1361 in Marlin 1.1.7): Uncomment <strong>#define ENCODER_STEPS_PER_MENU_ITEM 5</strong></p>
<p><em>This is how far the knob needs to turn to move between menu items. Make this number lower if it is too sensitive and higher if it is not.</em></p>
<p>Line 1303: (Line 1401 in Marlin 1.1.7): Uncomment <strong>#define SPEAKER</strong></p>
<p><em>This will let the machine beep and make sounds.</em></p>
<p>Line 1384 (Line 1482 in Marlin 1.1.7): Uncomment <strong>#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER</strong></p>
<p><em>This enables the LCD screen. When we first installed U8Glib library, it was for this option.</em></p>
<p>Line 1684 (Line 140 in Marlin 1.1.7): #define <strong>DEFAULT_NOMINAL_FILAMENT_DIA 1.75 </strong> </p>
<p><em>Here we set what size filament will be used in the machine.</em></p>
<p> </p>
<h1>Configuration_adv.h</h1>
<p>Line 602 (Line 658 in Marlin 1.1.7): Uncomment <strong>#define BABYSTEPPING</strong></p>
<p><em>Baby stepping allows you to adjust the Z axis while printing to help get the perfect 1<sup>st</sup> layer.</em></p>
<p>Line 606 (Line 662 in Marlin 1.1.7):  <strong>#define BABYSTEP_MULTIPLICATOR 5</strong></p>
<p><em>This is how much your Z axis will move per rotation on the knob. I find 5 is a good number but if you want finer control then lower this number. IF you want it to move more per click then increase this number.</em></p>
<p>Line 608 (Line 664 in Marlin 1.1.7): Uncomment <strong>#define DOUBLECLICK_FOR_Z_BABYSTEPPING</strong></p>
<p><em>This makes it so if you want to adjust baby stepping then you can press the control knob two times quickly and you will enter baby step mode.</em></p>
<p>Line 683 (Line 733 in Marlin 1.1.7): Comment out <strong>// #define ARC_SUPPORT</strong></p>
<p><em>Not really used since most slicers don’t do this function by default. If we disable it then we save even more memory.</em></p>
<p>Line 819 (Line 878 in Marlin 1.1.7): Uncomment <strong>#define ADVANCED_PAUSE_FEATURE</strong></p>
<p><em>This is for the filament runout sensor. It will home the hotend and unload the filament from the nozzle. Then once you load more filament it will wait till it’s extruding before beginning the print.</em></p>
<h1>Pins_RAMPS.h</h1>
<p>Line 206 (Line 255 in Marlin 1.1.7): <strong>#define FIL_RUNOUT_PIN      2</strong></p>
<p><em>We are changing this one value from 4 to 2 so we are using the right pin for the filament sensor.</em></p>
<p><em> </em></p>
<h2><strong>All done! Save your work.</strong></h2>
<p>Wow, you really have been sticking with me this whole time and you have modified everything and you are ready to build your firmware and install it. Kudos for sticking with me this whole time.</p>
<ol>
<li>
<em> </em>Select <em>Tools&gt;Board&gt;Arduino/Genuino Mega or Mega 2560</em> and then <em>Tools&gt;Processor&gt;ATMega2560 (Mega 2560) </em>and then select the COM port for your printer. Did I mention that you should have already plugged your printer into your computer?</li>
<li>
<em> </em>Now we want to verify and compile the code. You can do this by clicking on the checkmark icon in the tool bar or by going to <em>Sketch&gt;Verify/Compile </em>
</li>
<li>
<em> </em>If you got no errors then congratulations and now you are ready to upload the firmware. Go to Sketch&gt;Upload or click on the icon in the toolbar that is an arrow pointing to the right.</li>
<li>
<em> </em>Now you are all set and good to go, enjoy your new firmware. Let us know what you think and if you think we should do anything more.</li>
</ol>
