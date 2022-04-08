import tkinter as tk
from tkinter import IntVar, Radiobutton, Text, ttk

##############################
# CONFIGURATION
##############################

# Window
WINDOW_HEIGHT = 400
WINDOW_PADDING_X = 5
WINDOW_PADDING_Y = 5
WINDOW_TITLE = 'Search'
WINDOW_WIDTH = 800

# Tables
TABLE_COLUMN_ANCHOR = tk.W
TABLE_COLUMN_STRETCH = tk.NO

# Font
LABEL_FONT_FAMILY = 'Courier'
LABEL_FONT_SIZE = 10
LABEL_FONT_WEIGHT_LABEL = 'bold'
LABEL_FONT_WEIGHT_VALUE = 'normal'

BUTTON_FONT_FAMILY = 'Courier'
BUTTON_FONT_SIZE = 14
BUTTON_FONT_WEIGHT = 'bold'


#Swap Summary
swap_summary_columns = ['My role', 'Total', 'Accepted', 'Rejected', 'Rejected %']

#Swap History
swap_history_columns = [
    'Item #',
    'Game type',
    'Title',
    'Condition',
    'Description',
    'Distance',
    ''
    ''
]

swap_data = [
    [
        '1885', 'Jigsaw puzzle', 'Georgia tech campus', 'Mint', 'Stuff', '0.0', 'Detail',
    ],
    [
       '1885', 'Jigsaw puzzle', 'Georgia tech campus', 'Mint', 'Stuff', '0.0', 'Detail',
    ],
    [
        '1885', 'Jigsaw puzzle', 'Georgia tech campus', 'Mint', 'Stuff', '0.0', 'Detail',
    ]
]




##############################
# SETUP
##############################


def setup(title='My Window', width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window


window = setup(title=WINDOW_TITLE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)


# Header
label_item_counts = tk.Label(master=window, text='Search')
label_item_counts.pack(padx=WINDOW_PADDING_X,
                       pady=WINDOW_PADDING_Y, anchor='w')

# Separator
separator = ttk.Separator(window, orient='horizontal')
separator.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, fill='x')


# Search
r1 = Radiobutton(text="By keyword: " , variable=IntVar(), value=1)
r1_text_field = Text(window, height=0, width=55)
r2 = Radiobutton(text="In my postal code", variable=IntVar(), value=2 )
r3 = Radiobutton(text="Within x miles of me", variable=IntVar(), value=3 )
r4 = Radiobutton(text="In postal code", variable=IntVar(), value=4)
r4_text_field = Text(window, height=0, width=55)
r1.pack(anchor = tk.W)
r1_text_field.pack()
r2.pack(anchor = tk.W)
r3.pack(anchor = tk.W)
r4.pack(anchor = tk.W)
r4_text_field.pack()
button_propose_swap = tk.Button(text='Search', font=(BUTTON_FONT_FAMILY, BUTTON_FONT_SIZE, BUTTON_FONT_WEIGHT), fg='white', bg='blue')
button_propose_swap.pack()


# Separator
separator = ttk.Separator(window, orient='horizontal')
separator.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, fill='x')

# Table
frame_items = tk.Frame(window)
frame_items.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')
table_items = ttk.Treeview(frame_items, height=len(swap_data))
table_items['columns'] = swap_history_columns
table_items.column('#0', width=0, stretch=TABLE_COLUMN_STRETCH)
table_items.heading('#0', text='')
for column in table_items['columns']:
    table_items.column(column, anchor=TABLE_COLUMN_ANCHOR,
                       width=int(WINDOW_WIDTH/len(table_items['column']))-2)
    table_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
for i, row in enumerate(swap_data):
    table_items.insert(parent='', index='end', iid=i, text='', values=row)
table_items.pack()

##############################
# EVENT LOOP
##############################
window.mainloop()