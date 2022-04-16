from global_variables import *
def get_unrated_swaps(userEmail):
    import tkinter as tk
    from tkinter import ttk, StringVar, OptionMenu, Button
    from tkinter.font import BOLD

    from sql import sql_get_my_unrated_swaps
    import pandas as pd

    ##############################
    # CONFIGURATION
    ##############################

    # Window
    WINDOW_TITLE = 'Propose Swap'
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 800


    # ratings
    ratings = [5, 4, 3, 2, 1, 0]

    # swaps to be rated
    items_columns = [
        'Swap #',
        'Date Proposed',
        'Date Accepted',
        'User Email',
        'Item #',
        'Title',
        'Condition',
        'Description',
        ''
    ]


    # items_data = [
    #     [
    #         258, '2022-01-21', '2022-01-25', 'usr121@gt.edu', '875', 'Nuclear Strike 64', 'Mint', 'EA'
    #     ],
    #     [
    #         268, '2022-01-25', '2022-01-27', 'usr074@gt.edu', '536', 'Major League Baseball 2K8', 'Like New', 'Sports Kush Games'
    #     ]
    # ]


    unrated_items= pd.read_sql_query(sql_get_my_unrated_swaps(userEmail),cnx)
    print(sql_get_my_unrated_swaps(userEmail))
    items_data= unrated_items.values.tolist()
    print(items_data)


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
    label_item_number = tk.Label(window, text='Swap #', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_item_number.grid(row=2, column=0)

    label_title = tk.Label(window, text= 'Date Proposed', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_title.grid(row=2, column=2)

    label_game_type = tk.Label(window, text= 'Date Accepted', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_game_type.grid(row=2, column=4)

    label_platform = tk.Label(window, text='User Email', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_platform.grid(row=2, column=6)

    label_media = tk.Label(window, text='Item #', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_media.grid(row=2, column=8)

    label_title = tk.Label(window, text='Title', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_title .grid(row=2, column=10)

    label_condition = tk.Label(window, text='Condition', font=(
        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_condition.grid(row=2, column=12)

    # label_condition = tk.Label(window, text='Description', font=(
    #     LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    # label_condition.grid(row=2, column=14)


    for i, row in enumerate(items_data):
        clicked = StringVar()
        clicked.set("Select Rating")
        # Create an instance of Menu in the frame
        drop = OptionMenu(window, clicked, "5", "4",
                        "3", "2", "1", "0")

        label_item_number_value = tk.Label(window, text=row[0], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_item_number_value.grid(row=i+3, column=0)

        label_title_value = tk.Label(window, text=row[1], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_title_value.grid(row=i+3, column=2)

        label_game_type_value = tk.Label(window, text=row[2], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_game_type_value.grid(row=i+3, column=4)

        label_platform_value = tk.Label(window, text=row[3], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_platform_value.grid(row=i+3, column=6)

        label_media_value = tk.Label(window, text=row[4], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_media_value.grid(row=i+3, column=8)

        label_condition_value = tk.Label(window, text=row[5], font=(
            LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
        label_condition_value.grid(row=i+3, column=10)

        drop.grid(row=i+3, column=14)

    # Separator2
    separator = ttk.Separator(window, orient='horizontal')
    separator.grid(row=8, column=6)

    submit = Button(window, text="Submit Rating", fg="Black",
                    bg="Green", font=(
                        LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE, BOLD))
    submit.grid(row=9, column=12)

    ##############################
    # EVENT LOOP
    ##############################
    window.mainloop()


# # def rate_swaps(emailAddr, swapID, rating):
# get_unrated_swaps(userEmail='usr071@gt.edu')