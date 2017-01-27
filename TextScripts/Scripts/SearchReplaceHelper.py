import tkinter
import re


def SimpleSearchReplace(t1):
	expList = []
	expression = [search,replace]
	expList.append(expression)
	for i in range(len(expList)):
		t1 = re.sub(expList[i][0], expList[i][1], text)

def initialize():
	#Window
	root = tkinter.Tk()
	root.title('Advanced Search & Replace')
	root.minsize(width=900,height=600)
	
	#Labels
	l1 = tkinter.Label(root, text = 'Search')
	l1.grid(row=0,column=0)
	l2 = tkinter.Label(root, text = 'Replace')
	l2.grid(row=1,column=0)
	
	#Inputs
	e1 = tkinter.Entry(root)
	e1.grid(row=0,column=1)
	e2 = tkinter.Entry(root)
	e2.grid(row=1,column=1)
	
	#Text
	t1 = tkinter.Text(root)
	t1.grid(row = 3,column=1)
	
	#Start
	root.mainloop()

def build(root, e1, e2, t1)
	
	#b = tkinter.Button(root, text ='Execute')

initialize()
build()
