from tkinter import *
from tkinter.font import BOLD
from global_variables import *
from sql import *



def swap_history(userEmail):
  # Window
  WINDOW_TITLE = 'Swap History'


  TABLE_COLUMN_ANCHOR = tk.W
  TABLE_COLUMN_STRETCH = tk.NO


  swap_summary_columns = ['My role', 'Total', 'Accepted', 'Rejected', 'Rejected %']


  swap_history_columns = ['Proposed Date', 'Accepted/Rejected Date', 'Swap Status', 'My Role', 'Proposed Item', 'Desired Item', 'Other User', 'Rating', '']

  proposed_list = []
  date_list = []
  swap_status_list = []
  my_role_list = []
  proposed_item_list = []
  desired_item_list = []
  other_user_list = []
  swap_summary_data = []

  swap_data = []

  rating_dropdown = ['1', '2', '3', '4', '5']
  clicked=[]
  ratings = [5, 4, 3, 2, 1, 0]

  def callback(i):
    rating=clicked[i].get()
    print("rating changed to:", rating)
    return rating


  


  ##############################
  # SETUP
  ##############################
  def setup(title=WINDOW_TITLE, width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(title=WINDOW_TITLE, width=1000, height=WINDOW_SIZE_HEIGHT)
  name_var = tk.StringVar()

    ######### DATA
  df = pd.read_sql_query(sql_swap_title(userEmail), cnx)
  proposer = pd.read_sql_query(sql_rating_count_proposer(userEmail), cnx)
  counter = pd.read_sql_query(sql_rating_count_counter(userEmail), cnx)
  #proposed/desire item most show title
  #try joining swap and item together
  for index, row in proposer.iterrows():
    total_counter = row['total']
    accepted_counter = row['accepted_count']
    rejected_counter = row['rejected_count']
    percentage = (rejected_counter/total_counter)
    store = ['Proposer', total_counter, accepted_counter, rejected_counter, round(percentage * 100, 2)]
    swap_summary_data.append(store)
    

  for index, row in counter.iterrows():
    total_counter = row['total']
    accepted_counter = row['accepted_count']
    rejected_counter = row['rejected_count']
    percentage = rejected_counter/total_counter
    store = ['Counter', total_counter, accepted_counter, rejected_counter, round(percentage * 100, 2)]
    swap_summary_data.append(store)
  


  for index, row in df.iterrows():
      # proposed_list.append(str(pd.read_sql_query(sql_swap_title(userEmail), cnx)['swap_date_proposed'][0]))
      # print(proposed_list[index][0])

      proposed_date = row['swap_date_proposed']
      accepted_rejected_date = row['swap_date_responded']
      swap_status = row['swap_status']
      proposer_email = row['proposer_email']
      if(proposer_email==userEmail):
        my_role_txt='Proposer'
      else:
        my_role_txt='Counterparty'

      my_role = my_role_txt

      proposed_item = row['proposer_itemNumber']
      proposed_item_text = pd.read_sql_query(sql__pull_itemname(proposed_item), cnx)
      desired_item = row['counterparty_itemNumber']
      desired_item_text = pd.read_sql_query(sql__pull_itemname(desired_item), cnx)


      counterparty_email = row['counterparty_email']
      counterparty_email_text = pd.read_sql_query(sql__accept_reject_get_user_name(counterparty_email),cnx)

      arr = [
          proposed_date,
          accepted_rejected_date,
          swap_status,
          my_role_txt,
          proposed_item_text['item_title'],
          desired_item_text['item_title'],
          counterparty_email_text['user_nickname'],
          # OptionMenu(window, name_var, *ratings, command=lambda i=row:callback(i))
          ]

      swap_data.append(arr)
      


  # ratings


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

# swap_history_grid("usr001@gt.edu")