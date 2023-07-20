from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#Function Section#

def exit():
    work=messagebox.askyesno('Confirm','Are you sure you want exit')
    if work:
        pea.destroy()
    else:
        pass

def export():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=table.get_children()
    newlist=[]
    for index in indexing:
        content=table.item(index)
        datalist=content['values']
        newlist.append(datalist)

    tab=pandas.DataFrame(newlist,columns=('Id','Expenses','Quantity','Type','Cost','Purchaser'))
    tab.to_csv(url,index=False)
    messagebox.showinfo('SUCCESS','Data is saved successfully')
def edit():
    def editdata():
        query= 'update expenses set expenses=%s, quantity=%s, type=%s, cost=%s , purchaser=%s where Id=%s'
        mycursor.execute(query,(expenent.get(),quaent.get(),tyent.get(),coent.get(),coent.get(),ident.get()))
        con.commit()
        messagebox.showinfo('SUCCESS',f'Id {ident.get()} is modified successfully',parent=editwind)
        editwind.destroy()
        display()
    editwind = Toplevel()
    editwind.resizable(0, 0)
    editwind.grab_set()
    editwind.title('EDIT INFORMATION')
    idleb = Label(editwind, text='Id', font=('time new roman', 20,))
    idleb.grid(row=0, column=0, sticky=W)
    ident = Entry(editwind, font=('time new roman', 20))
    ident.grid(row=0, column=1, padx=20, pady=20)
    expenleb = Label(editwind, text='Expense', font=('time new roman', 20,))
    expenleb.grid(row=1, column=0, sticky=W)
    expenent = Entry(editwind, font=('time new roman', 20))
    expenent.grid(row=1, column=1, padx=20, pady=20)
    quatleb = Label(editwind, text='Quantity', font=('time new roman', 20,))
    quatleb.grid(row=2, column=0, sticky=W)
    quaent = Entry(editwind, font=('time new roman', 20))
    quaent.grid(row=2, column=1, padx=20, pady=20)
    typeleb = Label(editwind, text='Type', font=('time new roman', 20,))
    typeleb.grid(row=3, column=0, sticky=W)
    tyent = Entry(editwind, font=('time new roman', 20))
    tyent.grid(row=3, column=1, padx=20, pady=20)
    coleb = Label(editwind, text='Cost', font=('time new roman', 20,))
    coleb.grid(row=4, column=0, sticky=W)
    coent = Entry(editwind, font=('time new roman', 20))
    coent.grid(row=4, column=1, padx=20, pady=20)
    naleb = Label(editwind, text='Purchaser Name', font=('time new roman', 20,))
    naleb.grid(row=5, column=0, sticky=W)
    naent = Entry(editwind, font=('time new roman', 20))
    naent.grid(row=5, column=1, padx=20, pady=20)
    but = ttk.Button(editwind, text='EDIT DATA',command=editdata)
    but.grid(row=6, column=2, pady=20)

    indexing=table.focus()
    print(indexing)
    content=table.item(indexing)
    listdata=content['values']
    ident.insert(0,listdata[0])
    expenent.insert(0,listdata[1])
    quaent.insert(0,listdata[2])
    tyent.insert(0,listdata[3])
    coent.insert(0,listdata[4])
    naent.insert(0,listdata[5])

def display():
    query = 'select *from expenses'
    mycursor.execute(query)
    fetch = mycursor.fetchall()
    table.delete(*table.get_children())
    for data in fetch:
        table.insert('', END, values=data)
def delete():
    indexing=table.focus()
    print(indexing)
    content=table.item(indexing)
    content_id=content['values'][0]
    query='delete from expenses where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'This Id {content_id} is deleted succesfully')
    query='select *from expenses'
    mycursor.execute(query)
    fetch=mycursor.fetchall()
    table.delete(*table.get_children())
    for data in fetch:
        table.insert('',END,values=data)
