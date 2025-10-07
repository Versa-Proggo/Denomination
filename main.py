from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
root = Tk()
root.title("Denomination Counter")
root.geometry("650x400")
upload = Image.open("assets\image.png")
image = ImageTk,PhotoImage(upload)
label = Label(root,image=image, bg = "light blue")
label.place(x=180, y=20)
label1 = Label(root,text = "Hey Welcome to me DEVIL SATAN Lucifer SHAYTAN ",bg = "Light blue")
def msg():
    Msgbox = messagebox.showinfo("Alert" , "Do you wanna calculate the denomination count?")
    if Msgbox == "ok":
        topwin()
button1 = Button(root,text = "Lets get started!", command=msg, bg = "brown", fg = "white")
button1.place(x = 20, y = 360)
def topwin():
    top = Toplevel()
    top.title("DEnomInAtIoN cAlCuLaToR")
    top.configure(bg = "light grey")
    top.geometry("600x450")
    label = Label(top, Text = "Enter total amount", bg = "light grey")
    entry = Entry(top)
    lbl = Label(top,text="WDegfkjgfjkwr0", bg = "light grey")
    l1 = Label(top,text = "2000" bg = "lightyellow")
    l2 = Label(top,text = "500" bg = "light yellow")
    l3 = Label(top,text = "100" bg = "light yellow")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            global amount