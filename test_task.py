import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar
import os
from working_files import rech
def fi(z):
    f = open('zn.txt', 'a', encoding='utf-8')
    f.write(z+"\n")
    f.close()
def fif():
    t=["",""]
    f = open('zn.txt', 'r', encoding='utf-8')
    for i in f:
        if "начало:" in i:
            t[0] = i.split(":")[-1][:-1]
        elif "конец:" in i:
            t[1] = i.split(":")[-1][:-1]
    f.close()
    return t
def switch_windows():
    window1.withdraw()
    window2.deiconify()
def switch_windows2():
    window1.withdraw()
    window3.deiconify()
def updateLabel(event):
    t=""
    z = calendar.get_date().split("/")
    z[-1]="20"+z[-1]
    w = z[1]
    z[1] = z[0]
    z[0] = w
    for i in range(len(z)):
        if len(z[i]) == 1:
            if int(z[i])<10:
                t+="0"+z[i]
            else:
                t+=z[i]
        elif len(z[i]) == 4:
            t+=z[i][-2:]
        else:
            t+=z[i]
        t+="."
    fi("начало:"+t[:-1])
    inputtxt1.delete('1.0', "end")
    inputtxt1.insert("1.0",str(t[:-1]))
def updateLabel1(event):
    t2 = ""
    z2 = calendar2.get_date().split("/")
    z2[-1] = "20" + z2[-1]
    w2 = z2[1]
    z2[1] = z2[0]
    z2[0] = w2
    for i in range(len(z2)):
        if len(z2[i]) == 1:
            if int(z2[i]) < 10:
                t2 += "0" + z2[i]
            else:
                t2 += z2[i]
        elif len(z2[i]) == 4:
            t2 += z2[i][-2:]
        else:
            t2 += z2[i]
        t2 += "."
    fi("конец:"+t2[:-1]+"\n")
    inputtxt2.delete('1.0', "end")
    inputtxt2.insert("1.0",str(t2[:-1]))
def viv():
    editor.delete('1.0', "end")
    if fif() == ["",""]:
        inputtxt1.insert("1.0","выберите дату")
    else:
        rech(fif()[0], fif()[1])
        f = open('otvet.txt', 'r',encoding='utf-8')
        for i in f:
            editor.insert("end", str(i))
        f.close()
def printt():
    window2.withdraw()
    window1.deiconify()
def printt2():
    window3.withdraw()
    window1.deiconify()


window1 = tk.Tk()
window1.title("TextBox Input")
window1.geometry('500x300')

button = tk.Button(window1, text="Выбрать дату начала", command=switch_windows)
button.place(x=20, y=20)
#второе окно
window2 = tk.Toplevel()
window2.withdraw()
calendar = Calendar(window2, mindate=datetime(2001, 1, 1), maxdate=datetime(2003, 12, 30), showweeknumbers=False,showothermonthdays=False)
calendar.pack()
calendar.bind('<<CalendarSelected>>', updateLabel)
message_button = tk.Button(window2, text="Click Me", command=printt)
message_button.pack()
#запись в первом окне первого значения
inputtxt1 = tk.Text(window1,height = 1, width = 15)
inputtxt1.bind("<Key>", lambda e: "break")
inputtxt1.place(x=20, y=50)
button = tk.Button(window1, text="Выбрать дату конца", command=switch_windows2)
button.place(x=220, y=20)
#третье окно
window3 = tk.Toplevel()
window3.withdraw()
calendar2 = Calendar(window3, mindate=datetime(2001, 1, 1), maxdate=datetime(2003, 12, 30), showweeknumbers=False, showothermonthdays=False)
calendar2.pack()
calendar2.bind('<<CalendarSelected>>', updateLabel1)
message_button2 = tk.Button(window3, text="Click Me", command=printt2)
message_button2.pack()
#запись в первом окне второго значения
inputtxt2 = tk.Text(window1,height = 1, width = 14)
inputtxt2.bind("<Key>", lambda e: "break")
inputtxt2.place(x=220, y=50)
editor = tk.Text(window1,height = 10, width = 50)
editor.place(x=20, y=110)
message_button1 = tk.Button(window1,text="Вывести результат анализа", command=viv)
message_button1.place(x=20, y=80)
f = open('zn.txt', 'w')
f.write('')
f.close()
window1.mainloop()