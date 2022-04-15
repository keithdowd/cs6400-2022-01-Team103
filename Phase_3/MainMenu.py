from  additem import additemobject
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

    login_fetch_query="Select concat(user_firstname, ',' , user_lastname) name,unrated_swaps,unaccepted_swaps  from  CS6400_spr22_team103.user where email=  " + "'" + user_email+ "'"
    user_data = []
    user_data = pd.read_sql_query(login_fetch_query, cnx)
    myrating_fetch_query="Select avg(rating) user_rating,email from(Select sum(coalesce(swap_proposer_rating,0)) rating , proposer_email email from CS6400_spr22_team103.swap where proposer_email="+ "'" + user_email+ "'" +"union all Select sum(coalesce(swap_counterparty_rating,0)) , counterparty_email from CS6400_spr22_team103.swap where counterparty_email="+ "'" + user_email+ "'" +") a group by email"
    myrating_data = []
    myrating_data = pd.read_sql_query(myrating_fetch_query, cnx)
    print(myrating_fetch_query)



    myacceptedswaps_fetch_query = 'Select count(1) unaccepted_swaps from (Select 1 from CS6400_spr22_team103.swap where counterparty_email='+ "'" + user_email + "'" +' and swap_date_responded is null) A'
    myacceptedswaps_data = []
    myacceptedswaps_data = pd.read_sql_query(myacceptedswaps_fetch_query, cnx)
    fivedayoldswaps_fetch_query = 'Select count(1) fivedayoldswaps from (Select 1 from CS6400_spr22_team103.swap where counterparty_email='+ "'" + user_email + "'" +' and swap_date_responded is null and current_date-swap_date_proposed >4) A'
    fivedayoldswaps_data = []
    fivedayoldswaps_data = pd.read_sql_query(fivedayoldswaps_fetch_query, cnx)
    print(myrating_data)

    myratedswaps_fetch_query = '''
                               Select count(1) unrated_swaps from (Select swap_date_responded as acceptancedatee, 'Proposer' my_role,p_item.item_title ProposedItem, c_item.item_title DesiredItem,d_user.user_nickname other_user from CS6400_spr22_team103.swap s join CS6400_spr22_team103.item p_item on s.proposer_itemNumber=p_item.itemNumber
join CS6400_spr22_team103.item c_item on s.counterparty_itemNumber=c_item.itemNumber
join CS6400_spr22_team103.user d_user on s.counterparty_email=d_user.email
 where proposer_email='''+ "'" + user_email + "'" +'''
 and swap_status='Accepted'
 and swap_proposer_rating is null  
Union
Select swap_date_responded as acceptancedatee, 'Counterparty',p_item.item_title ProposedItem, c_item.item_title DesiredItem,d_user.user_nickname from CS6400_spr22_team103.swap s join CS6400_spr22_team103.item p_item on s.proposer_itemNumber=p_item.itemNumber
join CS6400_spr22_team103.item c_item on s.counterparty_itemNumber=c_item.itemNumber
join CS6400_spr22_team103.user d_user on s.counterparty_email=d_user.email
 where counterparty_email='''+ "'" +  user_email + "'" +'''
and swap_counterparty_rating is null and swap_status='Accepted') a
'''
    myratedswaps_data = []
    print(myratedswaps_fetch_query)
    myratedswaps_data = pd.read_sql_query(myratedswaps_fetch_query, cnx)



    def myitems():
        os.system('my_Items.py')

    def additem():
       additemobject(user_email)
      #os.system('additem.py')
    def searchitems():
        os.system('searchitems.py')

    def acceptorrejectswaps():
        if int(myacceptedswaps_data['unaccepted_swaps'][0]) > 0:
            os.system('GameSwapIntail.py')

    def propose_swaps():
        os.system('propose_swap.py')

    def unrated_swaps():
        if int(myratedswaps_data['unrated_swaps'][0]) > 0:
            os.system('rateswaps.py')
    def swaphistory():
        os.system('swaphistory.py')
    def updatemyinfo():
        os.system('UpdateMyInfo.py')



    label_logged_user = tk.Label(master,text="Welcome " + str(user_data['name'][0]))
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
    unacceptedswaps_text.set("Unaccepted Swaps-"+str(myacceptedswaps_data['unaccepted_swaps'][0]))
    unacceptedswaps_button = Button(master,
                 text=unacceptedswaps_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150,command=acceptorrejectswaps)
    unacceptedswaps_button.place(x=50,y=200)


    if myacceptedswaps_data['unaccepted_swaps'][0] > 4 or fivedayoldswaps_data['fivedayoldswaps'][0] >0 :
       unacceptedswaps_button.config(fg='red', font=("Courier", 10, 'bold'))
    else:
       unacceptedswaps_button.config(fg='blue', font=("Courier", 10))
    myitems_button = Button(master,text="My Item", bg='blue',fg='white', borderless=1,height=50,width=150,command=myitems)
    myitems_button.place(x=210,y=200)
    unratedswaps_text=tk.StringVar()
    unratedswaps_text.set("Unrated Swaps-"+str(myratedswaps_data['unrated_swaps'][0]))
    unratedswaps_button = Button(master,
                 text=unratedswaps_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150,command=unrated_swaps)
    unratedswaps_button.place(x=50,y=250)


    if myratedswaps_data['unrated_swaps'][0] > 1:
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