def search():
    def seardata():
        query='select *from expenses where id=%s or expenses=%s or quantity=%s or type=%s or cost=%s or purchaser=%s'
        mycursor.execute(query,(ident.get(),expenent.get(),quaent.get(),tyent.get(),coent.get(),naent.get()))
        table.delete(*table.get_children())
        fetch=mycursor.fetchall()
        for data in fetch:
            table.insert('',END,values=data)
    searchwind=Toplevel()
    searchwind.resizable(0,0)
    searchwind.grab_set()
    searchwind.title('SEARCH INFORMATION')
    idleb=Label(searchwind,text='Id',font=('time new roman',20,))
    idleb.grid(row=0,column=0,sticky=W)
    ident=Entry(searchwind,font=('time new roman',20))
    ident.grid(row=0,column=1,padx=20,pady=20)
    expenleb = Label(searchwind, text='Expense', font=('time new roman', 20,))
    expenleb.grid(row=1, column=0,sticky=W)
    expenent = Entry(searchwind, font=('time new roman', 20))
    expenent.grid(row=1, column=1, padx=20, pady=20)
    quatleb = Label(searchwind, text='Quantity', font=('time new roman', 20,))
    quatleb.grid(row=2, column=0,sticky=W)
    quaent = Entry(searchwind, font=('time new roman', 20))
    quaent.grid(row=2, column=1, padx=20, pady=20)
    typeleb = Label(searchwind, text='Type', font=('time new roman', 20,))
    typeleb.grid(row=3, column=0,sticky=W)
    tyent = Entry(searchwind, font=('time new roman', 20))
    tyent.grid(row=3, column=1, padx=20, pady=20)
    coleb = Label(searchwind, text='Cost', font=('time new roman', 20,))
    coleb.grid(row=4, column=0, sticky=W)
    coent = Entry(searchwind, font=('time new roman', 20))
    coent.grid(row=4, column=1, padx=20, pady=20)
    naleb = Label(searchwind, text='Purchaser Name', font=('time new roman', 20,))
    naleb.grid(row=5, column=0,sticky=W)
    naent = Entry(searchwind, font=('time new roman', 20))
    naent.grid(row=5, column=1, padx=20, pady=20)
    but = ttk.Button(searchwind, text='SEARCH FOR INFO',command=seardata)
    but.grid(row=6, column=2, pady=20)

def add():
    def add_infor():
        if ident.get() == '' or expenent.get() == '' or quaent.get() == '' or tyent.get() == '' or coent.get()== '' or naent.get() == '':
            messagebox.showerror('ERROR', 'Must fill every space!!', parent=addewind)
        else:
            query = 'insert into expenses values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(ident.get(), expenent.get(), quaent.get(), tyent.get(),coent.get(), naent.get()))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want add this data in yr database?',parent=addewind)
            if result:
                ident.delete(0, END)
                expenent.delete(0, END)
                quaent.delete(0, END)
                tyent.delete(0, END)
                coent.delete(0, END)
                naent.delete(0, END)
            else:
                pass
            query='select *from expenses'
            mycursor.execute(query)
            fetch=mycursor.fetchall()
            table.delete(*table.get_children())
            for data in fetch:
                datalist=list(data)
                table.insert('',END,values=datalist)

    addewind=Toplevel()
    addewind.resizable(0,0)
    addewind.grab_set()
    addewind.title('ADD IN INFORMATION')
    idleb=Label(addewind,text='Id',font=('time new roman',20,))
    idleb.grid(row=0,column=0,sticky=W)
    ident=Entry(addewind,font=('time new roman',20))
    ident.grid(row=0,column=1,padx=20,pady=20)
    expenleb = Label(addewind, text='Expense', font=('time new roman', 20,))
    expenleb.grid(row=1, column=0,sticky=W)
    expenent = Entry(addewind, font=('time new roman', 20))
    expenent.grid(row=1, column=1, padx=20, pady=20)
    quatleb = Label(addewind, text='Quantity', font=('time new roman', 20,))
    quatleb.grid(row=2, column=0,sticky=W)
    quaent = Entry(addewind, font=('time new roman', 20))
    quaent.grid(row=2, column=1, padx=20, pady=20)
    typeleb = Label(addewind, text='Type', font=('time new roman', 20,))
    typeleb.grid(row=3, column=0,sticky=W)
    tyent = Entry(addewind, font=('time new roman', 20))
    tyent.grid(row=3, column=1, padx=20, pady=20)
    coleb = Label(addewind, text='Cost', font=('time new roman', 20,))
    coleb.grid(row=4, column=0, sticky=W)
    coent = Entry(addewind, font=('time new roman', 20))
    coent.grid(row=4, column=1, padx=20, pady=20)
    naleb = Label(addewind, text='Purchaser Name', font=('time new roman', 20,))
    naleb.grid(row=5, column=0,sticky=W)
    naent = Entry(addewind, font=('time new roman', 20))
    naent.grid(row=5, column=1, padx=20, pady=20)
    but = ttk.Button(addewind, text='INSERT IN INFO',command=add_infor)
    but.grid(row=6, column=2, pady=20)

