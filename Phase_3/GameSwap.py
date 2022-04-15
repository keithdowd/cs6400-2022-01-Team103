from global_variables import cnx
from MainMenu import MainMenuObject
from sql import sql__gameswap__user_check
from sql import sql__gameswap__postalcode_check
from sql import sql__gameswap__getcitystate
from sql import sql__gameswap__phonenumber_check
from sql import sql__gameswap__user_password__check
from sql import sql__gameswap__user_email_phonenumber__check
from sql import sql__gameswap__email_fetch
import os
        #global emailtext
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkmacosx import Button
import pandas as pd
from functools import partial
from IPython.display import display






# creates a Tk() object
master = tk.Tk()
master.title("Login")
master.resizable(width=False, height=False)
#clickvalue=''
# sets the geometry of main
# root window
master.geometry("500x400")
def RegisterWindow():
    RegisterModule = Toplevel(master)
    RegisterModule.geometry("700x700")
    RegisterModule.resizable(width=False, height=False)
    RegisterModule.title("Registration")
    v = StringVar()
    p = StringVar()
    l_email = tk.Label(RegisterModule,  text="Email").place(x=40, y=5)
    EmailTtbx = tk.Entry(RegisterModule,borderwidth=1, relief="solid")
    EmailTtbx.place(width=242, height=35, x=40, y=25)
    l_nickname = tk.Label(RegisterModule, text="Nickname").place(x=340, y=5)
    NickNameTtbx = tk.Entry(RegisterModule,borderwidth=1, relief="solid")
    NickNameTtbx.place(width=242,height=35,x=340, y=25)
    l_password = Label(RegisterModule, text="Password").place(x=40, y=65)
    PasswordTtbx = Entry(RegisterModule,borderwidth=1, relief="solid")
    PasswordTtbx.place(width=242, height=35, x=40, y=85)
    l_city = Label(RegisterModule, text="City").place(x=340, y=65)
    CityTtbx = Label(RegisterModule, height=2, width=30,borderwidth=1, relief="solid")
    CityTtbx.place(x=340, y=85)
    l_firstName = Label(RegisterModule, text="First Name")
    l_firstName.place(x=40, y=125)
    FirstNameTtbx = Entry(RegisterModule, borderwidth=1, relief="solid")
    FirstNameTtbx.place(width=242,height=35,x=40, y=145)
    l_state = Label(RegisterModule, text="State").place(x=340, y=125)
    StateTtbx = Label(RegisterModule, height=2, width=30,borderwidth=1, relief="solid")
    StateTtbx.place(x=340, y=145)
    l_lastName = Label(RegisterModule, text="Last Name").place(x=40, y=185)
    LastNameTtbx = Entry(RegisterModule,borderwidth=1, relief="solid")
    LastNameTtbx.place(width=242,height=35,x=40, y=205)
    l_postalcode = Label(RegisterModule, text="Postal Code").place(x=340, y=185)
    PostalCodeTtbx = Entry(RegisterModule, borderwidth=1, relief="solid")
    PostalCodeTtbx.place(width=242,height=35,x=340, y=205)
    l_phno = Label(RegisterModule, text="Phone number (optional)").place(x=40, y=265)
    PhnoTtbx = Entry(RegisterModule, borderwidth=1, relief="solid")
    PhnoTtbx.place(width=242,height=35,x=40, y=285)
    cb1 = IntVar()
    phflgchckbox=Checkbutton(RegisterModule, text='Show the number in swaps',variable=cb1, onvalue=1, offvalue=0)
    phflgchckbox.place(x=40, y=325)


    RegisterModule.clicked = StringVar()
    RegisterModule.clicked.set("Select the phone type")
    option_Menu = StringVar(RegisterModule)
    options = [
        "Home",
        "Work",
        "Mobile"
            ]

    l_phno = Label(RegisterModule, text="Type").place(x=340, y=325)
    drop = OptionMenu(RegisterModule, option_Menu,"Home","Work", "Mobile")
    drop.place(x=340, y=350)
    #drop = OptionMenu(RegisterModule, clicked, "Home", "Work", "Mobile")
    label_error = Label(RegisterModule, foreground='red')
    label_error.place(x=170, y=350)
    postal_label_error = Label(RegisterModule, foreground='red')
    postal_label_error.place(x=170, y=380)
    phno_label_error = Label(RegisterModule, foreground='red')
    phno_label_error.place(x=170, y=400)
    Label(RegisterModule, textvariable=v).place(x=170, y=420)
    registration_complete_status = Label(RegisterModule, foreground='green')
    registration_complete_status['text'] = ''
    registration_complete_status.place(x=170, y=440)
    password_label_error = Label(RegisterModule, foreground='red')
    password_label_error.place(x=170, y=480)
    nickname_label_error = Label(RegisterModule, foreground='red')
    nickname_label_error.place(x=170, y=500)
    Label(RegisterModule, textvariable=p).place(x=170, y=520)

    def checkRegisterValidations():
        email_validated = 0
        password_validated = 0
        postal_validated = 0
        nickname_validated = 0
        phno_validated = 1
        registration_complete_status['text'] =''
        label_error['text'] = ''
        postal_label_error['text'] = ''
        phno_label_error['text'] = ''
        v.set(" ")
        p.set(" ")

        emailText = EmailTtbx.get()
        passwordText=PasswordTtbx.get()
        PostalText = PostalCodeTtbx.get()
        PhnoText = PhnoTtbx.get()
        NickNameText= NickNameTtbx.get()
        EmailTtbx.config(foreground="black")
        PasswordTtbx.config(foreground="black")
        display(emailText)
        display(PostalText)
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(email_pattern, emailText) is None or emailText == "":
             label_error['text'] = 'Please enter a valid email'
             EmailTtbx.config(foreground="red")
             email_validated = 0

        else:
             label_error['text'] = ''
             email_validated = 1

        login_fetch_query = sql__gameswap__user_check(emailText)
        user_data = []
        user_data = pd.read_sql_query(login_fetch_query, cnx)
        print("from sql file")
        print(sql__gameswap__user_check(emailText))

        if int(user_data['cnt']) == 1:
            #display(user_data['cnt'], "inside:")
             v.set("User Exists")
             email_validated = 0

        else:
              v.set(" ")
              email_validated = 1
        password_pattern = r'\b[A-Za-z0-9._%+-@]\b'
        if  passwordText == "":
            password_label_error['text'] = 'Please enter a valid password'
            password_validated = 0
        else:
            password_label_error['text'] =' '
            password_validated = 1
        if  NickNameText == "":
            nickname_label_error['text'] = 'Please enter a valid nickanme'
            nickname_validated = 0
        else:
            nickname_label_error['text'] =' '
            nickname_validated = 1

        if str.isdigit(PostalText) ==False or PostalText == "":
            postal_label_error['text'] = 'Please enter a valid postal code'
            PostalCodeTtbx.config(foreground="red")
            postal_validated = 0
        else:
            postal_label_error['text'] = ''
            PostalCodeTtbx.config(foreground="black")

            #postalcode_fetch_query = "Select count(1) cnt from   CS6400_spr22_team103.UserAddress where postalcode=  " + "'" + PostalText + "'"
            postalcode_fetch_query=sql__gameswap__postalcode_check(PostalText)
            sql__gameswap__postalcode_check(PostalText)
            postal_data = []
            postal_data = pd.read_sql_query(postalcode_fetch_query, cnx)

            if int(postal_data['cnt']) == 0 and PostalText !="" :
              postal_label_error['text'] = 'Please enter allowed postal code'
              PostalCodeTtbx.config(foreground="red")
              postal_validated = 0

            else:
                postal_label_error['text']=(" ")
                #postalcode_fetch_query = "Select addr_City,addr_State  from   CS6400_spr22_team103.UserAddress where postalcode=  " + "'" + PostalText + "'"
                postalcode_fetch_query=sql__gameswap__getcitystate(PostalText)
                postal_data = []
                postal_data = pd.read_sql_query(postalcode_fetch_query, cnx)
                display(postal_data['addr_City'])
                display(postal_data['addr_State'])
                CityTtbx['text']=str(postal_data['addr_City'][0])
                StateTtbx['text'] = str(postal_data['addr_State'][0])

                postal_validated = 1


            #r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phno_pattern = r'\b[0-9]{10,10}\b'
        if re.fullmatch(phno_pattern, PhnoText) is None and PhnoText != '' and PhnoText.find('-') ==-1  :
            #PhnoTtbx.delete(0, tk.END)
            #PhnoTtbx.insert(0, (format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1]))
            phno_label_error['text'] = 'Please enter a valid phono (enter 10 digits)'
            PhnoTtbx.config(foreground="red")
            phno_validated = 0
        else:
            if PhnoText != '':
              #phno_fetch_query = "Select count(1) cnt from  CS6400_spr22_team103.Phone where phone_number=  " + "'" + (format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1]) + "'"
              phnopass=(format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1])
              phno_fetch_query=sql__gameswap__phonenumber_check(phnopass)
              print(phno_fetch_query)
              phono_data = []
              phno_data = pd.read_sql_query(phno_fetch_query, cnx)
              if int(phno_data['cnt']) == 1:
                display(PhnoText)
                display(phno_data)
                display ((format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1]))
                display(phno_data['cnt'], "inside:phonenumber")
                p.set("Phone Number Exists")
                phno_validated = 0

              else:
                PhnoTtbx.delete(0, tk.END)
                PhnoTtbx.insert(0, (format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1]))
                phno_label_error['text'] = ''
                p.set(" ")
                PhnoTtbx.config(foreground="black")
                phno_validated = 1
        if password_validated==1 and email_validated==1 and postal_validated==1 and phno_validated==1 and nickname_validated==1:
            print("insert")
            #user_insert_status = pd.read_sql_query(register_user_query, cnx)
            display(PhnoTtbx.get())
            display(cb1.get())
            display(option_Menu.get())
            if PhnoTtbx.get() !='':
                register_phone_query ="insert into CS6400_spr22_team103.Phone (phone_number,phone_share,phone_type) values " + "('" + PhnoTtbx.get() + "','" + str(cb1.get()) + "','" + option_Menu.get() + "')"
                display(register_phone_query)
                #phone_insert_status = pd.read_sql_query(register_phone_query, cnx)
                mycursor = cnx.cursor()
                mycursor.execute(register_phone_query)
                cnx.commit()
                register_user_query = "insert into CS6400_spr22_team103.user (email,user_firstname,user_lastname,user_nickname,user_password,postalcode,phone_number) values " + "('" + emailText + "','" + FirstNameTtbx.get() + "','" + LastNameTtbx.get() + "','" + NickNameTtbx.get() + "','" + PasswordTtbx.get() + "','" + PostalText + "','" + PhnoTtbx.get() + "')"
                display(register_user_query)
                mycursor1 = cnx.cursor()
                mycursor1.execute(register_user_query)
                cnx.commit()
                mycursor.close()
            else:
               register_user_query = "insert into CS6400_spr22_team103.user (email,user_firstname,user_lastname,user_nickname,user_password,postalcode) values " + "('" + emailText + "','" + FirstNameTtbx.get() + "','" + LastNameTtbx.get() + "','" + NickNameTtbx.get() + "','" + PasswordTtbx.get() + "','" + PostalText + "')"
               display(register_user_query)
               mycursor = cnx.cursor()
               mycursor.execute(register_user_query)
               cnx.commit()
               mycursor.close()

            registration_complete_status['text'] = 'Registration complete.Kindly close the window and proceed to login'

        else:
            print(v)
            print("insert not done")


    Registerbtn1 = Button(RegisterModule,text="Register", bg='blue', fg='white', borderless=1,command=checkRegisterValidations).place(x=40,y=380)

