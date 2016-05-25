from Tkinter import *
import subprocess

master = Tk()

def callback2():
    txt = "I was born exactly 300 years after Galileos death." 

    subprocess.call(["say", txt])

b = Button(master, text="Fact!", command=callback2)
b.pack()

mainloop()
