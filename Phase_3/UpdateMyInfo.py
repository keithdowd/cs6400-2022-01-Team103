import tkinter as tk
from tkinter import *
import global_variables

from tkinter import ttk
from tkmacosx import Button
import pandas as pd
from functools import partial

from IPython.display import display
import mysql.connector

cnx = mysql.connector.connect(user='team103', password='gatech123',
                             host='127.0.0.1',
                              database='CS6400_spr22_team103')
import pandas as pd

# creates a Tk() object
master = Tk()
master.title("Login")
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