from gui3 import ErrorScreen,DampleApp
from config import DOCPATH
import commands,os



def showfunc(data):
 ls=commands.getoutput('cd ~/docs/%s/ && ls'%(data))
 if 'can\'t' in ls:
  d=ErrorScreen()
  d.mainloop()
 else:
  ls1=ls.split('\n')
  for i in ls1:
   os.system('eog %s'%(DOCPATH+'/'+data+'/'+i))

 
w=DampleApp()
w.mainloop()
showfunc(w.phone)
