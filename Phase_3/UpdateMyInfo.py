import tkinter as tk
from tkinter import *
from tkmacosx import Button
import pandas as pd
from functools import partial
from IPython.display import display
import mysql.connector
from global_variables import *
from sql import *
import pandas as pd
import re


def update_my_info(userEmail):

    # creates a Tk() object
    window = Tk()
    window.title("Update My Info")
    window.resizable(width=False, height=False)
    window.geometry("500x400")
    #clickvalue=''
    # sets the geometry of main
    # root window
    
    nickname_pulled=[]
    zip_pulled=[]
    city_pulled=[]
    first_name_pulled=[]
    state_pulled=[]
    last_name_pulled=[]
    phone_pulled=[]

    zip_pulled= pd.read_sql_query(sql__pull_zip(userEmail), cnx)
    zip_txt=zip_pulled['postalcode'][0]

    nickname_pulled= pd.read_sql_query(sql__pull_nick(userEmail), cnx)
    nickname_txt = nickname_pulled['user_nickname'][0]

    city_pulled= pd.read_sql_query(sql__pull_city(zip_txt), cnx)
    city_text = city_pulled['addr_city'][0]

    first_name_pulled= pd.read_sql_query(sql__pull_first_name(userEmail), cnx)
    first_name_txt = first_name_pulled['user_firstname'][0]

    state_pulled= pd.read_sql_query(sql__pull_state(zip_txt), cnx)
    state_txt = state_pulled['addr_state'][0]

    last_name_pulled= pd.read_sql_query(sql__pull_nick(userEmail), cnx)
    last_name_txt=last_name_pulled['user_lastname'][0]

    phone_pulled= pd.read_sql_query(sql__pull_nick(userEmail), cnx)
    phone_txt=phone_pulled['user_phone_number'][0]

    update_module = window
    update_module.geometry("700x700")
    update_module.resizable(width=False, height=False)
    update_module.title("Update My Info")
    v = StringVar()
    p = StringVar()
    l_email = tk.Label(update_module,  text="Email").place(x=40, y=5)
    EmailTtbx = tk.Entry(update_module,borderwidth=1, relief="solid")
    EmailTtbx.place(width=242, height=35, x=40, y=25)
    EmailTtbx.insert('end',userEmail)
    EmailTtbx.configure(state=DISABLED)
    
    l_nickname = tk.Label(update_module, text="Nickname").place(x=340, y=5)
    NickNameTtbx = tk.Entry(update_module,borderwidth=1, relief="solid")
    NickNameTtbx.insert('end',nickname_txt)
    NickNameTtbx.place(width=242,height=35,x=340, y=25)
    l_password = Label(update_module, text="Password").place(x=40, y=65)
    PasswordTtbx = Entry(update_module,borderwidth=1, relief="solid")
    PasswordTtbx.place(width=242, height=35, x=40, y=85)
    l_city = Label(update_module, text="City").place(x=340, y=65)
    CityTtbx = Entry(update_module,borderwidth=1, relief="solid")
    CityTtbx.insert('end',city_text)
    CityTtbx.place(x=340, y=85,height=35,width=242)
    l_firstName = Label(update_module, text="First Name").place(x=40,y=125)
    FirstNameTtbx = Entry(update_module, borderwidth=1, relief="solid")
    FirstNameTtbx.insert('end',first_name_txt)
    FirstNameTtbx.place(width=242,height=35,x=40, y=145)
    l_state = Label(update_module, text="State").place(x=340, y=125)
    StateTtbx = Entry(update_module,borderwidth=1, relief="solid")
    StateTtbx.insert('end',state_txt)
    StateTtbx.place(x=340, y=145,height=35,width=242)
    l_lastName = Label(update_module, text="Last Name").place(x=40, y=185)
    LastNameTtbx = Entry(update_module,borderwidth=1, relief="solid")
    LastNameTtbx.insert('end',last_name_txt)
    LastNameTtbx.place(width=242,height=35,x=40, y=205)
    l_postalcode = Label(update_module, text="Postal Code").place(x=340, y=185)
    PostalCodeTtbx = Entry(update_module, borderwidth=1, relief="solid")
    PostalCodeTtbx.insert('end',zip_txt)
    PostalCodeTtbx.place(width=242,height=35,x=340, y=205)
    l_phno = Label(update_module, text="Phone number (optional)").place(x=40, y=265)
    PhnoTtbx = Entry(update_module, borderwidth=1, relief="solid")
    PhnoTtbx.insert('end',phone_txt)
    PhnoTtbx.place(width=242,height=35,x=40, y=285)
    cb1 = IntVar()
    phflgchckbox=Checkbutton(update_module, text='Show the number in swaps',variable=cb1, onvalue=1, offvalue=0)
    phflgchckbox.place(x=40, y=325)

    update_module.clicked = StringVar()
    update_module.clicked.set("Select the phone type")
    option_Menu = StringVar(update_module)
    options = [
        "Home",
        "Work",
        "Mobile"
            ]

    l_phno = Label(update_module, text="Type").place(x=340, y=325)
    drop = OptionMenu(update_module, option_Menu,"Home","Work", "Mobile")
    drop.place(x=340, y=350)

    label_error = Label(update_module, foreground='red')
    label_error.place(x=170, y=350)
    postal_label_error = Label(update_module, foreground='red')
    postal_label_error.place(x=170, y=380)
    phno_label_error = Label(update_module, foreground='red')
    phno_label_error.place(x=170, y=400)
    Label(update_module, textvariable=v).place(x=170, y=420)
    registration_complete_status = Label(update_module, foreground='green')
    registration_complete_status['text'] = ''
    registration_complete_status.place(x=170, y=440)
    password_label_error = Label(update_module, foreground='red')
    password_label_error.place(x=170, y=480)
    nickname_label_error = Label(update_module, foreground='red')
    nickname_label_error.place(x=170, y=500)
    Label(update_module, textvariable=p).place(x=170, y=520)

    def validate_update():
        email_validated = 1
        password_validated = 0
        postal_validated = 0
        nickname_validated = 0
        phone_validated = 1
        registration_complete_status['text'] =''
        label_error['text'] = ''
        postal_label_error['text'] = ''
        phno_label_error['text'] = ''
        v.set(" ")
        p.set(" ")

        emailText = userEmail
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
        data={'cnt':[1]}
        user_data = pd.DataFrame(data)
        user_data = pd.read_sql_query(login_fetch_query, cnx)
        # user_data['cnt']=1
        
        # print("from sql file")
        # print(sql__gameswap__user_check(emailText))
        
        # if int(user_data['cnt']) == 1:
        #     #display(user_data['cnt'], "inside:")
        #      v.set("User Exists")
        #      email_validated = 0

        # else:
        #       v.set(" ")
        #       email_validated = 1
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
            phno_label_error['text'] = 'Please enter a valid phone number (enter 10 digits)'
            PhnoTtbx.config(foreground="red")
            phone_validated = 0
        else:
            if PhnoText != '':
              #phno_fetch_query = "Select count(1) cnt from  CS6400_spr22_team103.Phone where phone_number=  " + "'" + (format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1]) + "'"
              if PhnoText.find('-') ==-1:
                  phnopass=(format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1])
              else:
                  phnopass = PhnoText
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
                phone_validated = 0

              else:
                PhnoTtbx.delete(0, tk.END)
                PhnoTtbx.insert(0, (format(int(PhnoText[:-1]), ",").replace(",", "-") + PhnoText[-1]))
                phno_label_error['text'] = ''
                p.set(" ")
                PhnoTtbx.config(foreground="black")
                phone_validated = 1
        if password_validated==1 and email_validated==1 and postal_validated==1 and phone_validated==1 and nickname_validated==1:
            print("insert")
            user_insert_status = pd.read_sql_query(register_user_query, cnx)
            display(PhnoTtbx.get())
            display(cb1.get())
            display(option_Menu.get())
            if PhnoTtbx.get() !='':
                register_phone_query ="insert into CS6400_spr22_team103.Phone (phone_number,phone_share,phone_type) values " + "('" + PhnoTtbx.get() + "','" + str(cb1.get()) + "','" + option_Menu.get() + "')"
                display(register_phone_query)
                phone_insert_status = pd.read_sql_query(register_phone_query, cnx)
                mycursor = cnx.cursor()
                mycursor.execute(register_phone_query)
                cnx.commit()
                update_query = "update CS6400_spr22_team103.user set user_firstname="+FirstNameTtbx.get()+",user_lastname="+LastNameTtbx.get()+",user_nickname="+NickNameTtbx.get()+",user_password="+PasswordTtbx.get()+",postalcode="+PostalText+",phone_number="+PhnoTtbx.get()+" where email="+userEmail
                display(update_query)
                mycursor1 = cnx.cursor()
                mycursor1.execute(update_query)
                cnx.commit()
                mycursor.close()
            else:
                register_user_query = "update CS6400_spr22_team103.user set user_firstname="+FirstNameTtbx.get()+",user_lastname="+LastNameTtbx.get()+",user_nickname="+NickNameTtbx.get()+",user_password="+PasswordTtbx.get()+",postalcode="+PostalText+",phone_number="+PhnoTtbx.get()+" where email="+userEmail
                display(update_query)
                mycursor = cnx.cursor()
                mycursor.execute(update_query)
                cnx.commit()
                mycursor.close()

            registration_complete_status['text'] = 'Update complete. Kindly close the window and proceed to login'

        else:
            print(v)
            print("insert not done")

    Registerbtn1 = Button(update_module,text="Update", bg='blue', fg='white', borderless=1,command=validate_update).place(x=40,y=380)

    global clickvalue


    def quit(self):
        self.destroy()

    # update_my_info()
    mainloop()
    cnx.close()


##############################
# MAIN
##############################
# if __name__ == "__main__":
#     update_my_info()
    # window.mainloop()