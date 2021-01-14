'''first need to create database using cmd in the same folder where this py file is
in cmd--> sqlite3 dbname.db
		   create table student (rno int primary key, name text);
		   select * from student;
		   .exit
'''

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import socket
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


#6)define function
#f1,f3,f2-add

def f1():
	adst.deiconify()     #button to go next screen
	root.withdraw()
def f2():
	root.deiconify()     #back to last screen
	adst.withdraw()


def f3():
	con = None
	try:
		con = connect("stu.db")
		print("connected")
		if entrno.get() == "":
			raise Exception("enter rno")
		else:
			rno = int(entrno.get())

		name = entname.get()

		if entmarks.get() == "":
			raise Exception("student should have marks")
		else:
			marks = int(entmarks.get())

		if (len(name) == 0):
			raise Exception("enter name")
		elif rno < 0:
			raise Exception("roll no should be positive")
		elif len(name) < 2:
			raise Exception("name should have atleast more than 2 alphabets")
		elif name.isalpha() is False:
			raise Exception("name should contain only characters")
		elif marks < 0 or marks > 100:
			raise Exception("invalid range,marks should be from 0-100")

		args = (rno, name, marks)
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s', '%d')"
		cursor.execute(sql % args)
		con.commit()
		showinfo("success", "record added")

		entrno.delete(0, END)
		entname.delete(0, END)
		entmarks.delete(0, END)
	except ValueError:
		showerror("Mistake", "Integers only")
		entrno.delete(0, END)
		entname.delete(0, END)
		entmarks.delete(0, END)
	except Exception as e:
		showerror("failure", "insert issue-> " + str(e))
		entrno.delete(0, END)
		entname.delete(0, END)
		entmarks.delete(0, END)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")


#f4,f5-view
def f4():
	stdata.delete(1.0, END)
	viewst.deiconify()
	root.withdraw()
	con=None
	try:
		con=connect("stu.db")
		print("connected")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"rno:" +str(d[0])+ " name:" +str(d[1])+ " marks:" +str(d[2])+ "\n"
		stdata.insert(INSERT, info)
	except Exception as e:
		print("select issue->", e)
	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f5():
	root.deiconify()
	viewst.withdraw()

#f6, f7, f8-->update
def f6():
	updst.deiconify()
	root.withdraw() 

def f7():
	root.deiconify()
	updst.withdraw()

def f8():
	
	con=None
	try:   
		con=connect("stu.db")
		print("connected")
		if enturno.get()=="":
			raise Exception("enter rno")
		else:
			rno=int(enturno.get())

		name=entuname.get()

		if entumarks.get()=="":
			raise Exception ("student should have marks")
		else:
			marks=int(entumarks.get())
		
		if (len(name)==0):
			raise Exception("enter name")
		elif rno<0:
			raise Exception("roll no should be positive")
		elif len(name)<2:
			raise Exception("name should have atleast more than 2 alphabets")
		elif name.isalpha() is False:
			raise Exception("name should contain only characters")
		elif marks<0 or marks>100:
			raise Exception("invalid range,marks should be from 0-100")
		args=(name, marks, rno)
		cursor=con.cursor()
		sql="update student set name='%s', marks='%d' where rno='%d'"
		cursor.execute(sql % args)
		if cursor.rowcount>=1:
			con.commit()
			showinfo("success", "record upated")
		else:
			showwarning(rno, "does not exists")
		enturno.delete(0, END)
		entuname.delete(0, END)
		entumarks.delete(0, END)
	except Exception as e:
		showerror("error", "update issue->" + str(e))
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")

#f9, f10, f11-delete
def f9():
	delst.deiconify()    #button to go next screen
	root.withdraw()

def f10():
	root.deiconify()     #back to last screen
	delst.withdraw()

def f11():
	con=None
	try:
		con=connect("stu.db")
		print("connected")
		if entdrno.get()=="":
			raise Exception("enter rno")
		else:
			rno=int(entdrno.get())
		if rno<0:
			raise Exception("roll no should be positive")
		args=(rno)

		cursor=con.cursor()
		sql="delete from student where rno='%d'"
		cursor.execute(sql % args)  
		if cursor.rowcount>=1:
			con.commit()
			showinfo("success", "record deleted")
		else:
			showwarning(rno, "does not exists")
		entdrno.delete(0, END)
	except Exception as e:
		showerror("error", "delete issue->" + str(e))
		con.commit()
		entdrno.delete(0, END)
	finally:
		if con is not None:
			con.close()
			print("disconnected")       

#f12-chart
def f12():
	con=None
	try:
		con=connect("stu.db")
		print("connected")
		cursor=con.cursor()
		sql="SELECT * FROM student ORDER BY marks DESC LIMIT 5"
		cursor.execute(sql)
		data=cursor.fetchall()
		name=[]
		marks=[]
		
		for d in data:
			name.append(d[1])
			marks.append(d[2])
		plt.bar(name, marks, color=['yellow', 'red', 'green', 'blue', 'orange'])
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.title("Batch Information")
		plt.show()
	except Exception as e:
		print("issue->", e)
	finally:
		if con is not None:
			con.close()
			print("disconnected")

# 7)Location 8)Temperature
	
socket.create_connection(("www.google.com", 80))
res=requests.get("https://ipinfo.io")
print(res)
data=res.json()
#print(data)
	
city_name=data['city']
#print(city_name)
var=city_name
#print(var)

