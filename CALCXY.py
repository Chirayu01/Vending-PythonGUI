from tkinter import *
from tkinter import messagebox
import math as m
from xml.etree.ElementTree import PI

calculator = Tk()
calculator.title("電卓")

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.createWidgets()
    
    def replaceText(self,text):
        self.display.delete(0, END)
        self.display.insert(0, text)
        
    def appendToDisplay(self,text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)
        if self.entryText == "0":
             self.replaceText(text)
        else:
             self.display.insert(self.textLength, text)  
    
    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/ 100")
        
        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
             messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)
             
    def clearText(self):
        self.replaceText("0")
    
    def squared(self):
        self.result = False
        self.display = m.sqrt (float(self.display.get()))
        self.display.get()
    
    def Clear_Entry(self):
        current=self.display.get()
        length=len(current)-1
        self.display.delete(length, END)
        
    def sc(self):
        key=self.widgetName
        text=key["text"]
        no=self.display.get()
        result=""
        if text == "Pi":
            if no == "":
                result=str(m.pi)  
            else:
                result=str(float(no) * m.pi) 
        self.display.delete(0, END)
        self.display.insert(0, result)
                 
    def createWidgets(self):
        self.display = Entry(self, font=("arial", 35,"bold"),bg = "royalblue",border=30,width=20,justify = RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=100)    
        #::::::::::::ROW1:::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.sevenButton = Button(self, pady=1,border=4,fg="black",bg = "lavender",font=("arial",20,"bold"),width=6,height=2,text="7",
                               command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column=0)
        
        self.eightButton = Button(self, pady=1,border=4,fg="black",bg = "lavender",font=("arial",20,"bold"),width=6,height=2,text="8",
                               command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column=1)
        
        self.nineButton = Button(self, pady=1,border=4,fg="black",bg = "lavender",font=("arial",20,"bold"), width=6,height=2,text="9",
                        command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column=2)
        
        self.timesButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"), width=6,height=2,text="x", 
                                  command=lambda: self.appendToDisplay("*"))
        self.timesButton.grid(row=1, column=3)
        
        self.clearButton = Button(self, pady=1,border=4,fg="black",bg = "red",font=("arial",20,"bold"),width=6,height=2,text="AC",
                                  command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4)
 #::::::::::::ROW2:::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.fourButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="4",bg = "lavender", 
                                 command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column=0)
        
        self.fiveButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="5",bg = "lavender", 
                                 command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column=1)
        self.sixButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="6", bg = "lavender",
                                command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column=2)
        
        self.divideButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="/",
                                   command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2, column=3)
        
        self.percentageButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="%", 
                                       command=lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=2, column=4)
 #::::::::::::ROW3:::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.oneButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="1",bg = "lavender",
                                command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column=0)
        
        self.twoButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"), width=6,height=2,text="2", bg = "lavender",
                                command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column=1)
        
        self.threeButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="3", bg = "lavender",
                                  command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column=2)
        
        self.minusButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="-", 
                                  command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=3)
        
        self.plusButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="+",
                                   command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=3, column=4)
 #::::::::::::ROW4:::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.zeroButton = Button(self, pady=1,border=4,fg="black",bg = "lavender",font=("arial",20,"bold"),width=6,height=2,text="0",
                                 command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0)
        
        self.dotButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text=".", 
                                command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=4, column=1)
        
        self.equalsButton = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="=", 
                                 command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=4, column=4) 
        
        self.squd = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="Pi", 
                                command=lambda: self.sc())
        self.squd.grid(row=4, column=2)
        
        self.clear = Button(self, pady=1,border=4,fg="black",font=("arial",20,"bold"),width=6,height=2,text="C", 
                                 command=lambda: self.Clear_Entry())
        self.clear.grid(row=4, column=3)
        
        
app = Application(calculator).grid()
calculator.mainloop()
           