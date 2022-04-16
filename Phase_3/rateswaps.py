# import email
import tkinter as tk
from tkinter import ttk, StringVar, OptionMenu, Button
from tkinter.font import BOLD
from global_variables import *
from sql import sql_get_my_unrated_swaps,sql_rate_my_unrated_swaps
import pandas as pd


def get_unrated_swaps(userEmail='usr071@gt.edu'):

    ##############################
    # CONFIGURATION
    ##############################

    # Window
    WINDOW_TITLE = 'Rate Swap'
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 1000


    # ratings
    ratings = [5, 4, 3, 2, 1, 0]

    # swaps to be rated
    items_columns = [
        'Swap#',
        'Date_Proposed',
        'Date_Accepted',
        'UserEmail',
        'Item#',
        'Title',
        'Condition',
        'Description',
        ''
    ]


    unrated_items= pd.read_sql_query(sql_get_my_unrated_swaps(userEmail),cnx)

    items_data= unrated_items.values.tolist()
    # print(items_data)


    ##############################
    # SETUP
    ##############################


    def setup(title='My Window', width=800, height=400):
        window = tk.Tk()
        window.title(title)
        window.geometry(f'{width}x{height}')
        return window


    window = setup(title=WINDOW_TITLE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)


    ##############################
    # View
    ##############################

    # Header
    header = tk.Label(window, text='Rate Items', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE, BOLD))
    header.grid(row=0, column=6)

    header.grid_configure(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y)

    # Separator
    separator = ttk.Separator(window, orient='horizontal')
    separator.grid(row=1, column=6)

    # columns
    label_swapID = tk.Label(window, text='Swap#', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_swapID.grid(row=2, column=0)

    label_date_proposed = tk.Label(window, text= 'Propose', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_date_proposed.grid(row=2, column=2)

    label_date_accepted = tk.Label(window, text= 'Accept', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_date_accepted.grid(row=2, column=4)

    label_user_email = tk.Label(window, text='User_Email', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_user_email.grid(row=2, column=6)

    label_item_ID = tk.Label(window, text='Item#', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_item_ID.grid(row=2, column=8)

    label_title = tk.Label(window, text='Title', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_title.grid(row=2, column=10)

    label_condition = tk.Label(window, text='Condition', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_condition.grid(row=2, column=12)

    label_rating = tk.Label(window, text='Rating', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_rating.grid(row=2, column=14)

    clicked=[None, None]
    rating=[None, None]
    index_num=0
    for i, row in enumerate(items_data):

        label_swapID_value = tk.Label(window, text=row[0], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_swapID_value.grid(row=i+3, column=0)

        label_date_proposed_value = tk.Label(window, text=row[1], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_date_proposed_value.grid(row=i+3, column=2)

        label_date_accepted_value = tk.Label(window, text=row[2], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_date_accepted_value.grid(row=i+3, column=4)

        label_user_email_value = tk.Label(window, text=row[3], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_user_email_value.grid(row=i+3, column=6)

        label_item_ID_value = tk.Label(window, text=row[4], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_item_ID_value.grid(row=i+3, column=8)

        label_title_value = tk.Label(window, text=row[5], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_title_value.grid(row=i+3, column=10)

        label_condition_value = tk.Label(window, text=row[5], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_condition_value.grid(row=i+3, column=12)


        clicked[i] = StringVar()
        clicked[i].set(5)


        def callback():
            rating=clicked[i].get()
            print("rating changed to:", rating)
            return rating
        drop = OptionMenu(window, clicked[i], *ratings, command=lambda index_num=i:callback())

        drop.grid(row=i+3, column=14)

        # def close_window(self):
        #     self.master.destroy()

        submit = Button(window, text="Rate", fg="Black",
            bg="Green", font=(
                LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE, BOLD), 
                command=lambda index_num=i: rate_swaps(rating=callback(),userEmail=userEmail, emailAddr=row[3], swapID=row[0] ))
        submit.grid(row=i+3, column=16)

    ##############################
    # EVENT LOOP 
    ##############################
    window.mainloop()


def rate_swaps(emailAddr, userEmail, swapID, rating):
    mycursor = cnx.cursor()
    query=sql_rate_my_unrated_swaps(emailAddr, swapID, rating)
    print(query)
    mycursor.execute(query)
    cnx.commit()
    mycursor.close()
    get_unrated_swaps(userEmail)


#test this page
# get_unrated_swaps(userEmail='usr071@gt.edu')

# rate_swaps('usr121@gt.edu', 258,4)