from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as tkmb
root=Tk()
root.title("country flag")
root.geometry("600x400")

input_name=Entry(root)
label1=Label(root)
input_name.place(relx=0.5,rely=0.2,anchor=CENTER)
label1.place(relx=0.5,rely=0.6,anchor=CENTER)

india=ImageTk.PhotoImage(Image.open("ind.jpg"))
australia=ImageTk.PhotoImage(Image.open("aus.png"))
kenya=ImageTk.PhotoImage(Image.open("kenya.png"))
malaysia=ImageTk.PhotoImage(Image.open("malaysia.png"))
japan=ImageTk.PhotoImage(Image.open("japan.jpg"))

map_dictionary={   
"malay":malaysia,
"ken":kenya}

def country_flag():
    
        country_name=input_name.get()
        print(country_name)
        label1["image"]=map_dictionary[country_name]
        tkmb.showinfo("error","sorry this country flag is not present in our system")
    


btn=Button(root,text="show country flag",command=country_flag)
btn.place(relx=0.5,rely=0.33,anchor=CENTER)
root.mainloop()
