from email.mime import text
from tkinter import*

root=Tk()
root.title("Chat box")
lable=Label(text="My New GUI App!",fg="blue",font="top")
lable.pack
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
        t.insert(END,"\n"+"Sorry i didnt get you")
    e.delete(0,END)       
t=Text(root)
t.grid(row=0,column=0,columnspan=2)
e=Entry(width=150,bg="spring green",fg="black")
send=Button(root,text="Send",fg="red",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.mainloop()


