#!python3

#
#        
# by zz  
#
#2014/4/19

#I know! Let's use ttk!

from tkinter import *
from tkinter import ttk
import re


TEXTWIDTH=90



def translate(*args):
    s=link.get()
    s=s.encode('ascii','ignore').decode('ascii')
    pattern=re.compile(r'\s*')
    url.set(re.sub(pattern,'',s))

#####




root=Tk()
root.title("Convert link to url")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

link = StringVar()
url = StringVar()

link_entry=ttk.Entry(mainframe, width=TEXTWIDTH,textvariable=link)
url_entry=ttk.Entry(mainframe,width=TEXTWIDTH,textvariable=url)

link_entry.grid(column=1, row=1, sticky=(W,E))
url_entry.grid(column=1, row=3,sticky=(W,E))

url_entry.state(['readonly'])

ttk.Button(mainframe, text="translate",command=translate).grid(column=2,row=2,sticky=(W))

link_entry.focus()
root.bind('<Return>',translate)
root.mainloop()


