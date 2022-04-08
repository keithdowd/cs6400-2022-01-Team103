import tkinter as tk
from tkinter import ttk

##############################
# CONFIGURATION
##############################

# Window
WINDOW_HEIGHT = 400
WINDOW_PADDING_X = 5
WINDOW_PADDING_Y = 5
WINDOW_TITLE = 'Swap History'
WINDOW_WIDTH = 800

# Tables
TABLE_COLUMN_ANCHOR = tk.W
TABLE_COLUMN_STRETCH = tk.NO


#Swap Summary
swap_summary_columns = ['My role', 'Total', 'Accepted', 'Rejected', 'Rejected %']

#Swap History
swap_history_columns = [
    'Proposed Date',
    'Accepted/Rejected Date',
    'Swap status',
    'My role',
    'Proposed Item',
    'Desired Item',
    'Other User',
    'Rating',
    ''
    ''
]

swap_data = [
    [
        '06/01/2021', '06/02/2021', 'Accepted', 'Proposer', 'Mastermind', 'Skip-Bo', 'Princessz', 'drophere', 'Detail'
    ],
    [
       '06/01/2021', '06/02/2021', 'Accepted', 'Proposer', 'Mastermind', 'Skip-Bo', 'Princessz', 'drophere', 'Detail'
    ],
    [
        '06/01/2021', '06/02/2021', 'Accepted', 'Proposer', 'Mastermind', 'Skip-Bo', 'Princessz', 'drophere', 'Detail'
    ]
]


swap_summary_data = [['Proposer', '2', '1', '1', '50.0%'],['CounterParty', '2', '2', '0', '0.0%'] ]


rating_dropdown = ['1', '2', '3', '4', '5']



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
label_item_counts = tk.Label(master=window, text='Swap History ')
label_item_counts.pack(padx=WINDOW_PADDING_X,
                       pady=WINDOW_PADDING_Y, anchor='w')

# Separator
separator = ttk.Separator(window, orient='horizontal')
separator.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, fill='x')

# Table
frame_items = tk.Frame(window)
frame_items.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')
table_items = ttk.Treeview(frame_items, height=len(swap_summary_data))
table_items['columns'] = swap_summary_columns
table_items.column('#0', width=0, stretch=TABLE_COLUMN_STRETCH)
table_items.heading('#0', text='')
for column in table_items['columns']:
    table_items.column(column, anchor=TABLE_COLUMN_ANCHOR,
                       width=int(WINDOW_WIDTH/len(table_items['column']))-2)
    table_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
for i, row in enumerate(swap_summary_data):
    table_items.insert(parent='', index='end', iid=i, text='', values=row)
table_items.pack()


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