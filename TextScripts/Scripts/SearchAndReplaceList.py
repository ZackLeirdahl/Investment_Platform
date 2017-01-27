##Current State: Manual input of filename, one by one search and replace expression, no copy paste ability, 
#ask after every expression to continue


##Next iteration: 
import re
import tkinter
win = tkinter.Tk()

fname = input('Enter the filename: ')
flag = True
expList = []
while flag:
        addExpression = input('Add an expression?: ')
        if addExpression != 'Y':
                flag = False
        else:
                search = input('Enter text to search for: ')
                replace = input('Enter the replacement text: ')
                expression = [search,replace]
                expList.append(expression)

ofile = open(fname,'r')
text = ''
while not flag:
        line = ofile.readline()
        if line == '':
                flag = True
        text = text + line
ofile.close()

for i in range(len(expList)):
        text = re.sub(expList[i][0], expList[i][1], text)

ofile = open(fname, 'w')
ofile.write(text)
ofile.close()
