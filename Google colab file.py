# -*- coding: utf-8 -*-
"""Anurag workshop.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B_S5lhw7OkdUBLWi1nJ5Gy8YcOO6a3v6
"""

from tkinter import *

root=Tk()
root.geometry("1280x720")
root.mainloop()

root=Tk()
root.geometry("750x250+350+400")
root.mainloop()

root=Tk()
root.attributes('-fullscreen' ,True)
root.mainloop()

root=Tk()
root.geometry("450x450")
root.title("Calculator in progress")
root.mainloop()

root=Tk()
root.geometry("450x450")
root.title("preet kalra")
mylabel=Label(root,text="Ice cream")
mylabel.pack(pady=10)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("Label edit")
mylabel=Label(root,text="ice cream",foreground='blue',background='pink')
mylabel.pack(pady=30)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("Boom")
mylabel1=Label(root,text="Good morning",foreground='white',background='red')
mylabel2=Label(root,text="Good Night",background='lightblue')
mylabel1.pack(pady=40)
mylabel2.pack(pady=100)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("BOOM")
mylabel1=Label(root,text="Hello world",background='pink')
mylabel2=Label(root,text="Hi World",background='orange')
mylabel1.grid(row=2,column=0)
mylabel2.grid(row=0,column=1)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("BOOM")
mylabel1=Label(root,text="Hello world",background='pink')
mylabel2=Label(root,text="Hi World",background='orange')
mylabel3=Label(root,text="Hello world2",background='green')
mylabel4=Label(root,text="Hello world5",background='orange')
mylabel1.grid(row=2,column=0)
mylabel2.grid(row=0,column=1)
mylabel3.grid(row=5,column=3)
mylabel4.grid(row=3,column=4)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("Button")
mybutton=Button(root,text='Click me',padx=3,pady=50,state=DISABLED)
mybutton.pack(pady=40)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("Button")
mybutton=Button(root,text="Click ME",padx=50)
mybutton.pack(pady=40)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("Even Triggering button")
def click():
    mylabel=Label(root,text='Hello',fg="white",bg="black",pady=30,font=30)
    mylabel.pack()
mybutton=Button(root,text='Click me',command=click,padx=50)
mybutton.pack(pady=50)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("counter Button")
counter=0
def click():
    global counter
    global mylabel
    counter=counter+1
    mylabel.configure(text=f'you clicked {counter} times')
mylabel=Label(root,text='no click',fg="white",bg="black",pady=30,font=30)
mylabel.pack()
mybutton=Button(root,text='Click me',command=click,padx=50,font=40)
mybutton.pack(pady=50)
root.mainloop()

root=Tk()
root.geometry("500x500")
root.title("counter Button")
counter=0
def click():
    global counter
    global mylabel
    counter=counter+1
    mylabel.configure(text=f'you clicked {counter} times')
    if counter>10:
        mybutton.configure(state=DISABLED)
        mylabel.configure(text="NO STOP IT")

mylabel=Label(root,text='no click',fg="white",bg="black",pady=30,font=30)
mylabel.pack()
mybutton=Button(root,text='Click me',command=click,padx=50,font=40)
mybutton.pack(pady=50)
root.mainloop()

from tkinter import *

root=Tk()
root.title("Calculator")
mainframe=Frame(root,width=45,height=30,bd=10,relief=RIDGE,bg="Black")
mainframe.pack()
inner=Frame(mainframe,width=45,bd=10,relief=SUNKEN,bg="red")
inner.pack()
e=Entry(inner,width=60,borderwidth=0)
e.grid(row=0,column=0,columnspan=10,padx=10,pady=8)
def onclick(num):
    x=e.get()
    e.delete(0,END)
    e.insert(0,str(x)+str(num))

def clear():
    e.delete(0,END)

def add():
    global first,op
    op='+'
    first=e.get()
    e.delete(0,END)

def sub():
    global first,op
    op='-'
    first=e.get()
    e.delete(0,END)

def mul():
    global first,op
    op='*'
    first=e.get()
    e.delete(0,END)

def div():
    global first,op
    op='/'
    first=e.get()
    e.delete(0,END)

def equal():
    second=e.get()
    if op=='+':
        result=float(first)+float(second)
    elif op=='-':
        result=float(first)-float(second)
    elif op=='*':
        result=float(first)*float(second)
    elif op=='/':
        result=float(first)/float(second)
    e.delete(0,END)
    e.insert(0,result)


