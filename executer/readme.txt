This executer will monitor the folder containing the uploaded hex files. Each of the hex file will be read and programmed into the arduino attached to the usb port of the raspberry Pi. Make sure to configure the usb device file and uploaded folder location properly before using this program.

The sample usage is:
python executer.py




basic avrdude usage:
avrdude -C./etc/avrdude.conf -v -v -v -v  -patmega328p -carduino -P/dev/tty.usbmodem1421 -b115200 -D -Uflash:w:./sampleHex/blink.cpp.hex:i
