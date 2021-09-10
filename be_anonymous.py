import tkinter as tk
import os
from tkinter import messagebox
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0,column=1)
        self.entry1.place(x=135, y=100)
        self.b1 = tk.Button(self, text="Search", bg='black', fg='#469A00',command=lambda:self.if_not(self.entry1.get()))
        self.b2 = tk.Button(self, text="Download", bg='black', fg='#469A00',command=self.if_dont_exists)
        self.b2.grid(row=0,column=1)
        self.b1.grid(row=0,column=1)
        self.b1.place(x=135,y=130)
        self.b2.place(x=200,y=130)
    def if_dont_exists(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Download Page")
        self.b1 = tk.Button(self.root, text="Tor Server Download", bg='black', fg='#469A00',command=lambda:self.check_it())
        self.b1.grid(row=0, column=1)
        self.b1.place(x=135, y=130)
        self.b2 = tk.Button(self.root,text="ProxyChain Download", bg='black', fg='#469A00',command=lambda:self.check_it2())
        self.b2.grid(row=0, column=1)
        self.b2.place(x=135, y=160)
        self.b3 = tk.Button(self.root, text="Run Tor", bg='black', fg='#469A00',command=self.run_tor)
        self.b3.grid(row=0,column=1)
        self.b3.place(x=135,y=190)
    def check_it(self):
        self.command = "apt-get install tor -y"
        os.popen(self.command)
        messagebox.showinfo(detail="Installing,wait for a sec")
    def check_it2(self):
        self.command = "apt-get install proxychains -y"
        os.popen(self.command)
        messagebox.showinfo(detail="Installing,wait for a sec")
    def if_not(self,url):
        if not str(self.entry1.get()):
            messagebox.showinfo(detail="Enter Any URL")
        else:
            self.command = ("proxychains firefox %s" % (str(url)))
            os.popen(self.command)
    def run_tor(self):
        self.command = "service tor start"
        os.popen(self.command)
app = App()
app.geometry("400x300")
app.title("Be Anonymous")
app.mainloop()

