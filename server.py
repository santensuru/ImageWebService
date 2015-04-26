#!/usr/bin/env python

from ladon.ladonizer import ladonize
from PIL import Image
import base64
import StringIO

class ImageConverter(object):

    @ladonize(str,str,rtype=str)
    def grayscale(self,input,format):
        ba = bytearray(base64.b64decode(input))
        
        # Convert to grayscale
        buff = StringIO.StringIO()
        buff.write(ba)
        #seek back to the beginning so the whole thing will be read by PIL
        buff.seek(0)
        img = Image.open(buff).convert('L')
        
        # Convert to string
        output = StringIO.StringIO()
        img.save(output, "png")
        contents = output.getvalue()
        output.close()

        #return grayscale
        bytes = bytearray(contents)
        s = base64.b64encode(bytes)
        return s

