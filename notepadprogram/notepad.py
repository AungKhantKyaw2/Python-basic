
import os
from tkinter import *
from tkinter import filedialog,colorchooser,font
from tkinter.messagebox import *
from tkinter.filedialog import *


def changecolor():
    color = colorchooser.askcolor(title="pick a color")
    textarea.config(fg=color[1])

def change_font(*args):
    textarea.config(font=(font_name.get(),size_box.get()))

def newfile():
    window.title("Untitled")
    textarea.delete(1.0,END)

def openfile():
    file = askopenfilename(defaultextension = ".txt",file=[("All Files","*.*"),("Text Documents","*.txt")])
    
    try: 
        window.title(os.path.basename(file))    
        textarea.delete(1.0,END)
        with open(file,'r') as file:
            textarea.insert(1.0,file.read())
    except:
        print("Cannot do shit")  
    finally:
        file.close()       

def savefile():
    file = filedialog.asksaveasfilename(initialfile='untitled txt',
                                      defaultextension = ".txt",
                                        filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file is None:
        return
    try : 
         window.title(os.path.basename(file))
         file = open(file,"w")
         file.write(textarea.get(1.0,END))
    except :
           print("Do u want to save")
    finally : 
           file.close() 
def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")
    

def about():
    showinfo("About the program","This is the program written by u")

def quit():
    window.destroy()

window = Tk()
window.title("notepad editor program")
file =None

window_width =500
window_height=500

screen_width =window.winfo_screenwidth()    
screen_height = window.winfo_screenheight()

x= int((screen_width/2)-(window_width/2))
y= int((screen_height/2)-(window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

font_name =StringVar(window)
font_name.set("Arial")

font_size =StringVar(window)
font_size.set("25") 

textarea =Text(window, font=(font_name.get(),font_size.get()))

scrollbar =Scrollbar(textarea)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)


textarea.grid(sticky=N+E+S+W)
scrollbar.pack(side=RIGHT,fill=Y)
textarea.config(yscrollcommand=scrollbar.set)
frame =Frame(window)
frame.grid()
colorbutton =Button(frame,text="color",command=changecolor)
colorbutton.grid(row=0,column=0)

font_box = OptionMenu(frame,font_name,*font.families(),command=lambda:change_font)
font_box.grid(row =0 ,column=1)

size_box =Spinbox(frame, from_=1 ,to=100,textvariable=font_size,command=change_font)
size_box.grid(row=0,column=2)

menu_bar =Menu(window)
window.config(menu=menu_bar)

File_menu =Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=File_menu)
File_menu.add_command(label="New",command=newfile)
File_menu.add_command(label="Open",command=openfile)
File_menu.add_command(label="Save",command=savefile)
File_menu.add_separator()
File_menu.add_command(label="Exit",command=quit)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)


help_menu  = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About",command=about)
window.mainloop()
