# AI Driven Robot Development
1. Drawing Robot - Arduino Uno + CNC Shield + GRBL (May 27, 2017)<br>
https://www.thingiverse.com/thing:2349232<br>
https://www.youtube.com/watch?time_continue=3&v=vTD7USqdXJI<br>
<img src="https://cdn.thingiverse.com/renders/0c/90/3f/fb/04/45ea13cb80020e78b923b75b8021c750_preview_featured.JPG" alt="Drawing Robot - Arduino Uno + CNC Shield + GRBL" height="302" width="403"><br>
2. EEZYxyDRAW (Aug 24, 2018)<br>
https://www.thingiverse.com/thing:2936872<br>
<img src="https://cdn.thingiverse.com/renders/2c/ef/19/21/3e/c7dce7de062a3b1610eeea9f624ee118_preview_featured.jpg" alt="EEZYxyDRAW" height="302" width="403"><br>
3. drawbot (Sep 12, 2018)<br>
https://www.thingiverse.com/thing:3096135<br>
<img src="https://cdn.thingiverse.com/renders/e9/1e/b3/35/48/c63a890f3c0ff4ee8993b40c5bfdacdf_preview_featured.jpg" alt="drawbot" height="302" width="403"><br>
4. Cosmos Drawbot 1.0 (May 12, 2019)<br>
https://www.thingiverse.com/thing:3624736<br>
<img src="https://cdn.thingiverse.com/renders/24/96/ef/3e/99/292e86631f99ae4fcbbee7533d82bcfc_preview_featured.jpg" alt="Cosmos Drawbot 1.0" height="302" width="403"><br>
5. midTbot (Oct 16, 2017)<br>
https://www.thingiverse.com/thing:2587684<br>
http://www.buildlog.net/blog/2017/10/the-midtbot-a-new-flavor-of-h-bot/<br>
<img src="https://cdn.thingiverse.com/renders/9f/e1/e8/41/3c/1ea54ba4b695a37cefbbd15caf575798_preview_featured.jpg" alt="midTbot" height="302" width="403"><br>
    - PCB DipTrace file : <a href="http://www.buildlog.net/blog/wp-content/uploads/2017/10/MidTBot_PCB_V1.zip">MidTBot_PCB_V1</a><br>
    - PCB Gerber file : <a href="http://www.buildlog.net/blog/wp-content/uploads/2017/10/midTbot_Gerber_v1.zip">midTbot_Gerber_v1</a>

