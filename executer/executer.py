import os
import time
import uploader

#configure according to webserver upload folder locaion
datafolder = "/var/www/ArduSAT/uploads/"

def monitor_folder(device_type):
    folder_name = "%s/%s" % (datafolder , device_type)
    #folder_name = datafolder
    filenames = os.listdir(folder_name)
    
    
    for filename in filenames:
        print filenames
        
        file_infos=filename.split("_")
        timestamp = int(file_infos[0])
        #duration  = int(file_infos[1])
        duration = 20  #hardcoded for 20 seconds for now
        
        relative_filepath = "%s/%s" % (folder_name,filename)

        print "Going to send %s for uplaod" % relative_filepath
        if (uploader.upload(relative_filepath, device_type) == 0):        
            #allow it to execute for specfied time
            print "Hex File %s uploaded. Now allowing to executer for %d seconds" % (relative_filepath,duration)
            time.sleep(duration)
            
            #remove the file
            print "Removing the file %s" % relative_filepath
            os.unlink(relative_filepath)
            
        print "-------------------------------------------------------"

    
    
        
    return
    
"""
Main loop of the server
"""
def process():
    
    while True:
        monitor_folder("uno")
        time.sleep(2)
        monitor_folder("freeduino")
        time.sleep(2)
    return

def main():
    process()
    

if __name__ == '__main__':
    main()
