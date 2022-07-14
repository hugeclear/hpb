#coding: utf-8
import webiopi
import os
import datetime
SAVEDIR = '/home/pi/ex6'
@webiopi.macro
def camera(no):
filename = SAVEDIR + '/camera_' + no + '.jpg'
command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename
os.system(command)
os.system('sync')
@webiopi.macro
def Time():
now = datetime.datetime.now()
now_datetime = (str(now.year) + " " + str(now.month) + " " +
str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" +
str(now.second))
return now_datetime
os.system('sync')
#camera('1')