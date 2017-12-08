from gui3 import ErrorScreen,DampleApp
from config import DOCPATH
import commands,os
from exceptions import OSError

"""
def showfunc(data):
 ls=commands.getoutput('cd ~/docs/%s/ && ls'%(data))
 if 'can\'t' in ls:
  d=ErrorScreen()
  d.mainloop()
 else:
  ls1=ls.split('\n')
  for i in ls1:
   os.system('eog %s'%(DOCPATH+'/'+data+'/'+i))
"""

def showfunc(data):
 #ls=commands.getoutput('cd ~/docs/%s/ && ls'%(data))
 #commands.getoutput('cd %s && ls' %(PATH)).split('\n')
 try:
  ls=os.listdir(DOCPATH+data)

 #if 'can\'t' in ls:
  #d=ErrorScreen()
  #d.mainloop()
 #else:
  #ls1=ls.split('\n')
  for i in ls:
   os.system('eog %s'%(DOCPATH+'/'+data+'/'+i))
 except OSError:
   d=ErrorScreen()
   d.mainloop()

w=DampleApp()
w.mainloop()
showfunc(w.phone)