if var=='Thāne':	

	try:
		city_name='Thane'	
		socket.create_connection(("www.google.com", 80))
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q=" + city_name
		a3="&appid=df3dab41a4818a594a479a4cd99a9463" #new appid

		api_address=a1+a2+a3
		res=requests.get(api_address)
		print(res)

		data=res.json()
		#print(data)
		temperature=data['main']['temp']
		#print(temp1)

	except Exception as e:
		print("issue", e)


# 9)quote of the day
try:
	socket.create_connection(("www.google.com", 80))
	res = requests.get("https://www.brainyquote.com/quote_of_the_day")
	#print(res)
	
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	data = soup.find("img", {"class": "p-qotd"})
	msg = data['alt']

except Exception as e:
	print("issue", e)

#1)create root window

root=Tk()
root.title("S.M.S.")
root.geometry("400x500+400+100")
root.configure(background='light green')

btnadd=Button(root, text="Add", font=("arial", 18, "bold"), width=10, command=f1)
btnview=Button(root, text="View", font=("arial", 18, "bold"), width=10, command=f4)
btnupdate=Button(root, text="Update", font=("arial", 18, "bold"), width=10, command=f6)
btndelete=Button(root, text="Delete", font=("arial", 18, "bold"), width=10, command=f9)
btncharts=Button(root, text="Charts", font=("arial", 18, "bold"), width=10, command=f12)

lbllocation = Label(root, text="Location:", font=("arial", 14, "bold"), bg='light green')
lbltemp = Label(root, text="Temp:", font=("arial", 14, "bold"), bg='light green')
lblqotd = Label(root, text="QOTD:", font=("arial", 14, "bold"), bg='light green')
lblloc = Label(root, text=city_name, font=("arial", 14), bg='light green')
lbltemperature = Label(root, text=temperature, font=("arial", 14), bg='light green')
lblQotd = Label(root, text=msg, font=("arial",14), bg='light green', wraplength=300)

btnadd.pack(pady=10)
btnview.pack(pady=10)
btnupdate.pack(pady=10)
btndelete.pack(pady=10)
btncharts.pack(pady=10)

lbllocation.place(x=10, y=360)
lbltemp.place(x=195, y=360)
lblqotd.place(x=10, y=400)
lblloc.place(x=100, y=360)
lbltemperature.place(x=260, y=360)
lblQotd.place(x=80, y=400)



#2)create add student window

adst=Toplevel(root)
adst.title("Add St.")
adst.geometry("400x400+400+100")
adst.configure(background='light blue')
adst.withdraw()

lblrno=Label(adst, text="enter roll no", font=("arial", 18, "bold"), bg='light blue')
entrno=Entry(adst, bd=5, font=("arial", 18, "bold"))
lblname=Label(adst, text="enter name", font=("arial", 18, "bold"), bg='light blue')
entname=Entry(adst, bd=5, font=("arial", 18, "bold"))
lblmarks=Label(adst, text="enter marks", font=("arial", 18, "bold"), bg='light blue')
entmarks=Entry(adst, bd=5, font=("arial", 18, "bold"))
btnsave=Button(adst, text="Save", font=("arial", 18, "bold"), command=f3)
btnback=Button(adst, text="Back", font=("arial", 18, "bold"), command=f2)

lblrno.pack(pady=5)
entrno.pack(pady=5)
lblname.pack(pady=5)
entname.pack(pady=5)
lblmarks.pack(pady=5)
entmarks.pack(pady=5)
btnsave.pack(pady=5)
btnback.pack(pady=5)

#3)create view student window

viewst=Toplevel(root)
viewst.title("View St.")
viewst.geometry("400x400+400+100")
viewst.configure(background='pink')
viewst.withdraw()

stdata=ScrolledText(viewst, width=30, height=20)
btnvback=Button(viewst, text="Back", font=("arial", 18, "bold"), command=f5)

stdata.pack(pady=10)
btnvback.pack(pady=10)

#4) create update window

updst=Toplevel(root)
updst.title("Update St.")
updst.geometry("400x400+400+100")
updst.configure(background='light yellow')
updst.withdraw()

lblurno=Label(updst, text="enter rno", font=("arial", 18, "bold"), bg='light yellow')
enturno=Entry(updst, bd=5, font=("arial", 18, "bold"))
lbluname=Label(updst, text="enter new name", font=("arial", 18, "bold"), bg='light yellow')
entuname=Entry(updst, bd=5, font=("arial", 18, "bold"))
lblumarks=Label(updst, text="enter updated marks", font=("arial", 18, "bold"), bg='light yellow')
entumarks=Entry(updst, bd=5, font=("arial", 18, "bold"))
btnusave=Button(updst, text="Save", font=("arial", 18, "bold"), command=f8)
btnuback=Button(updst, text="Back", font=("arial", 18, "bold"), command=f7)

lblurno.pack(pady=5)
enturno.pack(pady=5)
lbluname.pack(pady=5)
entuname.pack(pady=5)
lblumarks.pack(pady=5)
entumarks.pack(pady=5)
btnusave.pack(pady=5)
btnuback.pack(pady=5)

#5) create delete window

delst=Toplevel(root)
delst.title("Delete St.")
delst.geometry("400x400+400+100")
delst.configure(background='light blue')
delst.withdraw()

lbldrno=Label(delst, text="enter rno", font=("arial", 18, "bold"), bg='light blue')
entdrno=Entry(delst, bd=5, font=("arial", 18, "bold"))
btndsave=Button(delst, text="Save", font=("arial", 18, "bold"), command=f11)
btndback=Button(delst, text="Back", font=("arial", 18, "bold"), command=f10)

lbldrno.pack(pady=5)
entdrno.pack(pady=5)
btndsave.pack(pady=5)
btndback.pack(pady=5)

root.mainloop()
