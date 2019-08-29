# -*- coding: utf-8 -*-

import os
import sys
import binascii
import re
import codecs
pattern = re.compile(r'\s+')
directory = os.listdir('/fanu/name')
os.chdir('/fanu/name')
for file in directory:
    r = file
    faxman = r.find('.KY2')
    if faxman == -1 :
        print(r+' pass')
    else :
        rx=r.replace(".KY2", "")
        f=open(r,'rb')
        f.seek(48)
        fanu=f.read(256)
        fanu1=fanu.split(b'\0',1)[0]
        momiji=fanu1.decode('UTF-8')
        #print(momiji)
        f.seek(48+256+256)
        funga=f.read(256)
        funga1=funga.split(b'\0',1)[0]
        funz=funga1.decode('UTF-8')
        #print(funz)
        data1 = rx+'\n'+momiji+'\n'+funz+'\n'+'\n'
        z=codecs.open('list.txt','a',encoding="utf-8")
        z.write(data1)
z.close()