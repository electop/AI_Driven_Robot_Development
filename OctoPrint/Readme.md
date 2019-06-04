# Prerequites
 - <a href="https://octopi.octoprint.org/latest">1. OctoPrint Download</a><br>
 - <a href="https://github.com/pbatard/rufus/releases/download/v3.5/rufus-3.5p.exe">2. rufs portable Download</a><br>
  . <a href="https://m.blog.naver.com/PostView.nhn?blogId=seoulworkshop&logNo=221262339483&proxyReferer=https%3A%2F%2Fwww.google.com%2F">How to make a OctoPrint image on SD card, using rufs tool</a><br>
 ## Your Raspberry Pi(@OctoPrint)
  . ID : **pi**, Password : **raspberry**<br>
  . $cd boot > $nano pctopi-wpa-supplicant.txt<br>
  . ...<br>
    network={<br>
      ssid=**"YOUR_AP_NAME"**<br>
      psk=**"YOUR_AP_PW"**<br>
    }<br>
    ...<br>
  . ^X > Y<br>
  . $ifconfig > Checking the IP address of your OctoPrint device: (e.g.)192.168.0.x<br>
  . $sudo raspi-config > Choice "5. Interfacing Options" > Choice "P2 SSH" > Choice "Yes"<br>
  . $sudo reboot<br>
 ## Your PC(@Ubuntu)
  . $sudo apt-get install putty<br>
  . $putty > Host Name: "YOUR_OCTOPRINT_DEVICE_IP" > Saved Sessions: "OctoPrint" > Click "Save" button<br>

### <a href="https://cosmosjs.blog.me/221516473588">라즈베리파이와 OctoPrint를 이용한 3D 프린터 원격제어</a>
### <a href="https://seoulworkshop.blog.me/221265052717">공유기 포트포워딩 설정하기</a>
### <a href="https://m.blog.naver.com/PostView.nhn?blogId=seoulworkshop&logNo=221262339483&proxyReferer=https%3A%2F%2Fwww.google.com%2F">OctoPrint 세팅 2 - OctoPi 설치 및 WiFi 연결 설정</a>
### <a href="https://studyforus.tistory.com/27">외부IP에서 내 컴퓨터(내부 IP)로 접속하기</a>
### <a href="https://bugwhale.com/raspberry-octoprint-install-02/">라즈베리파이에 옥토프린트 설치하기 - 02. 초기 설정하기</a>
### <a href="https://bugwhale.com/raspberry-octoprint-install-04/">라즈베리파이에 옥토프린트 설치하기 - 04. 전원 작업하기</a>