button_1=Button(inner,text='1',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(1))
button_2=Button(inner,text='2',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(2))
button_3=Button(inner,text='3',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(3))
button_4=Button(inner,text='4',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(4))
button_5=Button(inner,text='5',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(5))
button_6=Button(inner,text='6',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(6))
button_7=Button(inner,text='7',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(7))
button_8=Button(inner,text='8',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(8))
button_9=Button(inner,text='9',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(9))
button_0=Button(inner,text='0',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(0))

button_add=Button(inner,text='+',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=add)
button_sub=Button(inner,text='-',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=sub)
button_mul=Button(inner,text='*',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=mul)
button_div=Button(inner,text='/',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=div)
button_equal=Button(inner,text='=',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=equal)
button_clear=Button(inner,text='C',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=1)
root.mainloop()

from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Student registration Form")
window.geometry("500x500")
window.configure(background = "black")
a = Label(window ,text = "First Name").grid(row=0,column=0)
b = Label(window ,text = "Last Name").grid(row=1,column=0)
c = Label(window ,text = "Email").grid(row=2,column=0)
d = Label(window ,text = "Gender").grid(row=3,column=0)
e = Label(window ,text = "Phone no.").grid(row=4,column=0)
a1 = Entry(window).grid(row=0,column=1)
b1 = Entry(window).grid(row=1,column=1)
c1 = Entry(window).grid(row=2,column=1)
d1 = Entry(window).grid(row=3,column=1)
e1 = Entry(window).grid(row=4,column=1)

def clicked():
    res ="Welcome to" + txt.get()
    lbl.configure(text= res)
btn=ttk.Button(window ,text="Submit").grid(row=10,column=0)
window.mainloop()

root=Tk()
root.geometry("750x550")
root.title("Text widget (textbox)")
txt=Text(root)
txt.configure(bg='Skyblue',height=2)
txt.pack()
txt.insert('1.0',"Enter your Data")
name=''
def submit():
    global name
    name=txt.get("1.0","1.3")#line.column
    mylabel=Label(root,text=name,width=120)
    mylabel.pack()
    txt.delete('1.0','1.3')
button=Button(root,text='submit',command=submit)
button.pack()
root.mainloop()

root=Tk()
root.geometry("750x250")
myframe=LabelFrame(root,text='MY frame',padx=5,pady=5)
myframe.pack(padx=140,pady=10)

mylabel=Label(myframe,text="Label")
mylabel.pack()

mybutton=Button(myframe,text="Button")
mybutton.pack()
root.mainloop()

import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window=tk.Tk()
window.title('Claculator')
frame=tk.Frame(master=window,bg="skyblue",padx=10)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30)
entry.grid(row=0,column=0,columnspan=3,ipady=2,pady=2)

def myclick(number):
    entry.insert(tk.END,number)

def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")

def clear():
    entry.delete(0,tk.END)

button_1=tk.Button(master=frame,text='1',padx=15,pady=5,width=3,command=lambda:myclick(1))
button_1.grid(row=1,column=0,pady=2)
button_2=tk.Button(master=frame,text='2',padx=15,pady=5,width=3,command=lambda:myclick(2))
button_2.grid(row=1,column=1,pady=2)
button_3=tk.Button(master=frame,text='3',padx=15,pady=5,width=3,command=lambda:myclick(3))
button_3.grid(row=1,column=2,pady=2)
button_4=tk.Button(master=frame,text='4',padx=15,pady=5,width=3,command=lambda:myclick(4))
button_4.grid(row=2,column=0,pady=2)
button_5=tk.Button(master=frame,text='5',padx=15,pady=5,width=3,command=lambda:myclick(5))
button_5.grid(row=2,column=1,pady=2)
button_6=tk.Button(master=frame,text='6',padx=15,pady=5,width=3,command=lambda:myclick(6))
button_6.grid(row=2,column=2,pady=2)
button_7=tk.Button(master=frame,text='7',padx=15,pady=5,width=3,command=lambda:myclick(7))
button_7.grid(row=3,column=0,pady=2)
button_8=tk.Button(master=frame,text='8',padx=15,pady=5,width=3,command=lambda:myclick(8))
button_8.grid(row=3,column=1,pady=2)
button_9=tk.Button(master=frame,text='9',padx=15,pady=5,width=3,command=lambda:myclick(9))
button_9.grid(row=3,column=2,pady=2)
button_0=tk.Button(master=frame,text='0',padx=15,pady=5,width=3,command=lambda:myclick(0))
button_0.grid(row=4,column=1,pady=2)

