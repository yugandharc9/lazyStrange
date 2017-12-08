import Tkinter as tk

class SampleApp(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.lbl=tk.Label(self,text="Enter Mobile Number")
        self.button = tk.Button(self, text="AutoSort", command=self.on_button)
        

        self.lbl.pack()
        self.entry.pack()
        self.button.pack()

    def on_button(self):
        self.phone=self.entry.get().replace(' ','')
        self.destroy()

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
