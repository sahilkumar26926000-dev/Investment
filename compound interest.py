# compond interest gui calculator
from tkinter import *
def clear_all():
    principlefield.delete(0,END)
    ratefield.delete(0,END)
    timefield.delete(0,END)
    compoundfield.delete(0,END)

    principlefield.focus_set()

def calculator_ci(): #define for user input
    principle = int(principlefield.get())
    rate = float(ratefield.get())
    time = int(timefield.get())
    ci = principle*(pow((1+rate/100),time))
    compoundfield.insert(3,ci)

if __name__ =='__main__':
    root=Tk() #Using libray for modified structure
    root.configure(background='light green')
    root.geometry('400x300')
    root.title('compound interest calculator')
    lab1=Label(root,text ='principle amount(rs):',fg='black',bg='grey')
    lab2=Label(root,text="rate of interest:",fg='black',bg='grey')
    lab3=Label(root,text='time(years):',fg='black',bg='grey')
    lab4=Label(root,text='compound interest:',fg='black',bg='grey')
    
    lab1.grid(row=1,column=0,padx=10,pady=10)
    lab2.grid(row=2,column=0,padx=10,pady=10)
    lab3.grid(row=3,column=0,padx=10,pady=10)
    lab4.grid(row=5,column=0,padx=10,pady=10)

    principlefield=Entry(root)
    ratefield=Entry(root)
    timefield=Entry(root)
    compoundfield=Entry(root)

    principlefield.grid(row=1,column=1,padx=10,pady=10)
    ratefield.grid(row=2,column=1,padx=10,pady=10)
    timefield.grid(row=3,column=1,padx=10,pady=10)
    compoundfield.grid(row=5,column=1,padx=10,pady=10)
    
    b1 = Button(root,text='SUMBIT',bg='black',fg='white',command=calculator_ci)
    b2 = Button(root,text='CLEAR',bg='black',fg='white',command=clear_all)
    
    b1.grid(row=4,column=1,pady=10)
    b2.grid(row=6,column=1,pady=10)

    root.mainloop()