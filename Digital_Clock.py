from tkinter import *
from time import strftime
from pygame import mixer
import time
from tkinter import messagebox


root = Tk()
root.title("デジタル時計")
root.geometry("550x350")

def time():
    string = strftime("%H時:%M分:%S秒 \n%Y年-%m月-%d日")
    label.config(text = string)
    label.after(1000,time)
label = Label(root, font=("ds-digital.TTF", 30), foreground="cyan",background="purple")
label.pack(side="bottom")

msgi=StringVar()
alarmtime = StringVar()

head = Label(root, text = "デジタル　アラム　時計", font = ("Arial",20))
head.pack(side="top")

mixer.init()

def ala():
    a = alarmtime.get()
    AlarmT = a
    Currenttime = strftime("%H:%M")
    
    while AlarmT!=Currenttime:
        Currenttime = strftime("%H:%M")
    if AlarmT == Currenttime:
        mixer.music.load("C:\\Users\\Monst\\OneDrive\\Desktop\\Python\\1aa.mp3")
        mixer.music.play() 
        msg = messagebox.showinfo('Info',f'{msgi.get()}')
          
        if msg == "ok":
            mixer.stop() 


panel = Frame(root)
panel.place(x=5, y=70)

lbl1=Label(panel,text="アラム設定\n (Hr:min)", font = ("Arial", 18))
lbl1.grid(row=0,column=1,padx=10,pady=5)

entry=Entry(panel,textvariable=alarmtime,font =("Ariel", 20),width = 5)
entry.grid(row=0,column=2,padx=10,pady=10)

msg = Label(panel,text="アラムメッセージ", font = ("Arial", 18))
msg.grid(rows=1,column=1,padx=10,pady=5)

msgbox=Entry(panel,textvariable=msgi,font =("Ariel", 20),width = 18)
msgbox.grid(row=1,column=2,padx=10,pady=5)

submit = Button(root,text="アラム決定",width = 40,command=ala)
submit.pack(pady=10,padx=10)

time()
root.mainloop()
