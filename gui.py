#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
#import pandas as pd

import readpdf
import elektroskandia.search
import berner.search
import monitorERP.parser

root= tk.Tk()
root.title("Monitor conversion tool")

#canvas1 = tk.Canvas(root, width = 300, height = 200, relief = 'raised')

var = tk.StringVar(root, "1")

label1 = tk.Label(root, text='Monitor conversion tool')
label1.config(font=('Arial', 15))
label1.pack()

label2 = tk.Label(root, text='')
label2.config(font=('Arial', 10))

#canvas1.create_window(150, 60, window=label1)

def getTxt ():
    import_file_path = filedialog.askopenfilename()
    if(var.get() == "1"):   
        #print(import_file_path)
        readpdf.pdf_to_text(import_file_path)
        elektroskandia.search.run()     #Do the actually parsing will read file in background
        #print("Elektroskandia Parsed!!!")
        label2['text'] = "File parsed correctly! Click save to save parsed file"
    #if(var.get() == "2"):
        #print("Parse Berner")
    if(var.get() == "3"):
        #print("Parse to Elektroskandia")
        monitorERP.parser.run(import_file_path)
        label2['text'] = "File parsed correctly! Click save to save parsed file"
    
def saveParsed():
    if(var.get() == "1"):
        path_to_pref = filedialog.asksaveasfilename(
            defaultextension='.txt', filetypes=[("txt files", '*.txt')],
            #initialdir=self.default_path_to_pref,
            title="Choose filename")
        with open(path_to_pref, 'w') as f:
            str = open('C:/temp/OrderOut.txt')
            for line in str:
                f.write(line)
            f.close()
        #print("File saved!!!")
        label2['text'] = "Redo.."

    if(var.get() == "3"):
        path_to_pref = filedialog.asksaveasfilename(
            defaultextension='.txt', filetypes=[("txt files", '*.txt')],
            #initialdir=self.default_path_to_pref,
            title="Choose filename")
        with open(path_to_pref, 'w') as f:
            str = open('C:/temp/elektroskandiaout.txt')
            for line in str:
                f.write(line)
            f.close()
        #print("File saved!!!")
        label2['text'] = "Redo.."


browseButtonTxt = tk.Button(text="      Import file to parse     ", command=getTxt, bg='green', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(150, 130, window=browseButtonTxt)

def sel():
    global var
    print("You selected the option" + var.get())

R1 = tk.Radiobutton(root, text="Elektroskandia", variable=var, value="1", command=sel)
R1.pack()
R2 = tk.Radiobutton(root, text="Berner", variable=var, value="2", command=sel)
R2.pack()
R3 = tk.Radiobutton(root, text="MonitorToElektroskandia", variable=var, value="3", command=sel)
R3.pack()
browseButtonTxt.pack()
#canvas1.create_window(450, 130, window=canvas2)

saveAsButton = tk.Button(text='Save parsed file', command=saveParsed, bg='green', fg='white', font=('helvetica', 12, 'bold'))
saveAsButton.pack()
#canvas1.create_window(150, 180, window=saveAsButton)

def exitApplication():
    #MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    #if MsgBox == 'yes':
    root.destroy()

exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(150, 230, window=exitButton)
exitButton.pack()

label2.pack()

root.mainloop()

