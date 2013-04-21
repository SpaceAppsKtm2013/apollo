#!/usr/bin/env python
import subprocess
import logging

#to be configured based on the Raspbery 
avrdude_location = "avrdude"
avrdude_conf = "-C%s" %"/etc/avrdude.conf"


"""
Uploads the hex program for particular device.
Currently Arduino uno and freeduino are only supported
"""
def upload(target_hexfile, device_type):
    command = [avrdude_location, avrdude_conf]
    #print "Upload got %s for burning" % target_hexfile
    
    usb_device = "-P%s" %"/dev/ttyACM0"
    #target_hexfile = "./sampleHex/blink.cpp.hex"
    
    #to be configured based on the target device
    if device_type is "uno":  #for uno    
        _processor = "atmega328p"
        baud_rate = "115200"
        usb_device = "-P%s" %"/dev/ttyACM0" 
    elif device_type is "freeduino":   #for freeduino 
        _processor ="atmega328p"
        baud_rate = "57600"
        usb_device = "-P%s" %"/dev/ttyUSB0"

    part_no = "-p%s" % _processor    
    mem_ops = "-Uflash:w:%s:i"% target_hexfile
    arguments = [part_no, "-carduino", usb_device, "-b", baud_rate, "-D", mem_ops]
    command.extend(arguments)
    
    returncode = -1
    
    try:
        proc = subprocess.Popen(command, close_fds=True )
        proc.communicate()     
        returncode = proc.returncode
    except OSError, e:
        print "error while update=%s" % e
    
    return returncode
    
def main():
    if (upload("./sampleHex/blink_uneven.hex", "uno") == 0) :
        print "Successfully uploaded"
    else:
        print "Unsuccessful upload"

if __name__ == '__main__':
    main()
