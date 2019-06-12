### How to export hex file from arduino uno, using IDE
   - cmd
   - cd C:\Program Files (x86)\Arduino\hardware\tools\avr\bin
   - if com port is com7, execute "avrdude.exe -p m328p  -c arduino -C "..\etc\avrdude.conf" -P com7 -U flash:r:"C:\flash.hex":i" on "명령 프롬프트"
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

### How to flash hex file into arduino uno, using IDE
   - cmd
   - cd C:\Program Files (x86)\Arduino\hardware\tools\avr\bin
   - if com port is com7 and there is hex file at C drive root, execute "avrdude.exe -p m328p  -c arduino -C "..\etc\avrdude.conf" -P com7 -U flash:w:"C:\flash.hex":i" on "명령 프롬프트"<br>
     if there is no available hex file, please use 'falsh.hex' on this path.
   ```
   C:\Program Files (x86)\Arduino\hardware\tools\avr\bin>avrdude.exe -p m328p  -c arduino -C "..\etc\avrdude.conf" -P com7 -U flash:w:"C:\flash.hex":i

   avrdude.exe: AVR device initialized and ready to accept instructions

   Reading | ################################################## | 100% 0.00s

   avrdude.exe: Device signature = 0x1e950f (probably m328p)
   avrdude.exe: NOTE: "flash" memory has been specified, an erase cycle will be performed
                To disable this feature, specify the -D option.
   avrdude.exe: erasing chip
   avrdude.exe: reading input file "C:\flash.hex"
   avrdude.exe: writing flash (32768 bytes):

   Writing | ################################################## | 100% 5.39s

   avrdude.exe: 32768 bytes of flash written
   avrdude.exe: verifying flash memory against C:\flash.hex:
   avrdude.exe: load data flash data from input file C:\flash.hex:
   avrdude.exe: input file C:\flash.hex contains 32768 bytes
   avrdude.exe: reading on-chip flash data:

   Reading | ################################################## | 100% 4.13s

   avrdude.exe: verifying ...
   avrdude.exe: 32768 bytes of flash verified

   avrdude.exe: safemode: Fuses OK (E:00, H:00, L:00)

   avrdude.exe done.  Thank you.
   ```