def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host=enhost.get(), user=enus.get(), password=enpas.get(),database='producationexpenses')
            mycursor= con.cursor()
            messagebox.showinfo('Successful', 'Database connection successful', parent=window)
            addbu.config(state=NORMAL)
            Edibu.config(state=NORMAL)
            delbu.config(state=NORMAL)
            disbu.config(state=NORMAL)
            seabu.config(state=NORMAL)
            exbu.config(state=NORMAL)
            exibu.config(state=NORMAL)
        except:
            messagebox.showerror('Error', 'Invaild input',parent=window)
        query='create database producationexpenses'
        mycursor.execute(query)
        query= 'use producationexpenses'
        mycursor.execute(query)
        query= 'create table expenses(ID varchar(20) not null primary key, EXPENSES varchar(30) , QUANTITY varchar(10),' \
            'TYPE varchar(30),COST int(10), PURCHASER varchar(30))'
        mycursor.execute(query)

    window=Toplevel()
    window.grab_set()
    window.geometry('400x200+500+150')
    window.title('Connect to database')
    window.resizable(False,False)
    usna= Label(window,text='User Name',font=('time new roman',16))
    usna.grid(row=2, column=0,pady=12, padx=8)
    enus= Entry(window,font=('time new roman',16))
    enus.grid(row=2,column=1)
    honam= Label(window,text='Host Name',font=('time new roman',16))
    honam.grid(row=1,column=0,pady=12, padx=8)
    enhost=Entry(window,font=('time new roman',16))
    enhost.grid(row=1, column=1,pady=12, padx=8)
    paswo= Label(window,text='Password',font=('time new roman',16))
    paswo.grid(row=3, column=0,pady=12,padx=8)
    enpas= Entry(window,font=('time new roman',16),show='*')
    enpas.grid(row=3,column=1,pady=12,padx=8)
    but = ttk.Button(window,text='Connect',command=connect)
    but.grid(row=4,column=0, columnspan=2)




pea = ttkthemes.ThemedTk()

pea.get_themes()

pea.set_theme('adapta')

pea.geometry('1000x500+0+0')
pea.title('Producation expenses ')

connectbutton = ttk.Button(pea, text='Connect Database', command=connect_database)
connectbutton.place(x=1090,y=20)


leftfram= Frame(pea)
leftfram.place(x=30, y=80, width=400, height=600)
ima = PhotoImage(file='production (1).png')

imafra= Label(leftfram,image=ima)
imafra.grid(row=0,column=0)

addbu = ttk.Button(leftfram,text='Input data',state=DISABLED,command=add)
addbu.grid(row=1, column=0,pady=10)

Edibu = ttk.Button(leftfram,text='Edit data',state=DISABLED,command=edit)
Edibu.grid(row=2, column=0,pady=10)

delbu = ttk.Button(leftfram,text='Delete data',state=DISABLED,command=delete)
delbu.grid(row=3, column=0,pady=10)

disbu = ttk.Button(leftfram, text='Display data',state=DISABLED,command=display)
disbu.grid(row=4, column=0, pady=10)

seabu = ttk.Button(leftfram, text='Search data',state=DISABLED,command=search)
seabu.grid(row=5, column=0, pady=10)

exbu = ttk.Button(leftfram, text='Export data',state=DISABLED,command=export)
exbu.grid(row=6, column=0, pady=10)

exibu = ttk.Button(leftfram,text='Exit',state=DISABLED,command=exit)
exibu.grid(row=7,column=0)



rightfram =Frame(pea)
rightfram.place(x=280,y=80, width=800, height=555)

srollx= Scrollbar(rightfram,orient=HORIZONTAL)
srolly= Scrollbar(rightfram,orient=VERTICAL)

table=ttk.Treeview(rightfram,columns=('Id','Expenses','Quantity','Quality','Cost','Purchaser'),
                   xscrollcommand=srollx.set,yscrollcommand=srolly.set)
srollx.config(command=table.xview)
srolly.config(command=table.yview)

table.heading('Id', text='ID')
table.heading('Expenses', text='EXPENSES')
table.heading('Quantity', text='QUANTITY')
table.heading('Quality', text='TYPE')
table.heading('Cost', text='COST')
table.heading('Purchaser', text='PURCHASER NAME')

Style=ttk.Style()
Style.configure ('Treeview', rowheight=40, font=('arial',15,'bold'),foreground='red4',bg='white',fieldbackground='white')
Style.configure('Treeview.Heading',font=('time new romana',12))

table.config(show='headings')

srollx.pack(side=BOTTOM, fill=X)
srolly.pack(side=RIGHT, fill=Y)

table.pack()





pea.mainloop()