from email.mime import text
from tkinter import*
from tkinter import font
from turtle import right

root=Tk()
root.title("Chat box")
lable=Label(text="My New GUI App!",fg="black",bg="aqua",font=("Arial Bold Italic",25))
lable.pack(side="top")
def send():
    send="You ->"+e.get()
    t.insert(END,"\n"+send)
    if (e.get()=="Hello"or e.get()=="hello" or e.get()=="Hi" or e.get()=="hi"):
        t.insert(END,"\n"+"Me -> Hi")
    elif(e.get()=="How are you?"or e.get()=="how are you?"or e.get()=="HOW ARE YOU?"):
        t.insert(END,"\n"+"Me -> I am Fine")
    elif(e.get()=="What are you doing in studies ?"or e.get()== "what are you doing in studies?"or e.get()== "what are you doing"):    
        t.insert(END,"\n"+"Me -> I am doing Softwer Engineering")    
    elif (e.get()=="Now what do you want to do in future"):
        t.insert(END,"\n"+"I want to become a frontend devoloper" )    
    else:
        t.insert(END,"\n"+"Sorry i didn't get you")
    e.delete(0,END)       
t=Text(root,bg="grey")
t.pack(padx=60,pady=20)
e=Entry(width=150,bg="spring green",fg="black",relief="raised")
send=Button(root,text="Send",fg="red",command=send).pack(side="right")

e.pack()
root.mainloop()

