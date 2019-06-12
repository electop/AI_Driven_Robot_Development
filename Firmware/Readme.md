### How to export hex file from arduion, using arduino IDE
   - cmd
   - cd C:\Program Files (x86)\Arduino\hardware\tools\avr\bin
   - if com port is com6, execute "avrdude.exe -p m328p  -c arduino -C "..\etc\avrdude.conf" -P com6 -U flash:r:"C:\flash.hex":i" on "명령 프롬프트"
   ```
   C:\Program Files (x86)\Arduino\hardware\tools\avr\bin>avrdude.exe -p m328p  -c arduino -C "..\etc\avrdude.conf" -P com7 -U flash:r:"C:\flash.hex":i

   avrdude.exe: AVR device initialized and ready to accept instructions

   Reading | ################################################## | 100% 0.00s

   avrdude.exe: Device signature = 0x1e950f (probably m328p)
   avrdude.exe: reading flash memory:

   Reading | ################################################## | 100% 4.10s

   avrdude.exe: writing output file "C:\flash.hex"

   avrdude.exe: safemode: Fuses OK (E:00, H:00, L:00)

   avrdude.exe done.  Thank you.
   ```
   
