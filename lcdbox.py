#!/usr/bin/python
import serial, time, sys
from subprocess import *
from time import sleep, strftime
from datetime import datetime

#/dev/lcdbox
#/dev/ttyUSB0
#sudo apt-get install python-serial

try:
    f = open('/dev/lcdbox')
except IOError:
    print 'LCD Box not found... moving on'
    sys.exit()

ser = serial.Serial('/dev/lcdbox',  9600, timeout = 0.1)

if(ser.isOpen() == False):
        sys.exit()

#if you only want to send data to arduino (i.e. a signal to move a servo)
ser.write( "Example Serial Comm ".ljust(32));
time.sleep(10);

cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

while 1:

        ipaddr = run_cmd(cmd)
        ser.write(datetime.now().strftime('%b %d %H:%M:%S').ljust(16))
        ser.write('IP %s' % ( ipaddr ).ljust(16))
        sleep(5)

