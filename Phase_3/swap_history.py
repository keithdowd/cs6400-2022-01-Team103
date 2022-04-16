from global_variables import *
from sql import sql_get_swap_history



def swap_history(userEmail):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Swap History'


  TABLE_COLUMN_ANCHOR = tk.W
  TABLE_COLUMN_STRETCH = tk.NO


  swap_summary_columns = ['My role', 'Total', 'Accepted', 'Rejected', 'Rejected %']


  swap_history_columns = ['Proposed Date', 'Accepted/Rejected Date', 'Swap Status', 'My Role', 'Proposed Item', 'Desired Item', 'Other User', 'Rating', '','']


  swap_summary_data = [['Proposer', '2', '1', '1', '50.0%'],['CounterParty', '2', '2', '0', '0.0%'] ]

  swap_data = []

  rating_dropdown = ['1', '2', '3', '4', '5']





  ##############################
  # SETUP
  ##############################
  def setup(title=WINDOW_TITLE, width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(title=WINDOW_TITLE, width=WINDOW_SIZE_WIDTH, height=WINDOW_SIZE_HEIGHT)

    ######### DATA
  df = pd.read_sql_query(sql_get_swap_history(userEmail), cnx)

  proposed_date = df['swap_date_proposed'].values[0]
  accepted_rejected_date = df['swap_date_responded'].values[0]
  swap_status = df['swap_status'].values[0]
  my_role = df['itemtype_platform'].values[0]
  proposed_item = df['proposer_itemNumber'].values[0]
  desired_item = df['counterparty_itemNumber'].values[0]
  other_user = df['counterparty_email'].values[0]
  rating = df['item_condition'].values[0]

  print(proposed_date)


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
      table_items.column(column, anchor=TABLE_COLUMN_ANCHOR,width=int(WINDOW_SIZE_WIDTH/len(table_items['column']))-2)
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
                        width=int(WINDOW_SIZE_WIDTH/len(table_items['column']))-2)
      table_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
  for i, row in enumerate(swap_data):
      table_items.insert(parent='', index='end', iid=i, text='', values=row)
  table_items.pack()
 
##############################
# EVENT LOOP
##############################
# if __name__ == "__main__":
  window.mainloop()


userEmail = "usr001@gt.edu"
swap_history(userEmail)