button_add=tk.Button(master=frame,text="+",padx=15,pady=5,width=3,command=lambda:myclick('+'))
button_add.grid(row=5,column=0,pady=2)

button_subtract=tk.Button(master=frame,text="-",padx=15,pady=5,width=3,command=lambda:myclick('-'))
button_subtract.grid(row=5,column=1,pady=2)

button_multiply=tk.Button(master=frame,text="*",padx=15,pady=5,width=3,command=lambda:myclick('*'))
button_multiply.grid(row=5,column=2,pady=2)

button_div=tk.Button(master=frame,text="/",padx=15,pady=5,width=3,command=lambda:myclick('/'))
button_div.grid(row=6,column=0,pady=2)

button_clear=tk.Button(master=frame,text="clear",padx=15,pady=5,width=12,command=clear)
button_clear.grid(row=6,column=1,columnspan=2,pady=2)

button_equal=tk.Button(master=frame,text="=",padx=15,pady=5,width=9,command=equal)
button_equal.grid(row=7,column=0,columnspan=3,pady=2)

window.mainloop()

a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
import time
start=time.time()
for i in range (len(a)):
c.append(a[i]+b[i])
print(time.time()-start)

a=np.arange(10000000)
b=np.arange(10000000,20000000)
c=a+b
import numpy as np
start=time.time()
print(time.time()-start)

3.77/0.11

a = [i for i in range(100000)]
import sys
sys.getsizeof(a)

a= np.arange(100000,dtype=np.int16)
sys.getsizeof(a)

import numpy as np
a=np.array([1,2,3])
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

np.array([1,2,3],dtype=float)

np.arange(1,995,5)

a=np.arange(9).reshape(3,3)
print(a)
np.arange(30).reshape(2,5,3)

np.ones((3,4))

np.zeros((5,5))

np.zeros((99,99))

np.random.random((3,4))

np.random.random((3,4))

np.linspace(-50,50,21,dtype=int)

np.identity(9)

a1 = np.arange(10,dtype=np.int64)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(12,dtype=np.int32).reshape(2,2,3)
a3

a3.ndim

print(a2.shape)
a3

print(a3.size)

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

a4=a3.astype(np.int32)
a4.dtype

a1**2

a3**3

a3==4

a1 = np.arange(16,dtype=float).reshape(4,4)
a2 = np.arange(16,dtype=float).reshape(4,4)
a1

a1+a2

a1=np.random.random((3,3))
a1=np.round(a1*69)
a1

np.max(a1)

np.min(a1)

np.prod(a1)

np.sum(a1)

np.max(a1,axis=0)

np.max(a1,axis=1)

np.min(a1,axis=1)

np.exp(a1)

np.sin(a1)

np.var(a1,axis=1)

a1 = np.arange(16,dtype=float).reshape(4,4)
a2 = np.arange(16,dtype=float).reshape(4,4)
a3 = np.arange(16,dtype=np.int32).reshape(4,4)
a2

np.dot(a1,a2)

np.ceil(np.random.random((2,3))*100)

np.mean(a1,axis=1)

np.median(a1,axis=1)

np.std(a1,axis=1)

np.tan(a1)

a1

a2

a2[2,2]

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(64).reshape(4,4,4)
a3

a1[1]

a3[1,0,1]

a3[2,2,1]

a3[3,2,2]

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(160).reshape(10,4,4)
a3

a3[4,0,2]

a3.ravel()

np.transpose(a2)
a2.T

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(24,36).reshape(3,4)
a4

np.hstack((a4,a5))

np.vstack((a4,a5))

np.hsplit(a5,2)

a5[0:2]

a5[1:,1:3]

a2

a2[1:,0::3]

a3

a3[2,2:,1:3]

a3[4,2:,0::3]

a3[5,2:,0::2]

a4 = np.arange(27).reshape(3,3,3)
a4

#[10 11],[19,20]
a4[1:,0,1:]

for i in np.nditer(a3):
    print(i)

import numpy as np
import pandas as pd

country = ['India','USA','Nepal','Russia','England']
pd.Series(country)

marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']
pd.Series(marks,index=subjects)