# Summary for Drawing Robot
    - Configuration
    ```
    $0=10 (step pulse, usec)
    $1=25 (step idle delay, msec)
    $2=0 (step port invert mask:00000000)
    $3=0 (dir port invert mask:00000000)
    $4=0 (step enable invert, bool)
    $5=0 (limit pins invert, bool)
    $6=0 (probe pin invert, bool)
    $10=3 (status report mask:00000011)
    $11=0.010 (junction deviation, mm)
    $12=0.002 (arc tolerance, mm)
    $13=0 (report inches, bool)
    $20=0 (soft limits, bool)
    $21=0 (hard limits, bool)
    $22=0 (homing cycle, bool)
    $23=0 (homing dir invert mask:00000000)
    $24=25.000 (homing feed, mm/min)
    $25=500.000 (homing seek, mm/min)
    $26=250 (homing debounce, msec)
    $27=1.000 (homing pull-off, mm)
    $100=100.000 (x, step/mm) > GT2 Pully : 내경 5mm, 외경 13mm, 높이 14mm, Pitch 2mm, 16 teeth
    $101=100.000 (y, step/mm)
    $102=100.000 (z, step/mm)
    $110=3000.000 (x max rate, mm/min)
    $111=3000.000 (y max rate, mm/min)
    $112=3000.000 (z max rate, mm/min)
    $120=1000.000 (x accel, mm/sec^2)
    $121=1000.000 (y accel, mm/sec^2)
    $122=1000.000 (z accel, mm/sec^2)
    $130=300.000 (x max travel, mm)
    $131=220.000 (y max travel, mm)
    $132=200.000 (z max travel, mm)
    ```
    - Contents
        This drawing robot is similar to the commercially available AxiDraw. It is powered by an Arduino Uno controller, uses a CNC Shield, and GRBL firmware. The approximate cost to build this drawing robot is $100.

        Assembly documentation can be found in the Files section and at the following link. Thanks to Jonathan K for supplying this documentation.<br>
        https://docs.google.com/presentation/d/1GihJuR7yHVtUPYCp9GVDHLsJUhT2RwPrkIopzYrXYhw/edit?usp=sharing

        There's also a document which explains how to install Inkscape, the Inkscape MI extension, and the Universal G-Code Sender. It guides you through three example projects and can be found in the Files section of this Thing. Use these instructions instead of the last three pages of the assembly document which describe a different G-Code extension.

        This drawing robot allows you to draw things in Inkscape and then plot them out. The drawing robot receives G Code commands that are created inside an Inkscape extension called MI. Below are the links to the software used. There's a document in the Files section explaining how to use the software.

        Print all the parts. Assemble them using the assembly guide and then use the installation and use guide to start using your Draw Robot.

        When setting up your hardware you must do the following:

          1. Be sure to install 3 jumpers on the CNC Shield for each stepper driver. There's a photo showing the jumpers.
          2. You must use the GRBL version pointed to in the link below. Replace the "config.h" file with the one provided which has the correct features enabled before you compile and download from the Arduino IDE. IF YOU FAIL TO PERFORM THIS STEP, the robot will draw at a 45 degree angle. Don't send me a message about this because it means you failed to perform this step
          3. Set the GRBL parameters to the settings that are provided in one of the photos. This step is missing from the otherwise excellent instructions. You must do this or the robot will not work.
          4. Be sure to set the correct MI Extension parameters the first time you get the MI extension pop up.
          5. If you have problems with your stepper motors moving and you believe everything else above is OK, check that the small current adjustment on your stepper drivers are set mid point and also set the drive current to 1 amp using the correct procedure for your driver.

        I have posted all the parts needed from the two source designs. There are only 15 parts to print and none of them are very large. I added a stronger pen slider and a controller enclosure. There is an even better pen holder in the remix section. I also clarified the names that were in Spanish. I have posted all needed files so that there isn't confusion regarding which parts are needed from each of the original designs.

        My drawing robot is modified version of this one<br>
        https://www.thingiverse.com/thing:2058866

        Place this version of GRBL Firmware for the Arduino on your computer. You must use this version of GRBL. Other GRBL versions do not have the control code for the Z axis servo.<br>
        https://github.com/robottini/grbl-servo

        Replace the default config.h file in GRBL with the one supplied in the "Thing Files" section

        Upload GRBL to your Arduino Uno using these instructions<br>
        https://github.com/grbl/grbl/wiki/Compiling-Grbl (Ignore references to GRBL V1.1)<br>
        You must copy the config.h which I supply here to the directory where GRBL resides and then do the upload. The new config.h will be used for the compile of the GRBL code.

        Inkscape Drawing Software<br>
        https://inkscape.org/en/

        Universal G-Code Sender<br>
        https://winder.github.io/ugs_website/download/<br>

        Use the Inkscape MI Extension to generate G Code:<br>
        http://www.mediafire.com/file/ae0wquqornzc3o2/MI+Inkscape+Extension.zip<br>
        There is a tutorial in the Files section on how to use the software.

## HARDWARE NEEDED<br>
2x Nema 17 Stepper Motors<br>
2x Linear bearing rod M8 x 450mm, X Axis<br>
2x Linear bearing rod M8 x 350mm, Y axis<br>
2x Linear rod M3 x 75mm, Z Axis<br>
(You can find them in any old CDROM or purchase on EBay)<br>
1x M8x470mm threaded rod<br>
8x LM8UU linear bearings or printed bearings<br>
1x sg90 Servo<br>
2x GT2 Pulley 16 teeth<br>
5x Bearing 624zz<br>
1x 2000mm GT2 belt

misc M3 and M4 screws and nuts<br>
M8 nuts

