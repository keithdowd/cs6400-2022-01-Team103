from global_variables import *
from sql import *
# from view_item import view_item
from swap_history_detail import view_item

def my_items(userEmail):
  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Swap History'


  ##############################
  # SETUP
  ##############################

  def setup(title='Swap History', width=2500, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(
    title=WINDOW_TITLE, 
    width=1200, 
    height=WINDOW_SIZE_HEIGHT)

  # Create scrollable window for my my items table
  container = ttk.Frame(window)

  canvas = tk.Canvas(
    container, 
    width=1150,
    height=200)

  scrollbar = ttk.Scrollbar(
    container, 
    orient='vertical', 
    command=canvas.yview)
    
  scrollable_frame = ttk.Frame(canvas, width=1200)

  scrollable_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(
      scrollregion=canvas.bbox('all')
    )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
  canvas.configure(yscrollcommand=scrollbar.set)

  container.grid(row=7, column=0, columnspan=20, sticky='nesw')
  canvas.grid(row=0, column=0, sticky='nesw')
  scrollbar.grid(row=0, column=7, sticky='nse')


  ##############################
  # ITEM COUNTS
  ##############################

  ########## DATA
  
  # Item counts
  item_counts = {
    'My role': 0,
    'Total': 0,
    'Accepted': 0,
    'Rejected': 0,
    'Rejected %': 0,
  }

  counter_item_counts = {
    'My role': 0,
    'Total': 0,
    'Accepted': 0,
    'Rejected': 0,
    'Rejected %': 0,
  }

  df = pd.read_sql_query(sql__my_items__count_of_item_type(userEmail), cnx)
  proposer = pd.read_sql_query(sql_rating_count_proposer(userEmail), cnx)
  counter = pd.read_sql_query(sql_rating_count_counter(userEmail), cnx)


  proposer_accepted_count = 0 if proposer['accepted_count'].empty else proposer['accepted_count'].reset_index(drop=True)[0]
  proposer_rejected_count = 0 if proposer['rejected_count'].empty else proposer['rejected_count'].reset_index(drop=True)[0]
  proposer_rejected_percent = 0 if proposer_accepted_count == 0 else round((proposer_rejected_count/proposer_accepted_count)*100)
  proposer_total = proposer_accepted_count + proposer_rejected_count


  counter_accepted_count = 0 if counter['accepted_count'].empty else counter['accepted_count'].reset_index(drop=True)[0]
  counter_rejected_count = 0 if counter['rejected_count'].empty else counter['rejected_count'].reset_index(drop=True)[0]
  counter_rejected_percent = 0 if counter_accepted_count == 0 else round((counter_rejected_count/counter_accepted_count)*100)
  counter_total = counter_accepted_count + counter_rejected_count

  print("REJECT COUNTER HERE")
  print(counter_rejected_count)
  item_counts['My role'] = 'Proposer'
  item_counts['Total'] = proposer_total
  item_counts['Accepted'] = proposer_accepted_count
  item_counts['Rejected'] = proposer_rejected_count
  item_counts['Rejected %'] = proposer_rejected_percent


  counter_item_counts['My role'] = 'Counterparty'
  counter_item_counts['Total'] = counter_total
  counter_item_counts['Accepted'] = counter_accepted_count
  counter_item_counts['Rejected'] = counter_rejected_count
  counter_item_counts['Rejected %'] = counter_rejected_percent

  ########## VIEW

  # Header
  label_item_counts = tk.Label(
    master=window, 
    text='Swap History', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE
  ))
  label_item_counts.grid(
    row=0, 
    column=0, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

  # Separator
  separator = ttk.Separator(
    master=window, 
    orient='horizontal')
  separator.grid(
    row=1, 
    columnspan=10, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='ew')

  # Table (Header) #Propose
  for col_index, item_column in enumerate(item_counts.keys()):
    table_item_counts_header = tk.Label(
      master=window, 
      text=item_column, 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_LABEL),
    width=0)
    table_item_counts_header.grid(
      row=2, 
      column=col_index, 
      padx=1, 
      pady=WINDOW_PADDING_Y,
      sticky='ew')

  # Table (Values)#Propose
  for col_index, item_count in enumerate(item_counts.values()):
    table_item_counts_value = tk.Label(
      master=window, 
      text=item_count, 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_VALUE),
    width=0)
    table_item_counts_value.grid(
      row=3,
      column=col_index,
      padx=1, 
      pady=WINDOW_PADDING_Y,
      sticky='ew')
  

  # Table (Values)#counter
  for col_index, item_count in enumerate(counter_item_counts.values()):
    print(counter_item_counts.values())
    counter_table_item_counts_value = tk.Label(
      master=window, 
      text=item_count, bg=('red' if col_index==4 and counter_item_counts['Rejected %'] >= 50.0 else None),
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_VALUE),
    width=10)
    counter_table_item_counts_value.grid(
      row=4,
      column=col_index,
      padx=5, 
      pady=10,
      sticky='ew')
      

  ##############################
  # MY ITEMS
  ##############################

  ########## DATA

  my_items_columns = [
    'Proposed Date',
    'Accept/Reject DT',
    'Swap Status',
    'My Role',
    'Proposed Item',
    'Desired Item',
    'Other User',
    'Rating'
  ]

  swapID_data = []

  # df = pd.read_sql_query(sql__my_items__list_of_all_items(userEmail), cnx)
  df = pd.read_sql_query(sql_swap_title(userEmail), cnx)

  my_items_data = []
  # print(len(df))
  for index, row in df.iterrows():
      # print("start here")
      # print(row)
      proposed_date = row['swap_date_proposed']
      accepted_rejected_date = row['swap_date_responded']
      swap_status = row['swap_status']
      proposer_email = row['proposer_email']
      if(proposer_email==userEmail):
        my_role_txt='Proposer'
      else:
        my_role_txt='Counterparty'
      #if proposer rating is not null then rating_text = row[purposer_rating] else row[counter_party rating]
      rating_data = row['swap_proposer_rating']
      # if row['swap_proposer_rating'] != 'null':
        
      proposed_item = row['proposer_itemNumber']
      proposed_item_text = pd.read_sql_query(sql__pull_itemname(proposed_item), cnx)
      desired_item = row['counterparty_itemNumber']
      desired_item_text = pd.read_sql_query(sql__pull_itemname(desired_item), cnx)
  
      counterparty_email = row['counterparty_email']
      counterparty_email_text = pd.read_sql_query(sql__accept_reject_get_user_name(counterparty_email),cnx)
      swapID = row['swapID']
      swap_ID_arry = [
        swapID,
        proposed_item,
        desired_item,
        my_role_txt
      ]
      arr = [
          proposed_date,
          accepted_rejected_date,
          swap_status,
          my_role_txt,
          proposed_item_text['item_title'][0],
          desired_item_text['item_title'][0],
          counterparty_email_text['user_nickname'][0],
          proposed_date
      ]
      swapID_data.append(swap_ID_arry)
      print(swapID_data)
      my_items_data.append(arr)
  # print("stop here")
  ########## VIEW

  # Empty row
  empty_row = tk.Label(master=window, text='\n')
  empty_row.grid(row=4, column=0, columnspan=10)

  # Header
  label_my_items = tk.Label(
    master=window, 
    text='My Items',
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE)
  )
  label_my_items.grid(
    row=5, 
    column=0, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

  # Separator
  separator = ttk.Separator(
    master=window, 
    orient='horizontal')
  separator.grid(
    row=6, 
    columnspan=10, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='ew')

  if len(my_items_data) > 0: # Show table view if the user has at least one item
    # Table (Header)
    for col_index, item_column in enumerate(my_items_columns):
      table_my_items_header = tk.Label(
        master=scrollable_frame, 
        text=item_column, 
        font=(
          LABEL_FONT_FAMILY,
          LABEL_FONT_SIZE,
          LABEL_FONT_WEIGHT_LABEL
        ),
        width=16)
      table_my_items_header.grid(
        row=7, 
        column=col_index, 
        padx=WINDOW_PADDING_X, 
        pady=WINDOW_PADDING_Y,
        sticky='ew')

    # Table (Values)
    for row_index, my_item, in enumerate(my_items_data):
      org_row_index = row_index
      row_index += 8 # layout starts at row 8

      
      for col_index, my_item_value in enumerate(my_item):
        # center item number and left justify all other fields
        if col_index == 0:
          anchor = 'center'
        else:
          anchor = 'w'

        table_my_items_value = tk.Label(
          master=scrollable_frame, 
          text=my_item_value, 
          font=(
            LABEL_FONT_FAMILY,
            LABEL_FONT_SIZE,
            LABEL_FONT_WEIGHT_VALUE     
          ), 
          width=16,
          wraplength=125,
          anchor=anchor,
          justify='left')
        table_my_items_value.grid(
          row=row_index,
          column=col_index,
          padx=WINDOW_PADDING_X,
          pady=WINDOW_PADDING_Y,
          sticky='ne'
        )
      table_my_items_details_btn = tk.Button(
        master=scrollable_frame, 
        text='Details',
        font=(
          LABEL_FONT_FAMILY,
          LABEL_FONT_SIZE,
          LABEL_FONT_WEIGHT_VALUE,
        ),
        command=lambda swapID_number=swapID_data[org_row_index]: view_item(swapID_number) 
      )
      table_my_items_details_btn.grid(
        row=row_index,
        column=col_index+1, # add button after (to the right of) the last my items column
        sticky='we'
        ) 
    
  else: # Show a message instead of the items table if the user has no items
    label_my_items = tk.Label(
      master=scrollable_frame, 
      text='You have no items.', 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_VALUE
    ))
    label_my_items.grid(
      row=7, 
      column=0, 
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y, 
      sticky='w')
  window.mainloop()

##############################
# EVENT LOOP
##############################
my_items('usr001@gt.edu')