#!/usr/bin/env python

from suds.client import Client
from PIL import Image
import base64
import StringIO

client = Client('http://localhost:8080/ImageConverter/soap/description')

img = Image.open("lena.png")
format = "png"

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

img.save("gs2_lena.png", format)

print "done"