marks = pd.Series(marks,name='Daksh ke marks')
marks

marks = {
    'maths':99,
    'English':96,
    'science':77,
    'Hindi':83,
}
marks_series = pd.Series(marks,name='Daksh ke marks')
marks_series

marks_series.size

marks_series.dtype

marks_series.name

marks_series.is_unique
pd.Series([1,1,2,3,4,5]).is_unique

marks_series.index

subs = pd.read_csv('weather_by_cities.csv',squeeze=True)
subs

subs = pd.read_csv('subs.csv',squeeze=True)

subs

import pandas as pd
bw = pd.read_csv('bollywood.csv',squeeze=True)
bw

vk = pd.read_csv('kohli_ipl (3).csv',squeeze=True)
vk

import pandas as pd
movies = pd.read_csv('movies-1.csv',squeeze=True)
movies

subs.head()

subs.head(3)

subs.tail(6)

movies.sample(5)

movies.value_counts

subs.sort_values(by='runs',ascending=False).head(1).values[0]

vk.max()

vk[-1:]

vk.sort_index(ascending=False).head(1).values[0]

movies['Machine (2017 film)']

movies[::26]

print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(min(subs))
print(max(subs))

import numpy as np
import pandas as pd
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
pd.DataFrame(student_data,columns=['iq','marks','package'])

movies = pd.read_csv('movies-1.csv')
movies

print(movies.shape)
print(vk.shape)

print(movies.dtypes)

print(vk.index)

movies.info()

vk.info

subs.info()

movies.describe()

vk.isnull().sum()

movies['title_x']

movies.iloc[6]

movies

subs

vk

movies.iloc[0:3,0:3]

movies.value_counts().head(20).plot(kind='pie')

vk.value_counts().head(20).plot(kind='pie')

x=[1,2,3]
y=[2,5,1]
plt.plot(x,y)
plt.show()

subs

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('default')

price = [48000,54000,57000,49000,47000,45000]
year = [2015,2016,2017,2018,2019,2020]

plt.plot(year,price)
plt.show()

batsman = pd.read_csv('sharma-kohli.csv')
batsman
plt.plot(batsman['index'],batsman['V Kohli'])
plt.show()

batsman = pd.read_csv('sharma-kohli.csv')
batsman

plt.plot(batsman['index'],batsman['V Kohli'])
plt.plot(batsman['index'],batsman['RG Sharma'])

plt.plot(batsman['index'],batsman['V Kohli'])
plt.plot(batsman['index'],batsman['RG Sharma'])

