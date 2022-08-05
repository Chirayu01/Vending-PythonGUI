from tkinter import*
from tkinter import ttk,messagebox
root = Tk()
root.title("Vending Machine")
root.geometry("900x700")
root.resizable(False,False)
 
default = ['My Vending Machine','BILL','',['ITEM','QNTY','PRICE','VALUE\n']]
selected = {}
money = 0
total = 0
 
# HELPER FUNCTIONS
def onQuantityChange(index,value,op):
    # if quantity becomes 0 delete the item from the receipt
    if quantity.get() == 0:
        name = selected_name.cget('text')
        if name:
            del selected[name]
    # update the receipt
    resetReciept()
    
 
# called in inserting money
def insertMoney(val):
    global money
    money += val
    # display total money inserted
    totalMoney.config(text='Money Inserted:  '+str(money)+'円')
    # update receipt
    resetReciept()
                     
# called in selecting any product
def selectProduct(product,recFeild):
    # resset all product buttons background color
    # blue -> currently selected item
    # green -> this item is already on the ordered list
    # #f5b507 -> this item is not ordered
    
    for button in allProducts:
        if button .cget('bg') == 'blue' and button == product:
            return
        if button.cget('bg') == 'blue':
            name,price = button.cget('text').split('=')
            if name in selected.keys():
                if selected[name][1] >=1:
                    button.config(bg='green')
                    break
            button.config(bg='#f5b507')
            
    name,price = product.cget('text').split('=')
    product.config(bg='blue')
    selected_name.config(text=name)
        
    if name in selected.keys():
        selected_price.config(text=selected[name][2])
        quantity.set(selected[name][1])
    else:
        selected[name] = [name,1,price,price]
        quantity.set(1)
    
def resetReciept():
    global money,total
    receipt.config(state='normal')
    receipt.delete('1.0',END)
    qnt = 0
    total = 0
    for text in default:
        if isinstance(text,str):
            receipt.insert(END,text.center(40,' '))
        else:
            receipt.insert(END,text[0].center(20,' '))
            receipt.insert(END,text[1].center(4,' '))
            receipt.insert(END,text[2].center(8,' '))
            receipt.insert(END,text[3].center(7,' '))
    if selected:
        name = selected_name.cget('text')
        if quantity.get() != selected[name][1] and name in selected.keys():
            selected[name][1] = quantity.get()
        
        for k,v in selected.items():
            qnt += v[1]
            price = int(v[2].replace('円',''))
            value = v[1]*price
            total += value
            receipt.insert(END,f'{v[0]:<20}')
            receipt.insert(END,str(v[1]).center(4,' '))
            receipt.insert(END,v[2].center(8,' '))
            receipt.insert(END,f'{value:>4}円\n')
        receipt.insert(END,'\n')
        
        receipt.insert(END,'{:<20}'.format('TOTAL'))
        receipt.insert(END,str(qnt).center(4,' '))
        receipt.insert(END,f'{total:>13}円\n')
 
        receipt.insert(END,'{:<20}'.format('MONEY'))
        receipt.insert(END,f'{money:>17}円\n')
 
        change = money-total
        receipt.insert(END,'{:<20}'.format('CHANGE'))
        if change >=0:
            receipt.insert(END,f'{change:>17}円\n')
        else:
            receipt.insert(END,'{:>17}円\n'.format('0'))
        cancel.config(state = 'normal')
        ok.config(state = 'normal')
    else:
        ok.config(state = 'disabled')
        cancel.config(state = 'disabled')
    receipt.config(state='disabled')
         
 
def cancelOrder():
    global selected,money,total,allProducts
    can = messagebox.askquestion('キャンセル','キャンセルでよろしですか？?')
    
    if can == 'yes':
        selected = {}
        
        total = 0
        for button in allProducts:
            button.config(bg='#f5b507')
        totalMoney.config(text='入金額は:  0円')
        selected_price.config(text='')
        selected_name.config(text='')
        quantity.set(0)
        resetReciept()
        if money:
            messagebox.showinfo('キャンセル','お金をお取りください')
            money = 0
        else:
            messagebox.showinfo('キャンセル','オーダーキャンセルされました')
 
def submitOrder():
    global money,total,selected
    if money < total:
        messagebox.showerror('お金','入金額が足りません ! ')
        return
    else:
        for button in allProducts:
            button.config(bg='#f5b507')
        messagebox.showinfo('購入完了','商品をお取りください')
        selected_price.config(text='')
        selected_name.config(text='')
        quantity.set(0)
        money = 0
        total = 0
        selected = {}
        totalMoney.config(text='入金額:  0円')
        resetReciept()
           
        
        
 
 
