#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#Import the different modules
import readpdf
import elektroskandia.search
import berner.search
import monitorERP.parser

import ospath
intpath = ospath.ospath()

def saveParsed():
    if(var.get() == "1"):
        path_to_pref = filedialog.asksaveasfilename(
            defaultextension='.txt', filetypes=[("txt files", '*.txt')],
            #initialdir=self.default_path_to_pref,
            title="Choose filename")
        with open(path_to_pref, 'w') as f:
            str = open(intpath.getPath() + 'OrderOut.txt')
            for line in str:
                f.write(line)
            f.close()
        #print("File saved!!!")
        labelrun['text'] = "Redo.."

    if(var.get() == "3"):
        path_to_pref = filedialog.asksaveasfilename(
            defaultextension='.txt', filetypes=[("txt files", '*.txt')],
            #initialdir=self.default_path_to_pref,
            title="Choose filename")
        with open(path_to_pref, 'w') as f:
            str = open(intpath.getPath() + 'elektroskandiaout.txt')
            for line in str:
                f.write(line)
            f.close()
        #print("File saved!!!")
        labelrun['text'] = "Redo.."

    if(var.get() == "4"):
        path_to_pref = filedialog.asksaveasfilename(
            defaultextension='.txt', filetypes=[("txt files", '*.txt')],
            #initialdir=self.default_path_to_pref,
            title="Choose filename")
        with open(path_to_pref, 'w') as f:
            str = open(intpath.getPath() + 'elfaout.txt')
            for line in str:
                f.write(line)
            f.close()
        #print("File saved!!!")
        labelrun['text'] = "Redo.."

def getTxt ():
    import_file_path = filedialog.askopenfilename()
    if(var.get() == "1"):   
        #print(import_file_path)
        readpdf.pdf_to_text(import_file_path)
        elektroskandia.search.run()     #Do the actually parsing will read file in background
        #print("Elektroskandia Parsed!!!")
        labelrun['text'] = "File parsed correctly! Click save to save parsed file"
        saveParsed()

    if(var.get() == "2"):
        print("Parse Berner")

    if(var.get() == "3") or (var.get() == "4"):
        monitorERP.parser.run(import_file_path)
        labelrun['text'] = "File parsed correctly! Click save to save parsed file"
        saveParsed()
    
#Draw the gui


root= tk.Tk()
root.title("Monitor konverterings verktyg")
#root.pack(fill=BOTH, expand=1)

var = tk.StringVar(root, "1")

labelrun = tk.Label(root, text='')
labelrun.config(font=('Arial', 10))

#label1 = tk.Label(root, text='Monitor conversion tool')
#label1.config(font=('Arial', 15))
#label1.pack()

#label2 = tk.Label(root, text='')
#label2.config(font=('Arial', 10))

canvas1 = tk.Canvas(root, width = 300, height = 20, relief = 'raised')
canvas1.create_line(1, 10, 300, 10)
canvas1.pack()

canvas3 = tk.Canvas(root, width = 300, height = 200, relief = 'raised')
label2 = tk.Label(canvas3, text='Ordererkännande till monitor')
label2.config(font=('Arial', 15))
label2.pack()

R1order = tk.Radiobutton(canvas3, text="Elektroskandia", variable=var, value="1")
R1order.pack(anchor=tk.W)
R2order = tk.Radiobutton(canvas3, text="Berner (ej klar)", variable=var, value="2")
R2order.pack(anchor=tk.W)

canvas3.pack()

canvas5 = tk.Canvas(root, width = 300, height = 20, relief = 'raised')
canvas5.create_line(1, 10, 300, 10)
canvas5.pack()

canvas4 = tk.Canvas(root, width = 300, height = 200, relief = 'raised')
label2 = tk.Label(canvas4, text='Beställning webshop')
label2.config(font=('Arial', 15))
label2.pack()
R3best = tk.Radiobutton(canvas4, text="Elektroskandia", variable=var, value="3")
R3best.pack(anchor=tk.W)
R4best = tk.Radiobutton(canvas4, text="Elfa", variable=var, value="4")
R4best.pack(anchor=tk.W)
canvas4.pack()

#browseButtonTxt.pack()

#canvas1.create_window(450, 130, window=canvas2)

#saveAsButton = tk.Button(text='Save parsed file', command=saveParsed, bg='green', fg='white', font=('helvetica', 12, 'bold'))
#saveAsButton.pack()
#canvas1.create_window(150, 180, window=saveAsButton)

def exitApplication():
    root.destroy()

canvas7 = tk.Canvas(root, width = 300, height = 20, relief = 'raised')
canvas7.create_line(1, 10, 300, 10)
canvas7.pack()

canvas2 = tk.Canvas(root, width = 300, height = 200, relief = 'raised')
browseButtonTxt = tk.Button(canvas2, text="Välj fil", command=getTxt, bg='green', fg='white', font=('helvetica', 12, 'bold'))
browseButtonTxt.pack()
canvas2.pack()

canvas8 = tk.Canvas(root, width = 300, height = 20, relief = 'raised')
canvas8.create_line(1, 10, 300, 10)
canvas8.pack()

canvas6 = tk.Canvas(root, width = 300, height = 500, relief = 'raised')
exitButton = tk.Button (canvas6, text='Avsluta',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
exitButton.pack()
canvas6.pack()

labelrun.pack()


root.mainloop()

