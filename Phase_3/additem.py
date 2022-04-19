from  sql import sql__itemnumber__fetch
def additemobject(user_email):
    import tkinter as tk
    import sys
    import os
    #from tkinter import *
    #import global_variables
    import sys
    sys.path.append("MainMenu")
    #from  MainMenu import passon_variable

    #passon_variable

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
    #user_email=global_variables.email_text
    #display("email:"+user_email)
    master = tk.Tk()
    master.title("Add Item")
    master.resizable(width=False, height=False)
    # clickvalue=''
    # sets the geometry of main
    # root window
    #
    master.geometry("500x900")
    master.piece_cnt_txt=""
    master.video_media_type_txt=""
    master.platformtype_text=""
    master.game_type_txt=""
    def logout():
        master.destroy()
    l_piececnt = tk.Label(master, text="Piece Count")
    l_piececnt.place(x=40, y=225)
    l_piececnt.config(font=("Courier", 10, 'bold'))
    s_piece_cnt = tk.Spinbox(master, from_=1, to=10000)
    s_piece_cnt.place(x=40, y=250)
    s_piece_cnt.config(state='disabled')
    l_mediatype = tk.Label(master, text="Media Type")
    l_mediatype.place(x=40, y=300)
    l_mediatype.config(font=("Courier", 10, 'bold'))
    option_media_type = tk.StringVar(master)
    option_media_type.set("Optical Disc")
    menu_mediatype = tk.OptionMenu(master, option_media_type, "Optical Disc", "Game Card", "Cartridge")
    menu_mediatype.place(x=40, y=325)
    menu_mediatype.config(state='disabled')
    l_video_platformtype = tk.Label(master, text="Video Platform Type")
    l_video_platformtype.place(x=40, y=375)
    l_video_platformtype.config(font=("Courier", 10, 'bold'))
    option_video_platform_type = tk.StringVar(master)
    option_video_platform_type.set("Xbox")
    menu_video_platformtype = tk.OptionMenu(master, option_video_platform_type, "Nintendo", "PlayStation", "Xbox")
    menu_video_platformtype.place(x=40, y=395)
    menu_video_platformtype.config(state='disabled')
    l_computer_platformtype = tk.Label(master, text="Computer Platform Type")
    l_computer_platformtype.place(x=40, y=440)
    l_computer_platformtype.config(font=("Courier", 10, 'bold'))
    option_computer_platform_type = tk.StringVar(master)
    option_computer_platform_type.set("Windows")
    menu_computer_platformtype = tk.OptionMenu(master, option_computer_platform_type,  "Linux","macOS", "Windows")
    menu_computer_platformtype.place(x=40, y=465)
    menu_computer_platformtype.config(state='disabled')




    def gametypeselection(x):
        master.game_type_txt=x

        if x == 'Jigsaw Puzzle':
            s_piece_cnt.config(state='normal')
            master.piece_cnt_txt = s_piece_cnt.get()
            master.platformtype_text = ""
            master.video_media_type_txt = ""

        if x in('Video Game'):
            s_piece_cnt.config(state='disabled')
            menu_mediatype.config(state='normal')
            menu_video_platformtype.config(state='normal')
            menu_computer_platformtype.config(state='disabled')
            master.platformtype_text = option_video_platform_type.get()
            master.piece_cnt_txt = 0
            master.video_media_type_txt = option_media_type.get()

        if x in('Computer Game'):
            master.platformtype_text = option_computer_platform_type.get()
            master.piece_cnt_txt = 0
            master.video_media_type_txt = ""

            s_piece_cnt.config(state='disabled')
            menu_mediatype.config(state='disabled')
            menu_computer_platformtype.config(state='normal')

        if x in  ('Board Game','Card Game'):
            master.piece_cnt_txt = 0
            master.platformtype_text = ""
            master.video_media_type_txt = ""


    label_title = tk.Label(master, text="New Item Listing")
    label_title.place(width=250, height=35, x=50, y=50)
    label_title.config(font=("Courier", 15, 'bold'))


    l_gametype = tk.Label(master, text="Game Type")
    l_gametype.place(x=40, y=100)
    l_gametype.config(font=("Courier", 10, 'bold'))
    option_game_type = tk.StringVar(master)
    #option_game_type.set("JigSaw Puzzle")


    menu_gametype = tk.OptionMenu(master, option_game_type, "Jigsaw Puzzle",
        "Board Game",
        "Card Game",
        "Computer Game",
    "Video Game",command=gametypeselection)
    menu_gametype.place(x=40, y=120)
    l_title = tk.Label(master, text="Title")
    l_title.place(x=40, y=155)
    e_title = tk.Entry(master, borderwidth=1, relief="solid")
    e_title.place(width=300,height=35,x=40, y=175)
    l_condition = tk.Label(master, text="Condition")
    l_condition.place(x=40, y=515)
    l_condition.config(font=("Courier", 10, 'bold'))
    option_condition = tk.StringVar(master)
    option_condition.set("Like New")
    menu_condition = tk.OptionMenu(master, option_condition, "Like New","Limited to Mint", "Like New", "Lightly Used", "Moderately Used", "Heavily Used","Damaged/Missing parts")
    menu_condition.place(x=40, y=535)
    l_description = tk.Label(master, text="Description")
    l_description.place(x=40, y=565)
    e_description = tk.Entry(master, borderwidth=1, relief="solid")
    e_description.place(width=300,height=60,x=40, y=585)
    p = tk.StringVar()
    p.set("")
    tk.Label(master, textvariable=p).place(x=40, y=650)
    def itemadditionpopup():
        win = tk.Toplevel()
        win.geometry("210x100")
        win.wm_title("Success")

        l = tk.Label(win, text="Your item has been listed")

        l.grid(row=0, column=0)

        listitem_fetch_query = sql__itemnumber__fetch(user_email)
        listitem_data = []
        itemmnumber_text=""
        listitem_data = pd.read_sql_query(listitem_fetch_query, cnx)
        if listitem_data['itemnumber'].empty == False:
            itemmnumber_text=listitem_data['itemnumber'][0]
        else:
            itemmnumber_text = ""
        l1 = tk.Label(win, text="Your item number is " + str(itemmnumber_text))
        l1.grid(row=2, column=0)
        b = ttk.Button(win, text="OK", command=win.destroy)
        b.grid(row=4, column=0)

    def nulltitlepopup():
        win = tk.Toplevel()
        win.geometry("210x100")
        win.wm_title("Error")
        l1 = tk.Label(win, text="Null Title for the item or Invalid gametype")
        l1.grid(row=2, column=0)
        b = ttk.Button(win, text="OK", command=win.destroy)
        b.grid(row=4, column=0)

        l = tk.Label(win, text="Your item has been listed")
    def additeminsert():
        display(master.piece_cnt_txt)
        display(master.platformtype_text)
        display(master.video_media_type_txt)

        if (e_title.get()=="" or master.game_type_txt=='') :
            nulltitlepopup()
        else:
            add_item_query = "insert into CS6400_spr22_team103.item (item_title, item_condition, item_description, itemtype_name, itemtype_platform, itemtype_media, itemtype_piece_count, email) values " + "('" + e_title.get() + "','" + option_condition.get() + "','" + e_description.get() + "','" + master.game_type_txt + "','" + master.platformtype_text + "','" + master.video_media_type_txt + "','" + str(
                master.piece_cnt_txt) + "','" + user_email + "')"
            display(add_item_query)

            mycursor = cnx.cursor()
            mycursor.execute(add_item_query)
            cnx.commit()
            mycursor.close()
            cnx.close()
            
            itemadditionpopup()
            '''
            listitem_fetch_query = "Select count(1) cnt from  CS6400_spr22_team103.item  where item_title=  " + "'" + e_title.get() + "'"
            listitem_data = []
            itemmnumber_text = ""
            #import global_variables
            #passon_variable
            listitem_data = pd.read_sql_query(listitem_fetch_query, cnx)
            if listitem_data['cnt'].empty == False:

               add_item_query = "insert into CS6400_spr22_team103.item (item_title, item_condition, item_description, itemtype_name, itemtype_platform, itemtype_media, itemtype_piece_count, email) values " + "('" + e_title.get() + "','" + option_condition.get() +  "','" + e_description.get()  +  "','" + master.game_type_txt +  "','" + master.platformtype_text +  "','" + master.video_media_type_txt +  "','" + str(master.piece_cnt_txt) + "','" + user_email + "')"
               display(add_item_query)

               mycursor = cnx.cursor()
               mycursor.execute(add_item_query)
               cnx.commit()
               itemadditionpopup()
            else:
                p.set("Item Title Exists Please list with different title") '''

    listitembtn1 = Button(master, text="List Item", bg='blue', fg='white', borderless=1,command=additeminsert)
    listitembtn1.place(x=360, y=605)
    close_button = Button(master, text="Close", bg='blue', fg='white', borderless=1, command=logout)
    close_button.place(x=100, y=800)


    tk.mainloop()