Label(root,text="Welcome To Vending Machine",font=("algerian", 15,"bold"),bg = "cyan",border=8,width=30).pack(pady=10)
 
 
mugicya = Button(root,pady=1,border=2,activebackground="#FF0000",fg="black",bg = "#f5b507",font=("Ink Free",20,"bold"),width=16,height=2,text = "麦茶=110円")
lemontea = Button(root,pady=1,border=2,activebackground="#FF0000",fg="black",bg = "#f5b507",font=("Ink Free",20,"bold"),width=16,height=2,text = "レモンティー=130円")
ryoku = Button(root,pady=1,border=2,activebackground="#FF0000",fg="black",bg = "#f5b507",font=("Ink Free",20,"bold"),width=16,height=2,text = "緑茶=120円")
macha = Button(root,pady=1,border=2,activebackground="#FF0000",fg="black",bg = "#f5b507",font=("Ink Free",20,"bold"),width=22,height=2,text = "抹茶=120円")
royal = Button(root,pady=1,border=2,activebackground="#FF0000",fg="black",bg = "#f5b507",font=("Ink Free",20,"bold"),width=22,height=2,text = "ローヤルミルクテイ－=150円")
 
allProducts = [mugicya,lemontea,ryoku,macha,royal]
receipt = Text(root,width = 40,height=15)
receipt.place(x=550,y=350)
 
mugicya.place(x=20,y=100)
lemontea.place(x=310,y=100)
ryoku.place(x=600,y=100)
macha.place(x=60,y=210)
royal.place(x=460,y=210)
 
 
 
mugicya.config(command = lambda :selectProduct(mugicya,None))
lemontea.config(command = lambda :selectProduct(lemontea,None))
royal.config(command = lambda :selectProduct(royal,None))
ryoku.config(command = lambda :selectProduct(ryoku,None))
macha.config(command = lambda :selectProduct(macha,None))
 
quantity = IntVar()
quantity.trace('w',onQuantityChange)
Label(root, pady=1,border=1,fg="black",font=("arial",15,"bold"),width=12,height=1,text = "商品名").place(x=20,y=350)
Label(root, pady=1,border=1,fg="black",font=("arial",15,"bold"),width=8,height=1,text = "金額").place(x=220,y=350)
Label(root, pady=1,border=1,fg="black",font=("arial",15,"bold"),width=6,height=1,text = "数").place(x=360,y=350)
 
selected_name = Label(root, pady=1,border=1,fg="green",font=("arial",15,"bold"),width=12,height=1,text = "麦茶")
selected_price = Label(root, pady=1,border=1,fg="green",font=("arial",15,"bold"),width=12,height=1,text = "110円")
selected_quantity = ttk.Combobox(root, values=[str(x) for x in range(0, 10)], width=6, height=1, textvariable=quantity)
selected_name.place(x=20,y=400)
selected_price.place(x=200,y=400)
selected_quantity.place(x=360,y=408)
 
 
Label(root, pady=1,border=1,fg="black",font=("arial",20,"bold"),width=12,height=1,text = "入金").place(x=200,y=480)
 
money10 = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#FF0000",font=("Ink Free",20,"bold"),width=5,height=1,text = "10円",command=lambda:insertMoney(10))
money50 = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#FF0000",font=("Ink Free",20,"bold"),width=5,height=1,text = "50円",command=lambda:insertMoney(50))
money100 = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#FF0000",font=("Ink Free",20,"bold"),width=5,height=1,text = "100円",command=lambda:insertMoney(100))
money500 = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#FF0000",font=("Ink Free",20,"bold"),width=5,height=1,text = "500円",command=lambda:insertMoney(500))
money1000 = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#FF0000",font=("Ink Free",20,"bold"),width=5,height=1,text = "1000円",command=lambda:insertMoney(1000))
totalMoney = Label(root, pady=1,border=1,fg="black",font=("arial",16,"bold"),width=20,height=1,text = "入金額:  0円")
totalMoney.place(x=180,y=630)
money10.place(x=20,y=550)
money50.place(x=120,y=550)
money100.place(x=220,y=550)
money500.place(x=320,y=550)
money1000.place(x=420,y=550)
 
 
ok = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#00FF00",font=("Ink Free",20,"bold"),width=5,height=1,text = "OK",command=submitOrder)
 
cancel = Button(root,border=2,activebackground="#FF0000",fg="black",bg = "#FF0000",font=("Ink Free",20,"bold"),width=5,height=1,text = "Cancel",command=cancelOrder)
 
cancel.place(x=600,y=620)
ok.place(x=750,y=620)
 
 
resetReciept()
root.mainloop()