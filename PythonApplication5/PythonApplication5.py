from tkinter import*
from math import*
def decision(event):
	if (a.get()!="" and b.get()!="" and c.get()!=""):
		a_=int(a.get())
		b_=int(b.get())
		c_=int(c.get())
		D=b_**2-4*a_*c_
		if D==0:
			x1_=((-1)*b_)/(2*a)
			answer.configure(text=f"x = {x1}")
		elif D>0:
			x1_=round((((-1)*b_)+sqrt(D))/(2*a),2)
			x2_=round((((-1)*b_)-sqrt(D))/(2*a),2)
			answer.configure(text=f"x1 = {x1_}\nx2 = {x2_}")
		else:
			answer.configure(text="У уравнения нет корней")
		a.configure(bg="white")
		b.configure(bg="white")
		c.configure(bg="white")
	else:
		if a.get()=="":
			a.configure(bg="red")
		elif b.get()=="":
			b.configure(bg="red")
		else:
			c.configure(bg="red")
win=Tk()
win.geometry("600x200")
win.title("Решение квадратного уравнения")
lbl=Label(win,text="Решите квадратное уравнение",font="Calibri 26",fg="grey",bg="white")
lbl.pack()
answer=Label(win,text="решение",font="Calibri 26",fg="grey",bg="white")
answer.pack()
a=Entry(win,font="Calibri 26",fg="grey",bg="white",width=3)
a.pack(side=LEFT)
x1=Label(win,text="x**2+",font="Calibri 26",fg="grey",bg="white")
x1.pack(side=LEFT)
b=Entry(win,font="Calibri 26",fg="grey",bg="white",width=3)
b.pack(side=LEFT)
x2=Label(win,text="x+",font="Calibri 26",fg="grey",bg="white")
x2.pack(side=LEFT)
c=Entry(win,font="Calibri 26",fg="grey",bg="white",width=3)
c.pack(side=LEFT)
x=Label(win,text="=0",font="Calibri 26",fg="grey",bg="white")
x.pack(side=LEFT)
btn=Button(win,text="Показать решение",fg="grey",bg="black",font="Arial 20",width=15)
btn.pack(side=LEFT)
btn.bind("<Button-1>",decision)

win.mainloop()

