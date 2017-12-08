import Tkinter as tk
from config import INSTALLPATH
class SampleApp(tk.Tk):
    
    def __init__(self,passer):
        tk.Tk.__init__(self)
        self.title(u"ThingsLab - AutoSort")
        self.entry = tk.Entry(self,width=50,borderwidth=5,text="d")

        self.lbl=tk.Label(self,text="Enter Unique Identifier",font=3)

        self.lbl2=tk.Label(self,text='\n')

        self.button = tk.Button(self, text="AutoSort", command=self.on_button)
                
        self.lbl1=tk.Label(self,text="\n\nThingslab - AutoSort Utility \n can \n1.Tag documents with Unique Id\n2.Sort Documents in blink of an eye - just paste them in \'watcher\' folder \n 3.Fetch documents by unique identifier or by Image\n")

        self.entry.insert(0,passer) 

        self.lbl2.pack()
        self.lbl.pack()

        self.lbl2.pack()
        self.entry.pack()

        self.lbl2.pack()
        self.button.pack()
        self.lbl1.pack()
    def on_button(self):
        self.phone=self.entry.get().replace(' ','')
        filewriter(self.phone)
        self.destroy()

class DampleApp(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title(u"ThingsLab - AutoSort ")
        self.entry = tk.Entry(self,width=50,borderwidth=5,text="d")

        self.lblv=tk.Label(self,text="Viewer",font=3)
        self.lbl=tk.Label(self,text="Enter Unique Identifier",font=3)

        self.lbl2=tk.Label(self,text='\n')

        self.button = tk.Button(self, text="Fetch", command=self.on_button)
                
        self.lbl1=tk.Label(self,text="\n\nThingslab - AutoSort Utility \n can \n1.Tag documents with Unique Id\n2.Sort Documents in blink of an eye - just paste them in \'watcher\' folder \n 3.Fetch documents by unique identifier or by Image\n")

        self.entry.insert(0,'') 

        self.lblv.pack()
        self.lbl2.pack()
        self.lbl.pack()

        self.lbl2.pack()
        self.entry.pack()

        self.lbl2.pack()
        self.button.pack()
        self.lbl1.pack()
    def on_button(self):
        self.phone=self.entry.get().replace(' ','')
        filewriter(self.phone)
        self.destroy()

def filewriter(num):
 f=open(INSTALLPATH+'last','w')
 f.write(num)
 f.close()
       
class InvalidScreen(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.lbl=tk.Label(self,text="You gave an Invalid File")
        self.button = tk.Button(self, text="Exit", command=self.on_button)
        

        self.lbl.pack()
        self.button.pack()

    def on_button(self):
        self.destroy()


class ErrorScreen(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.lbl=tk.Label(self,text="No record associated with given number")
        self.button = tk.Button(self, text="Exit", command=self.on_button)
        

        self.lbl.pack()
        self.button.pack()

    def on_button(self):
        self.destroy()
