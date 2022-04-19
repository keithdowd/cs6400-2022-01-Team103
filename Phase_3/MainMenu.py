from  additem import additemobject
from sql import sql__firstlastname__fetch
from sql import sql__myrating__fetch
from sql import sql__unacceptedswaps__fetch
from sql import sql__fivedayoldswap__fetch
from sql import sql__unratedswaps__fetch
import my_items
import rateswaps
import AcceptRejectSwaps
import search
import swap_history_new
import UpdateMyInfo
def MainMenuObject(user_email):
#if __name__ == '__main__':
    import tkinter as tk
    import sys
    import os
    #from tkinter import *
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
    master = tk.Tk()
    master.title("GameSwap")
    master.resizable(width=False, height=False)
    #clickvalue=''
    # sets the geometry of main
    # root window
    master.geometry("500x500")


    def logout():
        master.destroy()
    label_title = tk.Label(master,text="GameSwap")
    label_title.place(width=100,height=35,x=50,y=50)
    label_title.config(font=("Courier", 15,'bold'))
    label_underline = tk.Label(master,text="----------------------------------------------------------------------------------------------------------------")
    label_underline.place(width=400,height=50,x=50,y=85)
    label_underline.config(font=("Courier", 5,'bold'))

    logout_button = Button(master,
                 text="Logout", bg='blue',fg='white', borderless=1,command=logout)
    logout_button.place(x=400,y=30)


    first_last_name_fetch_query=sql__firstlastname__fetch(user_email)
    first_last_name_data = []
    first_last_name_data = pd.read_sql_query(first_last_name_fetch_query, cnx)
    print(first_last_name_fetch_query)
    myrating_fetch_query=sql__myrating__fetch(user_email)
    myrating_data = []
    myrating_data = pd.read_sql_query(myrating_fetch_query, cnx)
    print(myrating_fetch_query)




    unacceptedswaps_fetch_query=sql__unacceptedswaps__fetch(user_email)
    unacceptedswaps_data = []
    unacceptedswaps_data = pd.read_sql_query(unacceptedswaps_fetch_query, cnx)
    fivedayoldswaps_fetch_query = sql__fivedayoldswap__fetch(user_email)
    fivedayoldswaps_data = []
    fivedayoldswaps_data = pd.read_sql_query(fivedayoldswaps_fetch_query, cnx)
    print(myrating_data)

    unratedswaps_fetch_query = sql__unratedswaps__fetch(user_email)
    unratedswaps_data = []
    print(unratedswaps_fetch_query)
    unratedswaps_data = pd.read_sql_query(unratedswaps_fetch_query, cnx)



    def myitems():
        my_items.my_items(user_email)
        #os.system('my_items.py')

    def additem():
       additemobject(user_email)
      #os.system('additem.py')
    def searchitems():
        search.search(user_email)
        #os.system('searchitems.py')

    def acceptorrejectswaps():
        if int(unacceptedswaps_data['unaccepted_swaps'][0]) > 0:
            AcceptRejectSwaps.accept_reject_swaps(user_email)
             #os.system('searchitems.py')

    def propose_swaps():
      os.system('propose_swap.py')

    def unrated_swaps():
        if int(unratedswaps_data['unrated_swaps'][0]) > 0:
            rateswaps.get_unrated_swaps(user_email)
            #os.system('rateswaps.py')
    def swaphistory():
        swap_history_new.swap_hist(user_email)
    def updatemyinfo():
        UpdateMyInfo.update_my_info(user_email)



    label_logged_user = tk.Label(master,text="Welcome " + str(first_last_name_data['name'][0]))
    label_logged_user.place(width=300,height=35,x=50,y=125)
    label_logged_user.config(font=("Times Roman", 10,'bold'))
    myrating_text=tk.StringVar()

    myrating_text.set("My Rating-"+str(myrating_data['user_rating'][0]))
    myrating_button = Button(master,
                 text=myrating_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150)
    myrating_button.place(x=50,y=150)
    myrating_button.config(fg='blue', font=("Courier", 10))



    listitem_button = Button(master,
                 text="List Item", bg='blue',fg='white', borderless=1,height=50,width=150,command=additem)
    listitem_button.place(x=210,y=150)
    unacceptedswaps_text=tk.StringVar()
    unacceptedswaps_text.set("Unaccepted Swaps-"+str(unacceptedswaps_data['unaccepted_swaps'][0]))
    unacceptedswaps_button = Button(master,
                 text=unacceptedswaps_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150,command=acceptorrejectswaps)
    unacceptedswaps_button.place(x=50,y=200)


    if unacceptedswaps_data['unaccepted_swaps'][0] > 4 or fivedayoldswaps_data['fivedayoldswaps'][0] >0 :
       unacceptedswaps_button.config(fg='red', font=("Courier", 10, 'bold'))
    else:
       unacceptedswaps_button.config(fg='blue', font=("Courier", 10))
    myitems_button = Button(master,text="My Item", bg='blue',fg='white', borderless=1,height=50,width=150,command=myitems)
    myitems_button.place(x=210,y=200)
    unratedswaps_text=tk.StringVar()
    unratedswaps_text.set("Unrated Swaps-"+str(unratedswaps_data['unrated_swaps'][0]))
    unratedswaps_button = Button(master,
                 text=unratedswaps_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150,command=unrated_swaps)
    unratedswaps_button.place(x=50,y=250)


    if unratedswaps_data['unrated_swaps'][0] > 1:
       unratedswaps_button.config(fg='red',font=("Courier", 10,'bold'))
    else:
       unratedswaps_button.config(fg='blue', font=("Courier", 10))
    searchitems_button = Button(master,
                 text="Search Items", bg='blue',fg='white', borderless=1,height=50,width=150,command=searchitems)
    searchitems_button.place(x=210,y=250)
    swaphistory_button = Button(master,
                 text="Swap History", bg='blue',fg='white', borderless=1,height=50,width=150,command=swaphistory)
    swaphistory_button.place(x=210,y=300)
    updatemyinfo_button = Button(master,
                 text="Update my info", bg='blue',fg='white', borderless=1,height=50,width=150,command=updatemyinfo)
    updatemyinfo_button.place(x=210,y=350)


    tk.mainloop()