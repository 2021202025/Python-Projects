from tkinter import *

window = Tk()

def miles_to_kms():
    print(e2_value.get())
    t1.delete('1.0', END)
    t1.insert(END, str(float(e2_value.get())*1.545) + " Kms" )
    t2.delete('1.0', END)
    t2.insert(END, str(float(e2_value.get())*0.868976) + " Knots")

e1=Label(window,text="Miles")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0,column=1)

b1= Button(window, text="Convert", command=miles_to_kms)
b1.grid(row=0, column=2)

l1 = Label(window,text="Equivalent to")
l1.grid(row=1, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=2, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()
