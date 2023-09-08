from tkinter import *
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    Text_Input.set(operator)
def btnClear():
    global operator
    operator=""
    Text_Input.set("")
def btnEquals():
    global operator
    result=str(eval(operator))
    Text_Input.set(result)    
cal=Tk()
cal.title("Calculator")
operator=""
Text_Input=StringVar()
txtDisplay=Entry(cal,width=30,font=('arial',20,'bold'),textvariable=Text_Input,bd=30,insertwidth=4,bg='aqua',justify='right').grid(columnspan=4)
bt7=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7), bg="silver").grid(row=1,column=0)
bt8=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8),bg="silver").grid(row=1,column=1)
bt9=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9),bg="silver").grid(row=1,column=2)
btDe=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/"),bg="silver").grid(row=1,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------
bt4=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4),bg="pink").grid(row=2,column=0)
bt5=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5),bg="pink").grid(row=2,column=1)
bt6=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6),bg="pink").grid(row=2,column=2)
btMu=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*"),bg="pink").grid(row=2,column=3)
#----------------------------------------------------------------------------------------------------------------------------------------------
bt1=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1),bg="blue").grid(row=3,column=0)
bt2=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2),bg="blue").grid(row=3,column=1)
bt3=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3),bg="blue").grid(row=3,column=2)
btSub=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-"),bg="blue").grid(row=3,column=3)
#----------------------------------------------------------------------------------------------------------------------------------------------
btClear=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=btnClear,bg="yellow").grid(row=4,column=0)
btdo=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text=".",command=lambda:btnClick("."),bg="yellow").grid(row=4,column=1)
bt0=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0),bg="yellow").grid(row=4,column=2)
btAdd=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+"),bg="yellow").grid(row=4,column=3)
#----------------------------------------------------------------------------------------------------------------------------------------------
btop=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="(",command=lambda:btnClick("("),bg="green").grid(row=5,column=0)
btcl=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text=")",command=lambda:btnClick(")"),bg="green").grid(row=5,column=1)
btEquals=Button(cal,padx=95,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=btnEquals,bg="green").grid(row=5,column=2,columnspan=2)

#----------------------------------------------------------------------------------------------------------------------------------------------

cal.mainloop()
