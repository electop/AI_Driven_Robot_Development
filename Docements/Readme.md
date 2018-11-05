#AxiDraw User Guide

 . Link: https://cdn.evilmadscientist.com/wiki/axidraw/software/AxiDraw_V37r1.pdf

# EBB(EiBotBoard)
 . Description : http://www.schmalzhaus.com/EBB/
 . Code: https://github.com/evil-mad/EggBot

# cncserver API (RESTful)
 . Document: https://github.com/techninja/cncserver/blob/master/API.md

# RoboPaint remote print mode API (RESTful)
 . Document: https://github.com/evil-mad/robopaint-mode-remote/blob/master/API.md
 
# Scratch API (only Get)
 . Document: https://github.com/techninja/cncserver/blob/master/scratch/SCRATCH.API.md
 
#SW Installation (For Linux)
<pre>
The AxiDraw extension for Inkscape has been developed and tested extensively under Ubuntu. We expect it to work equally well in most Ubuntu derivatives and other distributions where Inkscape is known to work. However, we do not have the capability to test every distribution.

If you have a choice during installation, we strongly recommend to install the "flatpack" or "PPA" options instead of the "snap" option of Inkscape.


Ubuntu install instructions:

Install Inkscape 0.91
Launch Inkscape from the Applications menu, and then quit it.
Download the software in this ZIP archive (0.4 MB), and unzip it. (Your computer may unzip the archive automatically for you.)
From the "Go" menu, open your Home Folder (~).
From the "View" menu select "Show hidden files" -- the .config folder should be visible.
Place the contents of the folder inside the ZIP archive inside .config/inkscape/extensions/
Add your user account to the "dialout" group. (See below for details.)
Log out and log back in, for that group change to take effect.
The "AxiDraw" submenu should appear in the Extensions menu of Inkscape when you start Inkscape.

About adding your user account to the "dialout" group:

In modern Linux releases, it is often necessary to change your user permissions, to explicitly grant access to the USB port where the AxiDraw is located. This can be done by adding your user group to the "dialout" user group on your system.
Open up a terminal window
For most distributions (including Fedora and Ubuntu), enter the command "sudo usermod -a -G dialout <myUserName>" <return>, replacing the <myUserName> part with the user that is running Inkscape (and without the quotation marks or angle brackets!).
If you are unsure of your user name, enter the command "whoami" <return>, and the computer will happily remind you.
If you are unsure whether you are already in the "dialup" group, enter the command "groups" <return>, and the computer will list the groups that you are in.
After changing groups, you need to log out and log back in for the change to take effect.

sudo usermod -a -G dialout <myUserName>"

Debian Wheezy install instructions(command line):

Download the latest Inkscape extension .ZIP file from the downloads section of the AxiDraw Releases page.
Open up a terminal window, enter the command ,<return>, where you type your user name instead of UserName (And, no quotation marks.):
"sudo apt-get install inkscape"
"sudo apt-get install unzip python-lxml"
unzip the latest Inkscape extension .ZIP file into 
/home/'UserName'/.config/inkscape/extensions
Than you can use the AxiDraw extension for Inkscape by type: "inkscape" <return>

Troubleshooting

If your permissions are not correct (your user is not in the dialout group), you may get consistent "Unable to find an AxiDraw" type error messages.
If the AxiDraw menu doesn't appear in Inkscape, verify that when you've extract the zip file, all the .py files are inside .config/inkscape/extensions/ folder (you might have extracted the entire AxiDraw folder, and .py files might be misplaced)
</pre>
