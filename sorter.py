import commands,qrtools
from config import INSTALLPATH,PATH,DOCPATH
from gui3 import InvalidScreen,SampleApp 
from PIL import Image
import qrcode
import shutil,os
from openall import showfunc
import random,time



def watch():
 #return commands.getoutput('cd %s && ls' %(PATH)).split('\n')
 return os.listdir(PATH)
def renamer(rpath):
 #print rpath
 for filename in os.listdir(rpath):
  os.chdir(rpath)
  os.rename(filename,filename.replace(' ',''))


while True:
 if watch()==[]:
  pass
 else:
  time.sleep(2)
  renamer(PATH)
  str1=watch().pop()
  #print str1
 
  qr=qrtools.QR()
  check= qr.decode(PATH+str1)
  if not check:
   f=open(INSTALLPATH+'last','r')
   passed=f.read().replace('\n','')        
   f.close()
   w=SampleApp(passed)
   w.mainloop()
   img=qrcode.make(w.phone)
   img.save(PATH+w.phone)
   saved=Image.open(PATH+w.phone)
   im2=saved.resize((80,80))

   srcdoc=Image.open(PATH+str1)
   srcdoc.paste(im2,(0,0))
   srcdoc.save(PATH+str1)
   #os.system('rm %s' %(PATH+w.phone))
   os.remove(PATH+w.phone)
   #os.system('mkdir -p ~/docs/%s'%w.phone)
   if not os.path.exists(DOCPATH+w.phone):
    os.makedirs(DOCPATH+w.phone)
   #mv=os.system('mv %s ~/docs/%s/'%(PATH+str1,w.phone))
   files=os.listdir(PATH)
   #for f in files:
   try:
    shutil.move(PATH+str1,DOCPATH+w.phone)
   except:
    num=str(random.random())[11:]
    shutil.move(PATH+str1,DOCPATH+'/%s/'%w.phone+num+str1)
   #if mv==0:
   if check:
    showfunc(str(qr.data))
   else:
    pass
    #raise "Bad Contact Yugandhar"
  else:
   img=qrcode.make(str(qr.data))
   img.save(PATH+str(qr.data))
   saved=Image.open(PATH+str(qr.data))
   im2=saved.resize((80,80))

   srcdoc=Image.open(PATH+str1)
   srcdoc.paste(im2,(0,0))
   srcdoc.save(PATH+str1)
   #os.system('rm %s' %(PATH+str(qr.data)))

   os.remove(PATH+qr.data)
   #os.system('mkdir -p ~/docs/%s'%str(qr.data))
  
   if not os.path.exists(DOCPATH+qr.data):
    os.makedirs(DOCPATH+qr.data)
   #mv=os.system('mv %s ~/docs/%s/'%(PATH+str1,str(qr.data)))
  
   files=os.listdir(PATH)
   #for f in files:
   try:
    shutil.move(PATH+str1,DOCPATH+qr.data)
   except:
    num=str(random.random())[11:]
    shutil.move(PATH+str1,DOCPATH+'/%s/'%qr.data+num+str1)
   #print mv
   #if mv==0:
   showfunc(str(qr.data))
   #pass
   #else:
   #raise "Bad Contact Yugandhar"
