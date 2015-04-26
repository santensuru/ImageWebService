#!/usr/bin/env python

from suds.client import Client
from PIL import Image
import base64
import StringIO
import thread
import datetime
import os

'''
client = Client('http://localhost:8080/ImageConverter/soap/description')
'''

path = "/home/pi/image/"
dest_path = "/home/pi/image/bw/"

dir = os.listdir(path)
files = []
files2 = []
files3 = []

i = 0
for file in dir:
    if ".png" in file or ".jpg" in file:
        if i%3 == 0:
            files.append( file )
        elif i%3 == 1:
            files2.append( file )
        else:
            files3.append( file ) 
        #print files
        i = i + 1
    
'''
thread.start_new_thread( do_convert, (files, "1", datetime.datetime.now()) )
'''



def do_convert( list_name, name, time ):
    client = Client('http://' + name + ':8080/ImageConverter/soap/description')
    print name, time    
    
    for file in list_name:
        print file
        
        img = Image.open(path + file)
        if ".png" in file:
            format = "png"
        else:
            format = "jpeg"
        
        # Convert to string
        output = StringIO.StringIO()
        img.save(output, format)
        contents = output.getvalue()
        output.close()
        
        # Get grayscale
        bytes = bytearray(contents)
        s = base64.b64encode(bytes)
        
        input = client.service.grayscale(s, format)
        
        ba = bytearray(base64.b64decode(input))
        
        # Convert to save
        buff = StringIO.StringIO()
        buff.write(ba)
        #seek back to the beginning so the whole thing will be read by PIL
        buff.seek(0)
        img = Image.open(buff)
        
        img.save(dest_path + "gs_" + file, format)
        
        print "done", "gs_" + file, datetime.datetime.now()


try:
    thread.start_new_thread( do_convert, (files, "localhost", datetime.datetime.now()) )
    thread.start_new_thread( do_convert, (files2, "10.151.12.201", datetime.datetime.now()) )
except:
    print "Error"

while 1:
    pass
print "???"

'''
thread.start_new_thread( do_convert, (files, "1", datetime.datetime.now()) )
'''
