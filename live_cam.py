import time
import picamera
import requests
import json
import ftplib
import os

def upload_image(image_name):
    print("uploading")
    username = "raspberry@owlpost.io"
    password = "JXBZDVuhCTLT2Sqh2Jsx"
    host = "ftp.owlpost.io"
    session = ftplib.FTP(host,username,password)
    file = open(image_name,'rb')                  # file to send
    session.storbinary("STOR " + image_name, file)     # send the file 
    file.close()
    session.quit()
    print("sent")

def html_post_image(image_name):
    url = 'http://owlpost.io/receive.php'
    files = {'file': open(image_name, 'rb')}
    try:
        r = requests.post(url, files=files)
    except requests.exceptions.RequestException as e:
        print e
        sleep(60)
    print "html sent"
    


with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(10) #warmup

    for filename in camera.capture_continuous('images/image{counter:05d}.jpg'):
        print('Captured %s' % filename)
#        upload_image(filename)
        html_post_image(filename)
        os.remove(filename)
        time.sleep(10) # wait 5 seconds
        

