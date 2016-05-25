from Tkinter import *
import subprocess

master = Tk()

def callback():
    txt = "My name is Stephen Hawking, and I was born in Oxford, UK on January 8th, 1942. I was diagnosed with ALS, a paralysing disease, at age 21. I am known for my theories on black holes, and my writing. ALS does not allow me to talk, so I talk through a computer."

    subprocess.call(["say", txt])

b = Button(master, text=“Click me to learn more!”, command=callback)
b.pack()

mainloop()


master = Tk()

def callback2():
    txt = “I was born exactly 300 years after Galileo’s death.” 

    subprocess.call(["say", txt])

b = Button(master, text=“Fact!”, command=callback2)
b.pack()

mainloop()