global clickvalue


def quit(self):
    self.destroy()

label = Label(master,text="Sign In")
label.pack(pady=10)
l = Label(master, text="Email/Phone Number (enter phone number in xxx-xxx-xxxx)")
l.config(font=("Courier", 10))
l.pack()
#EmailTextbox=Text(master,height=2,width=30,borderwidth=1, relief="solid")
#EmailTextbox.pack(pady=20)
EmailTextbox = tk.Entry(master, borderwidth=1, relief="solid")
EmailTextbox.place(width=250,height=35,x=125,y=75)


l = Label(master, text="Password")
l.config(font=("Courier", 10))
l.place(x=220,y=150)
PasswordTextBox = tk.Entry(master,show="*", borderwidth=1, relief="solid")
PasswordTextBox.place(width=250,height=35,x=125,y=180)
#PasswordTextBox.pack(pady=20)
master.v=StringVar()
Label(master, textvariable=master.v).place(x=170,y=350)
master.p=StringVar()
password_label=Label(master, textvariable=master.p).place(x=170,y=370)


def checkUserExists():

   master.v.set(" ")
   master.p.set(" ")
   emailText_fetch_query=sql__gameswap__email_fetch(EmailTextbox.get())
   emailText_data = []
   emailText_data = pd.read_sql_query(emailText_fetch_query, cnx)
   emailtext=emailText_data['email'][0]
   EmailTextbox.config(foreground="black")
   PasswordTextBox.config(foreground="black")
   display(emailtext)
   pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

   ''' if re.fullmatch(pattern, emailText) is None:
       master.v.set("Please enter a valid email")
       #master.label_error['text'] = 'Please enter a valid email'
       EmailTextbox.config(foreground ="red")
'''

   #    master.v.set("Please enter a valid email")
       #master.label_error['text'] = ''
   #login_fetch_query="Select email,phone_number,count(1) cnt from  CS6400_spr22_team103.user where email=  " + "'" + EmailTextbox.get()+ "' or phone_number=  " + "'" + EmailTextbox.get()+ "' group by email,phone_number"
   login_fetch_query=sql__gameswap__user_email_phonenumber__check(EmailTextbox.get())
   user_data = []
   user_data = pd.read_sql_query(login_fetch_query, cnx)
   display(user_data['cnt'])
   if user_data['cnt'].empty == False:
    if int(user_data['cnt'][0]) == 1:
      master.v.set(" ")

    else:
           master.v.set("User Not Exists")
   else:
           master.v.set("User Not Exists")

   #password_fetch_query = "Select count(1) cnt from  CS6400_spr22_team103.user where user_password=  " + "'" + PasswordTextBox.get() + "' and email="  + "'" + EmailTextbox.get()+  "' or phone_number=  " + "'" + EmailTextbox.get()+ "'"
   password_fetch_query=sql__gameswap__user_password__check(EmailTextbox.get(),PasswordTextBox.get())
   pwd_data = []
   pwd_data = pd.read_sql_query(password_fetch_query, cnx)
   display(pwd_data['cnt'])
   display(password_fetch_query)

   if int(pwd_data['cnt'][0]) == 1:

       #global_variables.email_text = emailText
       master.destroy()
       MainMenuObject(emailtext)
       master.v.set("Login successful")
       #master.e=getemail()
       master.destroy()

   else:
       #master.password_error['text'] = ''
             PasswordTextBox.config(foreground="red")
             master.p.set("Incorrect Password")






Loginbtn = Button(master,
             text="Login", bg='blue',fg='white', borderless=1,command=checkUserExists)
Loginbtn.place(x=200,y=240)
#Loginbtn.pack(pady=10)
Registerbtn = Button(master,
             text="Register", bg='blue',fg='white', borderless=1, command=RegisterWindow)
Registerbtn.place(x=200,y=300)
#Registerbtn.pack(pady=10)
#master.label_error = Label(master, foreground='red')
#master.label_error.place(x=170,y=350)

#label = Label(master,text=" ")
#label.pack(pady=10)
mainloop()
cnx.close()


