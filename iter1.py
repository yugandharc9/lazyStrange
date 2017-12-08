import commands,qrtools
from config import PATH
from gui3 import InvalidScreen,SampleApp 
from PIL import Image
import qrcode
import os
from openall import showfunc

def watch():
 return commands.getoutput('cd %s && ls' %(PATH)).split('\n')

while True:
 if watch()==['']:
  pass
 else:
  str2=watch().pop()
  str1=str2.replace('\n','')
  qr=qrtools.QR()
  check= qr.decode(PATH+str1)
  if not check:
   w=SampleApp()
   w.mainloop()
   img=qrcode.make(w.phone)
   img.save(PATH+w.phone)
   saved=Image.open(PATH+w.phone)
   im2=saved.resize((80,80))

   srcdoc=Image.open(PATH+str1)
   srcdoc.paste(im2,(0,0))
   srcdoc.save(PATH+str1)
   os.system('rm %s' %(PATH+w.phone))
   os.system('mkdir -p ~/docs/%s'%w.phone)
   mv=os.system('mv %s ~/docs/%s/'%(PATH+str1,w.phone))
   if mv==0:
    if check:
     showfunc(str(qr.data))
   else:
    raise "Bad Contact Yugandhar"
  else:
   img=qrcode.make(str(qr.data))
   img.save(PATH+str(qr.data))
   saved=Image.open(PATH+str(qr.data))
   im2=saved.resize((80,80))

   srcdoc=Image.open(PATH+str1)
   srcdoc.paste(im2,(0,0))
   srcdoc.save(PATH+str1)
   os.system('rm %s' %(PATH+str(qr.data)))
   os.system('mkdir -p ~/docs/%s'%str(qr.data))
   mv=os.system('mv %s ~/docs/%s/'%(PATH+str1,str(qr.data)))
   if mv==0:
    showfunc(str(qr.data))
    pass
   else:
    raise "Bad Contact Yugandhar"
