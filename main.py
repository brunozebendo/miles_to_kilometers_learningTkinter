import tkinter

windows = tkinter.Tk()
windows.title("My first GUI program")
windows.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("arial", 24, "bold"))
my_label.pack()









windows.mainloop()