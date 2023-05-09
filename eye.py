import requests
import telegram
import os
import subprocess as sub 

#send to telegram
def send_to_telegram(message):


    apiURL = f'https://api.telegram.org/bot{telegram.apiToken}/sendMessage?chat_id={telegram.chatID}&text={message}'
    requests.get(apiURL)

#write hashes into a file 

def check_file():

       
    file_exist=os.path.exists("./eyewatcher/mirror")
    if file_exist == True:
        os.system("for i in `cat ./targetfile` ; do md5sum $i  >> ./eyewatcher/check ;hostname > ./eyewatcher/host ; done")
        #open files 
        check_file=open("./eyewatcher/check","r")
        check=check_file.readlines()
        mirror_file=open("./eyewatcher/mirror","r")
        host_file=open("./eyewatcher/host","r")
        host=host_file.read()
        mirror=mirror_file.readlines()
        for i in check:
            if i in mirror:
                pass
            else:
                
                send_to_telegram(i + " has been changed on "+host+" host")
                os.system("cat ./eyewatcher/mirror > ./eyewatcher/mirror.backup")
                os.system("cat ./eyewatcher/check > ./eyewatcher/mirror")
        os.system("rm -f ./eyewatcher/check")


        
    else: 
        os.system("rm -rf ./eyewatcher ;mkdir ./eyewatcher; for i in `cat ./targetfile` ; do md5sum $i >> ./eyewatcher/mirror ; done")

#run it        
check_file()
    
###






