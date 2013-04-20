#!/usr/bin/env python
import subprocess
import logging

#to be configured based on the Raspbery 
avrdude_location = "avrdude"
avrdude_conf = "-C%s" %"./etc/avrdude.conf"
command = [avrdude_location, avrdude_conf]

"""
Uploads the hex program for particular device.
Currently Arduino UNO and diecimila are only supported
"""
def upload(target_hexfile, device_type):
    usb_device = "-P%s" %"/dev/tty.usbmodem1421"
    #target_hexfile = "./sampleHex/blink.cpp.hex"
    
    #to be configured based on the target device
    if device_type is "UNO":  #for UNO    
        _processor = "atmega328p"
        baud_rate = "115200"
    elif device_type is "diecimila":   #for diecimila
        _processor ="atmega168"
        baud_rate = "19200"

    part_no = "-p%s" % _processor    
    mem_ops = "-Uflash:w:%s:i"% target_hexfile
    arguments = [part_no, "-carduino", usb_device, "-b", baud_rate, "-D", mem_ops]
    command.extend(arguments)
    
    returncode = -1
    
    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        proc.wait()     
        returncode = proc.returncode
    except OSError, e:
        print "error while update=%s" % e
    
    return returncode
    
def main():
    if (upload("./sampleHex/blink.hex", "UNO") == 0) :
        print "Successfully uploaded"
    else:
        print "Unsuccessful upload"

if __name__ == '__main__':
    main()
