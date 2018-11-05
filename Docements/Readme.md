## RoboPaint for AxiDraw
### cncserver API (RESTful)
 . Document: https://github.com/techninja/cncserver/blob/master/API.md

### RoboPaint remote print mode API (RESTful)
 . Document: https://github.com/evil-mad/robopaint-mode-remote/blob/master/API.md
 
### Scratch API (only Get)
 . Document: https://github.com/techninja/cncserver/blob/master/scratch/SCRATCH.API.md

## Information
### AxiDraw User Guide
 . Link: https://cdn.evilmadscientist.com/wiki/axidraw/software/AxiDraw_V37r1.pdf

### EBB(EiBotBoard)
 . Description : http://www.schmalzhaus.com/EBB/
 . Code: https://github.com/evil-mad/EggBot

## SW Installation (For Linux)
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

<pre>
Inkscape 용 AxiDraw 확장은 우분투에서 광범위하게 개발되고 테스트되었습니다.
우리는 Inkscape가 잘 작동하는 우분투 파생 상품 및 기타 배포판에서도 똑같이 잘 작동 할 것으로 기대합니다.
그러나 모든 배포를 테스트 할 수있는 기능이 없습니다.
설치 중에 선택할 수있는 경우 Inkscape의 "snap"옵션 대신 "flatpack"또는 "PPA"옵션을 설치하는 것이 좋습니다.

###우분투 설치 지침 :
잉크 스케이프 0.91 설치
응용 프로그램 메뉴에서 잉크 스케이프를 시작한 다음 종료 하십시오.
이 ZIP 아카이브 (0.4 MB)에 소프트웨어를 다운로드하고 압축을 풉니다. (컴퓨터가 자동으로 압축 파일의 압축을 풀 수 있습니다.)
"이동"메뉴에서 홈 폴더 (~)를 엽니 다.
"보기"메뉴에서 "숨김 파일 표시"를 선택하십시오. - .config 폴더가 표시 되어야 합니다.
.config / inkscape / extensions / 내에 ZIP 아카이브 안에 폴더의 내용을 넣습니다.
사용자 계정을 "전화 걸기"그룹에 추가하십시오. (자세한 내용은 아래를 참조하십시오.)
해당 그룹 변경 사항을 적용하려면 로그 아웃했다가 다시 로그인하십시오.
Inkscape를 시작하면 "AxiDraw"하위 메뉴가 Inkscape의 Extensions 메뉴에 나타납니다.

"dialout"그룹에 사용자 계정 추가 정보 :
최신 Linux 릴리스에서는 사용자 권한을 변경하여 AxiDraw가있는 USB 포트에 대한 액세스 권한을 명시 적으로 부여해야하는 경우가 있습니다.
이것은 사용자 그룹을 시스템의 "dialout"사용자 그룹에 추가하여 수행 할 수 있습니다.
터미널 창을 여십시오.
Fedora와 Ubuntu를 포함한 대부분의 배포판의 경우 "sudo usermod -a -G dialout"명령을 입력하여 Inkscape를 실행중인 사용자로 부품을 교체합니다.
(따옴표 또는 꺾쇠 괄호는 사용하지 마십시오!).
사용자 이름이 확실하지 않은 경우 "whoami"명령을 입력하면 컴퓨터가 즐겁게 알려줍니다.
이미 "전화 접속"그룹에 있는지 여부가 확실하지 않은 경우 "그룹"명령을 입력하면 컴퓨터에 현재있는 그룹이 나열됩니다.
그룹을 변경하고 로그 아웃 한 다음 다시 로그인해야 변경 사항이 적용됩니다.

sudo usermod -a -G dialout "
데비안 Wheezy 설치 지침 (명령 줄) :

AxiDraw Releases 페이지의 다운로드 섹션에서 최신 Inkscape 확장자 .ZIP 파일을 다운로드하십시오.
터미널 창을 열고 명령을 입력하십시오. 여기서 UserName 대신 사용자 이름을 입력하십시오 (따옴표 제외).
"sudo apt-get install inkscape"
"sudo apt-get install unzip python-lxml"
최신 Inkscape 확장자 .ZIP 파일의 압축을 풉니 다. 
/home/'UserName'/.config/inkscape/extensions
Inkscape 용 AxiDraw 확장자를 "inkscape"형식으로 사용할 수 있습니다. 

###문제 해결
권한이 올바르지 않은 경우 (사용자가 전화 걸기 그룹에 있지 않은 경우) 일관된 "AxiDraw를 찾을 수 없음"유형의 오류 메시지가 표시 될 수 있습니다.
AxiDraw 메뉴가 Inkscape에 나타나지 않으면 zip 파일의 압축을 풀었을 때 모든 .py 파일이 .config / inkscape / extensions / 폴더 안에 있는지 확인하십시오 (AxiDraw 폴더 전체를 추출했을 수도 있고 .py 파일이 잘못 배치되었을 수 있음)
</pre>