plt.title('Rohit Sharma Vs Virat kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

plt.plot(batsman['index'],batsman['V Kohli'],color='#ff240d')
plt.plot(batsman['index'],batsman['RG Sharma'],color='#c6dc37')

plt.title('Rohit Sharma Vs Virat kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

movies = pd.read_csv('movies-1.csv')
movies

plt.plot(movies['runtime'],movies['imdb_rating'],color='#ff240d',linestyle='solid',marker='o',markersize=2,linewidth=0.1)
plt.show
plt.grid()

plt.plot(batsman['index'],batsman['V Kohli'],color='#ff240d',linestyle='dotted',linewidth=3,marker='s',markersize=5,label='virat')
plt.plot(batsman['index'],batsman['RG Sharma'],color='#c6dc37',linestyle='dashdot',linewidth=2,marker='o',markersize=5,label='rohit')

plt.title('Rohit Sharma Vs Virat kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.legend(loc='upper right')
plt.grid()

plt.plot(movies['imdb_votes'],movies['year_of_release'],color='#ff240d',linestyle='solid',linewidth=1)
plt.show

price = [48000,54000,57000,49000,47000,4500000]
year = [2015,2016,2017,2018,2019,2020]
plt.title('Ambani Ji ki jai ho')

plt.plot(year,price)
plt.ylim(0,75000)
plt.grid()

x = np.linspace(-10,10,50)
y = 10*x + 3 + np.random.randint(0,30,50)
y

plt.scatter(x,y)
plt.show()

batter = pd.read_csv('batter.csv')
batter

plt.plot(batter['runs'],batter['strike_rate'])

children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']
plt.bar(colors,children,color='cyan')

plt.barh(colors,children,color='darkgreen')
plt.grid()

children = [10,20,40,10,30]
colors = ['red red red red red red','blue blue blue blue','green green green','yellow yellow yellow','pink pink']
plt.bar(colors,children,color='skyblue')
plt.xticks(rotation='vertical')
plt.show()

bat = pd.read_csv('batsman_season_record.csv')
bat

plt.bar(bat['batsman'],bat['2017'],label='2017')
plt.bar(bat['batsman'],bat['2016'],bottom=bat['2017'],label='2016')
plt.bar(bat['batsman'],bat['2015'],bottom=(bat['2016'] + bat['2017']),label='2018')
plt.legend()

data = [23,45,100,20,49]
subjects = ['eng','science','maths','sst','hindi']
plt.pie(data,labels=subjects)
plt.show()

from scipy import special as sp

a=sp.exp10(7)
print(a)
b=sp.exp2(5)
print(b)

c=sp.sindg(45)
print(c)
d=sp.cosdg(60)
print(d)

from scipy import constants as con

con.find()

con.value('Planck constant')

con.value('weak mixing angle')

con.value('luminous efficacy')

from scipy.stats.mstats import gmean,hmean

g=gmean([1,50,20])
print(g)

h=hmean([1,50,20])
print(h)

from numpy import poly1d

p=poly1d([4,5,7,8],variable='y')
print(p)

p=poly1d([3,6,5])
print(p)

def upper_dec(func):#2
    def wrapper():#11
        s1=func()#12
        return s1.upper()#15
    return wrapper#3
def split_dec(func):#5
    def inner():#9
        s2 = func()#10 #16
        return s2.split()#17
    return inner#6

def myfun(): #13
    return "Hello Students" #14
s=split_dec(upper_dec(myfun)) #1,4,7

s()#8

import time
def timer(func):
  def wrapper(*args):
    start = time.time()
    func(*args)
    print('time taken by',func.__name__,time.time()-start,'secs')
  return wrapper
@timer
def hello():
    print('hello world')
    time.sleep(3)
@timer
def square(num):
    print(num**2)
    time.sleep(4)
@timer
def power(a,b):
    print(a**b)
    time.sleep(5)
hello()
square(2)
power(2,3)

def sanity_check(data_type):
  def outer_wrapper(func):
    def inner_wrapper(*args):
      if type(*args) == data_type:
        func(*args)
      else:
        raise TypeError('Ye datatype nhi chalega')
    return inner_wrapper
  return outer_wrapper

#@sanity_check(int)
#def square(num):
     #print(num**2)

@sanity_check(str)
def greet(name):
    print('hello',name)
#square("Maneesh")
greet("Maneesh")

def sanity_check(data_type):
  def outer_wrapper(func):
    def inner_wrapper(*args):
      if type(*args) == data_type:
        func(*args)
      else:
        raise TypeError('Ye datatype nhi chalega')
    return inner_wrapper
  return outer_wrapper

@sanity_check(int)
#def square(num):
     #print(num**2)

@sanity_check(str)
def greet(name):
    print('hello',name)
#square("Maneesh")
greet("Maneesh")

num=[1,2*8,3]

for i in num:
  print(i)

L = [x for x in range(1,10000000)]
#for i in L:
 #print(i*2)
import sys
print(sys.getsizeof(L)/1024)
#print(dir(L))
x = range(1,10000000)
#for i in x:
 #print(i*2)
print(sys.getsizeof(x)/1024)
#print(dir(p))

L=[1,2,3]
#L is not an iterator
iter_L=iter(L)
print(dir(iter_L))
#iter_L is an iterator

num = [1,2,3]
# Fetch the iterator
iter_num = iter(num)
# step2- next
next(iter_num)
next(iter_num)
next(iter_num)
next(iter_num)

num = [1,2,3]
# Fetch the iterator
iter_num = iter(num)
# step2- next
next(iter_num)
next(iter_num)

class Sq:
    def __init__ (self):
        self.a=0
    def __iter__ (self):
        return self
    def __next__ (self):
        if self.a<=9:
           self.a=self.a+1
           return self.a**2
        else:
           raise StopIteration
for i in Sq():
    print(i)

def mera_loop(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(next(iterator))
    except StopIteration:
      break

a = [1,2,3]
b = range(1,11)
c = (1,2,3)
d = {1,2,3}
e = {0:1,1:1}
mera_loop(e)

l=[1,2,3,4]
for i in l:
 print(i)
print(id(iter(l)))
print(id(i))
print(dir(i))
print(dir(l))

type(x)

