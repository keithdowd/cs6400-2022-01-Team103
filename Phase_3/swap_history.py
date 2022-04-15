from global_variables import *
from sql import sql_get_swap_history

itemNumber = 0
item_title = "test"
itemtype_name = "test name"
itemtype_platform = "test plat"
itemtype_media = "test media"
item_condition = "tes condition"

def view_item(userEmail):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Swap History'

  ##############################
  # SETUP
  ##############################
  def setup(title=WINDOW_TITLE, width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(title=WINDOW_TITLE, width=WINDOW_SIZE_WIDTH, height=WINDOW_SIZE_HEIGHT)

    

  ##############################
  # VIEW ITEM
  ##############################

  ########## DATA
#   df = pd.read_sql_query(sql_get_swap_history(userEmail), cnx)

#   proposed_date = df['swap_date_proposed'].values[0]
#   accepted_rejected_date = df['swap_date_responded'].values[0]
#   swap_status = df['swap_status'].values[0]
#   my_role = df['itemtype_platform'].values[0]
#   proposed_item = df['proposer_itemNumber'].values[0]
#   desired_item = df['counterparty_itemNumber'].values[0]
#   other_user = df['counterparty_email'].values[0]
#   rating = df['item_condition'].values[0]



  ########## VIEW

  # Header
  label_item_counts = tk.Label(master=window, text='Swap History')
  label_item_counts.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')

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
      table_items.column(column, anchor=TABLE_COLUMN_ANCHOR,idth=int(WINDOW_WIDTH/len(table_items['column']))-2)
      table_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
  for i, row in enumerate(swap_summary_data):
      table_items.insert(parent='', index='end', iid=i, text='', values=row)
 

  # Right column
  # frame_right = tk.Frame(master=window)
  # frame_right.grid(row=2, column=1, sticky='nw')

  # label_offered_by = tk.Label(master=frame_right, text='Offered by', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  # label_offered_by.grid(row=0, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_offered_by_value = tk.Label(master=frame_right, text=f'{OFFERED_BY}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  # label_offered_by_value.grid(row=0, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # label_location = tk.Label(master=frame_right, text='Location', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  # label_location.grid(row=1, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_location_value = tk.Label(master=frame_right, text=f'{LOCATION}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  # label_location_value.grid(row=1, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # label_rating = tk.Label(master=frame_right, text='Rating', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  # label_rating.grid(row=2, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_rating_value = tk.Label(master=frame_right, text=f'{RATING}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  # label_rating_value.grid(row=2, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # label_distance = tk.Label(master=frame_right, text='Distance', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL), bg='red')
  # label_distance.grid(row=3, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_distance_value = tk.Label(master=frame_right, text=f'{DISTANCE} miles', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE), bg='red')
  # label_distance_value.grid(row=3, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # button_propose_swap = tk.Button(master=frame_right, text='Propose Swap', height=2, font=(BUTTON_FONT_FAMILY, BUTTON_FONT_SIZE, BUTTON_FONT_WEIGHT), fg='white', bg='blue')
  # button_propose_swap.grid(row=4, columnspan=2, pady=25)

##############################
# EVENT LOOP
##############################
# if __name__ == "__main__":
  window.mainloop()

userEmail = "usr001@gt.edu"
view_item(userEmail)