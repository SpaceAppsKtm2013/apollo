Sample code:

avrdude -C./etc/avrdude.conf -v -v -v -v  -patmega328p -carduino -P/dev/tty.usbmodem1421 -b115200 -D -Uflash:w:./sampleHex/blink.cpp.hex:i