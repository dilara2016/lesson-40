from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")
def topwin():
 top = Toplevel()
 top.geometry("160x100")
 top.title("toplevel")
 l2=Label(top, text = "this  is top level window")
 l2.pack()

 top.mainloop()
l = Label(root, text = "this is root window")
btn=Button(root, text = "Click here to open another window", command = topwin)
l.pack()
btn.pack()
root.mainloop()
