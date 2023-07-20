from customtkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3,bcrypt

x=50

conn=sqlite3.connect('user.db')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (Username TEXT NOT NULL, Password TEXT NOT NULL)')
#functionalty section#

def login_user():
    if usernamefram.get()=='' or passwordfram.get()=='':
        messagebox.showerror('ERROR','ALL FIELDS MUST BE FILLED')
    else:
        cursor.execute('SELECT password FROM users WHERE username=?',[usernamefram.get()])
        result_password=cursor.fetchone()
        if result_password:
            if bcrypt.checkpw(passwordfram.get().encode('UTF-8'),result_password[0]):
                messagebox.showinfo('SUCCESS','Logged in successfully')
                window.destroy()
                import data
            else:
                messagebox.showerror('ERROR','Invalid password')
        else:
            messagebox.showerror('ERROR','Invalid username')
            usernamefram.delete(0,END)
            passwordfram.delete(0,END)
            window.focus


def register_user():
    if usernamefram.get()=='' or passwordfram.get()=='':
        messagebox.showerror('ERROR','ALL FIELDS MUST BE FILLED')
    else:
        cursor.execute('SELECT username FROM users WHERE username=?',[usernamefram.get()])
        if cursor.fetchone() is not None:
            messagebox.showerror('ERROR','USERNAME ALREADY EXISTS')
        else:
            encode_password=passwordfram.get().encode('UTF-8')
            hashed_password=bcrypt.hashpw(encode_password,bcrypt.gensalt())
            cursor.execute('INSERT INTO users VALUES (?,?)',[usernamefram.get(),hashed_password])
            conn.commit()
            messagebox.showinfo('Success','Registration is successfull')
            move_right()
            usernamefram.delete(0,END)
            passwordfram.delete(0,END)
            window.focus()


def move_left():
    global x
    if x>50:
        x-=1
        topframe.place(x=x,y=10)
        topframe.after(1,move_left)


def move_right():
    global x
    if x<370:
        x+=1
        topframe.place(x=x,y=10)
        topframe.after(1,move_right)
    headinglabel.configure(text='Login')
    innerbu.configure(text='Login',command=login_user)


#GUI part#
window=CTk()
window.title('Login and Sign up page')
window.wm_geometry('+100+100')
mainfram=CTkFrame(window,fg_color='blue4',width=600,height=400)
mainfram.grid(row=0,column=0,padx=30,pady=30)
login=CTkButton(mainfram,text='Login',fg_color='blue4',font=('ariel',20,'bold'),border_color='blue2',border_width=1,
                hover_color='blue2',cursor='hand2',command=move_right)

login.place(x=430,y=300)

signup=CTkButton(mainfram,text='Sign Up',fg_color='blue4',font=('ariel',20,'bold'),border_color='blue2',border_width=1,
                hover_color='blue2',cursor='hand2',command=move_left)

signup.place(x=30,y=300)

topframe=CTkFrame(window,fg_color='White',width=350,height=400)
topframe.place(x=50,y=10)

logoimage=CTkImage(light_image=Image.open('login.png'),size=(80,80))
logolabel=CTkLabel(topframe,image=logoimage,text='')
logolabel.grid(row=0, column=0,pady=(20,0))

headinglabel=CTkLabel(topframe,text='Sign Up',font=('ariel',30,'bold'),text_color='blue4')
headinglabel.grid(row=1, column=0,pady=(20,0))

usernamefram=CTkEntry(topframe,font=('ariel',20,'bold'),width=200,height=30,placeholder_text='Username')
usernamefram.grid(row=2,column=0,padx=20,pady=(30,20))

passwordfram=CTkEntry(topframe,font=('ariel',20,'bold'),width=200,height=30,placeholder_text='Password',show='*')
passwordfram.grid(row=3,column=0,padx=20,pady=(0,20))

innerbu=CTkButton(topframe,text='Sign Up',fg_color='blue2',font=('ariel',20,'bold'),
                  hover_color='blue4',cursor='hand2',command=register_user)
innerbu.grid(row=4, column=0,pady=20)


window.mainloop()