import math
import tkinter as t
from tkinter import ttk, Frame
from math import *
from PIL import *
import time
import sys
window=t.Tk()
window.title("📚Matrix operator")
window.geometry('390x550')
window.configure(background='pink')
number_order = []
op = ['*','+','-','/']
#canvas=t.Canvas(window,width=800,height=550,bd=0)
#imgpath='hu.gif'
#window.configure(backgroud='pexels-pixabay-289225.jpg')
#img=Image.open(imgpath)
#photo=ImageTK.PhotoImage(img)
#canvas.create_image(700,500,image=photo)
#canvas.pack()
#canvas.create_window(100,50,width=100,height=20,)
text_input_main=t.Text(window,width=41,height=11)
text_input_main.place(x=30,y=30)
text_input_main.insert('insert','|----Matrix Analysis(Version 0.1.1)-----|\n')
text_input_main.insert('insert','|-----[Windows version]-----------------|\n')
text_input_main.insert('insert','|----Input matrix:Matrix Manipulatio----|\n')
text_input_main.insert('insert','|----Input 2matrix:Matrix by Matrix-----|\n')
text_input_main.insert('insert','|----Input exit:Exit system-------------|\n')
text_input_main.insert('insert','|----Input about:About document---------|\n')
text_input_main.insert('insert','|----Input n:Numerical calculation------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
text_input_main.insert('insert','|----Note:Only 3 by 3 Matrix------------|\n')
text_input_main.insert('insert','|---------------------------------------|\n')
button=t.Button(window,text='Exit',command=lambda:window.destroy(),width=4,height=1)
button.place(relx=0,rely=1,anchor='sw')


pos = t.Frame
pos_v = 0
pos2 = t.Frame
pos_v2 = 0
def By():
    global pos,pos_v
    text_input_main.delete(1.0, "end")
    text_input_main.insert('insert', '|---------------------------------------|\n')
    text_input_main.insert('insert', "| For example: [0-9] Click N/C          |\n")
    text_input_main.insert('insert', "|   [1,2,3,4,5,6,7,8,9] Click M/C       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "| Note: Make sure you input format is   |\n")
    text_input_main.insert('insert', "|         correct                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|*************-----BFQM-----************|\n")
    text_input_main.insert('insert', '|---------------------------------------|\n')

    frame=t.Frame(width=330,height=180,bg='#FFFAF0')
    frame.place(x=32,y=280)
    pos = frame
    pos_v = pos_v + 1
    text=t.Text(frame,width=35,height=1)
    text.place(x=25,y=20)
    text.insert("insert","Select you number and input Matrix\n")
    
    text=t.Text(frame,width=35,height=1)
    text.place(x=25,y=150)
    text.insert("insert","Enter quit to exit the panel\n")
    
    select=ttk.Combobox(frame,width=2,textvariable=t.IntVar(),state='readonly')
    lis=[0,1,2,3,4,5,6,7,8,9]
    select['values']=lis
    select.place(x=31,y=50)
    entry=t.Entry(frame,width=14)
    entry.place(x=31,y=90)
    button=t.Button(frame,text='N/C',command=lambda:Select(select),width=4,height=1)
    button.place(x=200,y=50)
    button2=t.Button(frame,text='M/C',command=lambda:Select(entry),width=4,height=1)
    button2.place(x=200,y=90)
    window.mainloop()
def Matrix():
    global pos2,pos_v2
    frame=t.Frame(width=330,height=160,bg='#F8F8FF')
    frame.place(x=32,y=280)
    pos2 = frame
    pos_v2 = pos_v2 + 1
    text=t.Text(frame,width=35,height=1)
    text.place(x=25,y=20)
    text.insert("insert","Note that Enter with commmas(,)\n")
    
    text_input=t.Text(frame,width=9,height=3)
    text_input.place(x=25,y=60)
    text_input2=t.Text(frame,width=9,height=3)
    text_input2.place(x=105,y=60)

    select=ttk.Combobox(frame,width=2,textvariable=t.IntVar(),state='readonly')
    lis=['+','-','*']
    select['values']=lis
    select.place(x=25,y=120)

    text_input_main.delete(1.0, "end")
    text_input_main.insert('insert', '|---------------------------------------|\n')
    text_input_main.insert('insert', "| For example:  Input two matrices      |\n")
    text_input_main.insert('insert', "|         [1,2,3      [1,2,3            |\n")
    text_input_main.insert('insert', "|         4,5,6       4,5,6             |\n")
    text_input_main.insert('insert', "|         7,8,9]      7,8,9]            |\n")
    text_input_main.insert('insert', "|         Select operator [+,-,*]       |\n")
    text_input_main.insert('insert', "|        Ensure proper formatting       |\n")
    text_input_main.insert('insert', "|        Click  M/M/M                   |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|*************-----BFQM-----************|\n")
    text_input_main.insert('insert', '|---------------------------------------|\n')

    button2=t.Button(frame,text='M/M/M',command=lambda:Matrix_by(text_input,text_input2,select),width=7,height=1)
    button2.place(x=230,y=70)
    #button3=t.Button(frame,text='Clear',command=lambda:Clear(text_input,text_input2,select),width=3,height=1)
    #button3.place(x=200,y=70)
def about():
    text_input_main.insert('insert', '|---------------------------------------|\n')
    text_input_main.insert('insert', "|             [About document]          |\n")
    text_input_main.insert('insert', "|This program is based on python tkinter|\n")
    text_input_main.insert('insert', "|library implementation,The initial     |\n")
    text_input_main.insert('insert', "|graphical version 0.1 was implemented  |\n")
    text_input_main.insert('insert', "| in November 2022, thanks to those     |\n")
    text_input_main.insert('insert', "| who used the program to help          |\n")
    text_input_main.insert('insert', "| with linear algebra learning.         |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|*************-----about-----***********|\n")
    text_input_main.insert('insert', '|---------------------------------------|\n')


pos3 = t.Frame
pos3_v = 0
def number():
    global pos3_v,pos3
    text_input_main.delete(1.0, "end")
    text_input_main.insert('insert', '|---------------------------------------|\n')
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|         [Numerical calculation]       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|                                       |\n")
    text_input_main.insert('insert', "|*************---N mode---**************|\n")
    text_input_main.insert('insert', '|---------------------------------------|\n')

    frame = t.Frame(width=330, height=225, bg='#F8F8FF')
    frame.place(x=32, y=300)
    pos3 = frame
    pos3_v = pos3_v +1
    button1 = t.Button(frame, text='1', command=lambda: number_by(1), width=5,height=1)
    button1.place(x=20, y=20)
    button2 = t.Button(frame, text='2', command=lambda: number_by(2), width=5, height=1)
    button2.place(x=80, y=20)
    button3 = t.Button(frame, text='3', command=lambda: number_by(3), width=5, height=1)
    button3.place(x=140, y=20)
    button_p = t.Button(frame, text='+', command=lambda: opsys('+'), width=5, height=1)
    button_p.place(x=200, y=20)
    button_d = t.Button(frame, text='/', command=lambda: opsys('/'), width=5, height=1)
    button_d.place(x=260, y=20)

    button4 = t.Button(frame, text='4', command=lambda: number_by(4), width=5, height=1)
    button4.place(x=20, y=80)
    button5 = t.Button(frame, text='5', command=lambda: number_by(5), width=5, height=1)
    button5.place(x=80, y=80)
    button6 = t.Button(frame, text='6', command=lambda: number_by(6), width=5, height=1)
    button6.place(x=140, y=80)
    button_s = t.Button(frame, text='-', command=lambda: opsys('-'), width=5, height=1)
    button_s.place(x=200, y=80)
    button_q = t.Button(frame, text='=', command=lambda: opsysc(), width=5, height=1)
    button_q.place(x=260, y=80)

    button7 = t.Button(frame, text='7', command=lambda: number_by(7), width=5, height=1)
    button7.place(x=20, y=140)
    button8 = t.Button(frame, text='8', command=lambda: number_by(8), width=5, height=1)
    button8.place(x=80, y=140)
    button9 = t.Button(frame, text='9', command=lambda: number_by(9), width=5, height=1)
    button9.place(x=140, y=140)
    button_t = t.Button(frame, text='*', command=lambda: opsys('*'), width=5, height=1)
    button_t.place(x=200, y=140)
    button_e = t.Button(frame, text='Emp', command=lambda: opdel(), width=5, height=1)
    button_e.place(x=260, y=140)

    button_f = t.Button(frame, text='.', command=lambda: number_by('.'), width=5, height=1)
    button_f.place(x=20, y=180)
    button_pcent = t.Button(frame, text='%', command=lambda: Precent(), width=5, height=1)
    button_pcent.place(x=80, y=180)
    button_pcent = t.Button(frame, text='X*2', command=lambda: Times(), width=5, height=1)
    button_pcent.place(x=140, y=180)

cont = 0
def Times():
    i = (text_input_main.get(0.0, 'end')).split('\n')
    for j in i:
        j = j.split(' ')
        number_order.append(j[0])
    print(number_order)
    if (len(number_order) < 1) or (number_order[0] in op):
        text_input_main.delete(1.0, "end")
        text_input_main.insert('insert', 'No value ! Error ! \n')
    ans = math.pow(int(number_order[0]),2)
    text_input_main.insert('insert', '\nans' + ' = ' + str(ans))
def Precent():
    i = (text_input_main.get(0.0, 'end')).split('\n')
    for j in i:
        j = j.split(' ')
        number_order.append(j[0])
    print(number_order)
    if (len(number_order) == 0) or (number_order[0] in op):
        text_input_main.delete(1.0, "end")
        text_input_main.insert('insert', 'No value ! Error ! \n')

    ans = eval(number_order[0]) * 0.01
    #text_input_main.delete(1.0, "end")
    text_input_main.insert('insert', '\nans' + ' = ' + str(ans))
    ...
def number_by(number_input):
    global cont
    cont = cont + 1
    if cont == 1:
        text_input_main.delete(1.0, "end")
    text_input_main.insert('insert', str(number_input))

    ...
def opdel():
    text_input_main.delete(1.0, "end")
    number_order.clear()
def opsys(charer):
    text_input_main.insert('insert', ' ' + charer + ' ')

def opsysc():
    i = (text_input_main.get(0.0, 'end')).split('\n')
    for j in i:
        if len(j.split(' ')) != 0:
            j = j.split(' ')
            for k in range(len(j)):
                if j[k] != ' ':
                    number_order.append(j[k])
    number_order.remove(number_order[len(number_order) - 1])
    if (number_order[len(number_order) - 1] in op) or (number_order[0] in op):
        text_input_main.delete(1.0, "end")
        text_input_main.insert('insert', ' Incorrect input format! ')
        return 0
    ans = 0
    print(number_order)

    frist = search_number_op()
    if frist != 0:
        number_c_frist(frist)
        if len(number_order) == 1:
            ans = number_order[0]
        else:
            ans = number_c_nomel()
    else:
        ans = number_c_nomel()
    text_input_main.insert('insert', '\nans' + ' = ' + str(ans))

    text_input_main.insert('insert', '\n\n\n\n\n\n\nInside: ' + str(number_order))

def number_c_frist(n):
    ans = 0
    print(str(n) + 'p')
    while (n != 0):
        if number_order[n] == '*':
            if ans == 0:
                ans = eval(number_order[n - 1]) * eval(number_order[n + 1])
                number_order.remove(number_order[n])
                number_order.remove(number_order[n])
                number_order.remove(number_order[n - 1])
            number_order.insert(n,str(ans))
        elif number_order[n] == '/':
            if ans == 0:
                ans = eval(number_order[n - 1]) / eval(number_order[n + 1])
                number_order.remove(number_order[n])
                number_order.remove(number_order[n])
                number_order.remove(number_order[n - 1])
            number_order.insert(n,str(ans))

        if number_order[0] in op:
            a = number_order[0]
            number_order[0] = number_order[1]
            number_order[1] = a
        #print(number_order)
        n = search_number_op()
        ans = 0
        #print(str(n) + 'k')


def number_c_nomel():
    ans = 0
    for z in range(len(number_order) - 1):
        if number_order[z] == '+':
            if ans == 0:
                #print(eval(number_order[z - 1]),eval(number_order[z + 1]))
                ans = number_c(eval(number_order[z - 1]),eval(number_order[z + 1]),number_order[z])
            else:
                ans = ans + eval(number_order[z + 1])
        elif number_order[z] == '-':
            if ans == 0:
                ans = number_c(eval(number_order[z - 1]),eval(number_order[z + 1]),number_order[z])
            else:
                ans = ans - eval(number_order[z + 1])
        elif number_order[z] == '/':
            if ans == 0:
                ans = number_c(eval(number_order[z - 1]),eval(number_order[z + 1]),number_order[z])
            else:
                ans = ans / eval(number_order[z + 1])
        elif number_order[z] == '*':
            if ans == 0:
                ans = number_c(eval(number_order[z - 1]), eval(number_order[z + 1]), number_order[z])
            else:
                ans = ans * eval(number_order[z + 1])
    return ans

def search_number_op():
    for i in range(len(number_order) - 1):
        if (number_order[i] == '*') or (number_order[i] == '/'):
            return i
    return 0
def number_c(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    else:
        return a * b

def Clear(x,y,z):
    if x and y and z:
        #text_input.delete(1.0,"end")
        #text_input2.delete(1.0,"end")
        return 'ok'
    
def Valid(x,y):
    if x!=y:
        return False
    return True

def Result(n,m):
    v=[]
    Time=0
    Space=0
    k=0
    i=0
    j=0
    ci=1
    while True:
        s=For(m,Time,Space)
        k+=int(n[i][j])*int(s)
        j+=1
        Space+=1
        if Space>2:
            v.append(k)
            ci+=1
            j=0
            i=0
            Time+=1
            Space=0
            k=0
        if ci>3:
            break
            
        if i==2 and Time==2:
            break
    return v
def Result_2(n,m):
    v=[]
    Time=0
    Space=0
    k=0
    i=1
    j=0
    ci=1
    while True:
        s=For(m,Time,Space)
        k+=int(n[i][j])*int(s)
        j+=1
        Space+=1
        if Space>2:
            v.append(k)
            ci+=1
            j=0
            i=1
            Time+=1
            Space=0
            k=0
        if ci>3:
            break
            
        if i==2 and Time==2:
            break
    return v

def Result_3(n,m):
    v=[]
    Time=0
    Space=0
    k=0
    i=2
    j=0
    ci=1
    while True:
        s=For(m,Time,Space)
        k+=int(n[i][j])*int(s)
        j+=1
        Space+=1
        if Space>2:
            v.append(k)
            ci+=1
            j=0
            i=2
            Time+=1
            Space=0
            k=0
        if ci>3:
            break
    return v

def Fun(get,get2):
    result=Result(get,get2)
    result2=Result_2(get,get2)
    result3=Result_3(get,get2)
    return (result,result2,result3)
    
def For(m,time,space):
    Time=time #元素索引
    row=space #行数
    for i in range(len(m[row])):
        return m[row][Time]

def Shellfe(k):
    a=[]
    b=[]
    c=[]
    gross=[]
    for j in range(len(k)):
        if len(a)!=3:
            a.append(k[j])
        elif len(b)!=3 and j>2:
            b.append(k[j])
        elif len(c)!=3 and j>5:
            c.append(k[j])
    gross=[a,b,c]
    return gross

def Fun2(x,y,n):
    z=[]
    if str(n)=='-':
        for i in range(len(x)):
            z.append(int(x[i])-int(y[i]))
    else:
        for j in range(len(x)):
            z.append(int(x[j])+int(y[j]))
    return z
            
            

def Matrix_by(x,y,z):
    text_x=[]
    text_y=[]
    X=(x.get(0.0,'end').replace(" ","")).split('\n')
    X.pop()
    for i in X:
        d=i.split(',')
        for j in d:
            text_x.append(j)
            
    Y=(y.get(0.0,'end').replace(" ","")).split('\n')
    Y.pop()
    for h in Y:
        o=h.split(',')
        for a in o:
            text_y.append(a)
    print(text_x)
    print(text_y)
            
    b=0
    if Valid(len(text_x),len(text_y)) and str(z.get())=='*':
        n=Shellfe(text_x)
        m=Shellfe(text_y)
        Re=Fun(n,m)
        text_input_main.delete(1.0,"end")
        for n in range(len(Re)):
            text_input_main.insert('insert',str(Re[n])+'\n')
        text_x.clear()
        text_y.clear()
    else:
        print('Valid')
    if Valid(len(text_x),len(text_y)) and str(z.get())!='*':
        Rt=Fun2(text_x,text_y,z.get())
        print(Rt)
        text_input_main.delete(1.0,"end")
        if len(Rt)==9:
            b=len(Rt)/3
        if len(Rt)==4:
            b=len(Rt)/2
        for i in range(len(Rt)):
            if i==b or i/3==2:
                text_input_main.insert('insert','\n')
            text_input_main.insert('insert',str(Rt[i]))
            text_input_main.insert('insert',' ')
        text_x.clear()
        text_y.clear()
    else:
        print('Valid')

Number=0
def Select(self):
    re=[]
    R=[]
    r=0
    v=[]
    n=0
    flag=False
    
    try:
        if len(self.get())==1:
            global Number
            Number=self.get()
        if len(self.get())>2:
            if str(self.get())=='quit':
                return 'quit'
            k=self.get().split(',')
            for i in k:
                v.append(int(i))
            print(v)
            if len(v)==9:
                n=len(v)/3
                flag=True
            if len(v)==4:
                n=len(v)/2
                flag=True
            text_input_main.delete(1.0,"end")
            for i in range(len(v)):
                if (i==n or i/3==2) and flag==True:
                    text_input_main.insert('insert','\n')
                text_input_main.insert('insert',int(v[i])*int(Number))
                text_input_main.insert('insert',' ')
            return 'pass'
    except:
        text_input_main.delete(1.0,"end")
        text_input_main.insert('insert','Input-error\n')

def pos_var(pos):
    if pos == 1:
        return True
    return False
def pos_var_dob(pos1,pos2):
    if pos1 == 1 or pos2 == 1:
        return True
    return False
def main(self):
    global pos_v,pos2,pos_v2,pos,pos3,pos3_v
    if str(self.get())=='matrix':
        text_input_main.delete(1.0,"end")
        if pos_var(pos_v2):
            pos2.destroy()
            pos_v2 = 0
        if pos3_v == 1:
            pos3_v = 0
            pos3.destroy()
        By()
    elif str(self.get())=='2matrix':
        text_input_main.delete(1.0,"end")
        if pos_var(pos_v):
            pos.destroy()
            pos_v = 0
        if pos3_v == 1:
            pos3_v = 0
            pos3.destroy()
        Matrix()
    elif str(self.get())=='exit':
        window.destroy()
    elif str(self.get())=='n':
        if pos_var_dob(pos_v,pos_v2):
            pos_v = 0
            pos_v2 = 0
            pos.destroy()
            pos2.destroy()
        number()
    elif str(self.get())=='about':
        text_input_main.delete(1.0, "end")
        about()
    else:
        text_input_main.delete(1.0,"end")
        text_input_main.insert('insert', '|---------------------------------------|\n')
        text_input_main.insert('insert', "|             [Error infor]             |\n")
        text_input_main.insert('insert', "|                                       |\n")
        text_input_main.insert('insert', "|                                       |\n")
        text_input_main.insert('insert', "|   [The command line does not exist]   |\n")
        text_input_main.insert('insert', "|                                       |\n")
        text_input_main.insert('insert', "|                                       |\n")
        text_input_main.insert('insert', "|                                       |\n")
        text_input_main.insert('insert', "|                                       |\n")
        text_input_main.insert('insert', "|*************-----error-----***********|\n")
        text_input_main.insert('insert', '|---------------------------------------|\n')
        
        
    

entry=t.Entry(window,width=20)
entry.place(x=40,y=230)
button=t.Button(window,text='Choose',command=lambda:main(entry),width=6,height=1)
button.place(x=280,y=230)
window.mainloop()
    
