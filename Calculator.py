from tkinter import *
from math import *


#-----WINDOW-----
window = Tk()
window.config(bg='#ece7e7')
window.title('Calculator Challenge')
i = 0

#-----ENTRY-----
screen = Entry(window, font='Roboto')
Ans = Label(window, font='Roboto 8', text= 'Ans', bg='black', fg='white', pady=2, anchor=NW)
screen.grid(row=0, column=0, columnspan=5, padx=8, pady=5)
Ans.grid(row=6, column=3, sticky=E+W,columnspan=2)

#-----FUNTIONS-----

def click_button(event):
    global i
    screen.insert(i, event)
    i += len(str(event))

def delete():
    screen.delete(0, END)
    i = 0

def same():
    equation = screen.get()
    result = round(eval(equation), 4)
    screen.delete(0, END)
    screen.insert(0, result)
    Ans['text'] = result
    i = len(str(result))

def delete_last():
    screen.delete(len(screen.get())-1, END)
    i = len(screen.get())-1


#-----BUTTONS-----

#numbers
number1 = Button(window, text='1', width=5, height=2 , command= lambda:click_button(1))
number2 = Button(window, text='2', width=5, height=2 , command= lambda:click_button(2))
number3 = Button(window, text='3', width=5, height=2 , command= lambda:click_button(3))
number4 = Button(window, text='4', width=5, height=2 , command= lambda:click_button(4))
number5 = Button(window, text='5', width=5, height=2 , command= lambda:click_button(5))
number6 = Button(window, text='6', width=5, height=2 , command= lambda:click_button(6))
number7 = Button(window, text='7', width=5, height=2 , command= lambda:click_button(7))
number8 = Button(window, text='8', width=5, height=2 , command= lambda:click_button(8))
number9 = Button(window, text='9', width=5, height=2 , command= lambda:click_button(9))
number0 = Button(window, text='0', width=5, height=2 , command= lambda:click_button(0))

#operators
button_div = Button(window, text='÷', width=5, height=2 , command= lambda:click_button('/'))
button_mult = Button(window, text='x', width=5, height=2, command= lambda:click_button('*'))
button_sum = Button(window, text='+', width=5, height=2, command= lambda:click_button('+'))
button_sub = Button(window, text='-', width=5, height=2, command= lambda:click_button('-'))
button_raise = Button(window, text='^', width=5, height=2, command= lambda:click_button('**'))

#symbols
button_same = Button(window, text='=', width=5, height=2, command= same)
button_delete = Button(window, text='AC', width=5, height=2, command= delete)
button_point = Button(window, text='.', width=5, height=2, command= lambda:click_button('.'))
button_e = Button(window, text='e', width=5, height=2, command= lambda:click_button('e'))
button_pi = Button(window, text='π', width=5, height=2, command= lambda:click_button('pi'))
button_sin = Button(window, text='sin', width=5, height=2, command= lambda:click_button('sin('))
button_cos = Button(window, text='cos', width=5, height=2, command= lambda:click_button('cos('))
button_par1 = Button(window, text='(', width=5, height=2, command= lambda:click_button('('))
button_par2 = Button(window, text=')', width=5, height=2, command= lambda:click_button(')'))
button_delete1 = Button(window, text='DEL', width=5, height=2, command= delete_last)

#-----BUTTON LOCATION-----

number1.grid(row=4, column=0, padx=2, pady=2)
number2.grid(row=4, column=1, padx=2, pady=2)
number3.grid(row=4, column=2, padx=2, pady=2)
number4.grid(row=3, column=0, padx=2, pady=2)
number5.grid(row=3, column=1, padx=2, pady=2)
number6.grid(row=3, column=2, padx=2, pady=2)
number7.grid(row=2, column=0, padx=2, pady=2)
number8.grid(row=2, column=1, padx=2, pady=2)
number9.grid(row=2, column=2, padx=2, pady=2)
number0.grid(row=5, column=0, padx=2, pady=2)

button_point.grid(row=5, column=1, padx=2, pady=2)
button_delete1.grid(row=2, column=4, padx=2, pady=2)

button_delete.grid(row=2, column=3, padx=2, pady=2)
button_same.grid(row=5, column=4, padx=2, pady=2)
button_mult.grid(row=3, column=3, padx=2, pady=2)
button_div.grid(row=3, column=4, padx=2, pady=2)
button_sum.grid(row=4, column=3, padx=2, pady=2)
button_sub.grid(row=4, column=4, padx=2, pady=2)
button_e.grid(row=5, column=2, padx=2, pady=2)
button_pi.grid(row=5, column=3, padx=2, pady=2)

button_sin.grid(row=1, column=0, padx=2, pady=2)
button_cos.grid(row=1, column=1, padx=2, pady=2)
button_par1.grid(row=1, column=2, padx=2, pady=2)
button_par2.grid(row=1, column=3, padx=2, pady=2)
button_raise.grid(row=1, column=4, padx=2, pady=2)




window.mainloop()