## ELECTRONICS<br>
Arduino Uno<br>
CNC Shield<br>
12V 2A Wall Transformer<br>
https://www.amazon.com/Adapter-100-240V-Transformers-Switching-Adaptor/dp/B019Q3U72M<br>
2-4 limit switches ( optional. I suggest you leave them off and add later if you want them)

## SOFTWARE<br>
Inkscape which is the graphics design software (draw or import graphics)<br>
Inkscape MI GRBL Extension (convert graphics to G-Code)<br>
Universal G Code Sender (sends the G-Code to the robot causing drawing motion)<br>
GRBL which is the Arduino firmware (programmed into the Arduino Uno)

I have supplied a few G Code files that work with this drawing robot. If your drawing robot is built identical to this design, the G Code files will also work with yours.

Here are a couple of videos of this drawing robot in action:<br>
https://youtu.be/vTD7USqdXJI<br>
https://youtu.be/kpTIFBDcTaY

Update 6-15-2017: I added the limit switches about 10 days ago and they don't add much to the functionality. When GRBL sees a limit switch hit, it just stops with an alarm condition. You must soft reset the robot and your drawing cannot be continued. The homing feature doesn't seem to work. I read in another persons post that they could not get home to work in GRBL 0.9. At this point I suggest building the drawing robot without the limit switches. As long as your drawing does not exceed the envelope of the robot, you won't need the limit switches.

Update 6-19-2017: My friend found a better Inkscape Extension for generating G Code.<br>
I think the MI Extension is easier to use and generates better G Code:<br>
http://www.mediafire.com/file/ae0wquqornzc3o2/MI+Inkscape+Extension.zip

Update 6-26-2017:<br>
I added the config.h file needed for GRBL for this machine. With this file and the GRBL parameter settings in the screen shot, you should be able to easily get your machine up and running. Don't forget to install the stepper driver jumpers.

Update 7-4-2017:<br>
The top and bottom clam shells did not fit without pushing the LM8UU bearings slightly out of alignment. I removed a small amount of material from the top clamshell to allow clearance for the bottom clamshell posts. The old Top_XY_clamshell.stl file has been removed and replaced with the Top_XY_clamshell_V4.stl file. Thanks to rocketmannate who caught this problem.

Update 11-18-2017<br>
Jonathan K. provided assembly documentation. Thanks you so much. I appreciate your efforts. Checkout the great PDF with excellent photos.

Update 3-11-2018<br>
I have had some questions from people whose drawing robots didn't work. Here are some things to check If your robot doesn't work:
Here are some things to check If your robot doesn't work:
Make sure you have the correct version of GRBL (the one pointed to in the description)
Make sure you copied the config.h file to your GRBL directory
Check your CNC jumpers. All three should be installed
Check that you entered the GRBL parameters using Universal G-Code sender
If your Z axis motor isn't working, make sure you have the correct version of GRBL and that you wired your servo to the correct pins.
Make sure you used the MI extension parameters shown in screenshot specifically M3 and M5 for up and down on Z servo

Update: Sept. 18, 2018<br>
If you have problems with your stepper motors moving and you believe everything else above is OK, check that the small current adjustment on your driver is set mid point and then set the drive current to 1 amp using the correct procedure for your driver.
Thanks to Ashkangh for catching this possible issue.

Update: January 4, 2019<br>
A few people have run into software errors when using the GRBL MI Extension. This extension depends on a software package called Python. Your computer may not have this package or it may have one that is older or newer than the one this robot was tested with. I suggest that you do a Google search if you get a xxxx.py" error and follow the instructions for correcting code or installation of Python.

Also:<br>
There are various Stepper Motor drivers that are slightly different. in some cases the current adjust pot is on the opposite end of the module which can be confusing when trying to plug it in based on my photos. Be sure to check the pin names and plug your module in with the pin names that match. I'm sorry but I don't have time to figure out your individual hardware configuration problems. This design works but it can require some troubleshooting if software or hardware is different than what I happened to use. When you figure out your problem, be sure to post the solution in the comments so that others may benefit from your experience.
