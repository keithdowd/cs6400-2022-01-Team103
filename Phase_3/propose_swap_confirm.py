from datetime import datetime

from global_variables import *
import propose_swap_insert
import search
# from sql import sql__propose_swap_confirm__items_for_swap
from sql import sql__my_items__list_of_all_items


def propose_swap_confirm(
  emailAddr, 
  offered_by_email,
  itemNumber,
  item_title, 
  distance):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Propose Swap'


  ##############################
  # SETUP
  ##############################

  def setup(title='My Window', width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(
    title=WINDOW_TITLE, 
    width=700, 
    height=WINDOW_SIZE_HEIGHT)

  # Create scrollable window for my items table
  container = ttk.Frame(window)

  canvas = tk.Canvas(
    container, 
    width=670, 
    height=200)

  scrollbar = ttk.Scrollbar(
    container, 
    orient='vertical', 
    command=canvas.yview)

  scrollable_frame = ttk.Frame(canvas, width=670)

  scrollable_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(
      scrollregion=canvas.bbox('all')
    )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
  canvas.configure(yscrollcommand=scrollbar.set)

  container.grid(row=7, column=0, columnspan=9, sticky='nesw')
  canvas.grid(row=0, column=0, sticky='nesw')
  scrollbar.grid(row=0, column=9, sticky='nse')

  ##############################
  # PROPOSE SWAP (CONFIRM)
  ##############################

  ########## DATA

  def return_to_search_exec():
    search.search(emailAddr)
    window.destroy()

  proposed_item_title = item_title
  proposed_item_number = itemNumber

  # Variables for input modals
  selection_rb_var = tk.IntVar(window)

  # Getters for for input modal variables
  def get_selection_rb_var():
    return selection_rb_var.get()

  my_items_columns = [
    'Item #',
    'Game Type',
    'Title',
    'Condition',
  ]

  # df = pd.read_sql_query(sql__propose_swap_confirm__items_for_swap(emailAddr), cnx)
  df = pd.read_sql_query(sql__my_items__list_of_all_items(emailAddr), cnx)

  my_items_data = []

  for _, row in df.iterrows():
      item_number = row['itemNumber']
      item_type_name = row['itemtype_name']
      item_title = row['item_title']
      item_condition = row['item_condition']
      
      arr = [
          item_number,
          item_type_name,
          item_title,
          item_condition
      ]

      my_items_data.append(arr)

  def propose_swap_confirm_exec():
    proposer_email = emailAddr
    counterparty_email = offered_by_email
    proposer_itemNumber = get_selection_rb_var()
    counterparty_itemNumber = proposed_item_number
    swap_status = ''
    swap_date_proposed = datetime.today().strftime('%Y-%m-%d')

    propose_swap_insert.propose_swap_insert(
      proposer_email,
      counterparty_email,
      proposer_itemNumber,
      counterparty_itemNumber,
      swap_status,
      swap_date_proposed
    )

    window.destroy()

  ########## VIEW

  # Header
  label_propose_swap = tk.Label(
    master=window, 
    text='Propose Swap', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE
  ))
  label_propose_swap.grid(
    row=0, 
    column=0, 
    columnspan=10,
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

  # Distance prompt (if distance >= 100.0 miles away)
  if distance >= 100.0:
    label_distance_prompt = tk.Label(
      master=window, 
      text=f'The other user is {distance} miles away!', 
      bg='red',
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_LABEL
    ))
    label_distance_prompt.grid(
      row=2, 
      column=0, 
      columnspan=10,
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y, 
      sticky='we')

  # Proposing trade for
  label_proposing_trade_for = tk.Label(
    master=window, 
    text=f'You are proposing a trade for: {proposed_item_title}', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_LABEL
  ))
  label_proposing_trade_for.grid(
    row=(2 if distance < 100.0 else 3), 
    column=0, 
    columnspan=10,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

  # Empty row
  empty_row = tk.Label(master=window, text='\n')
  empty_row.grid(row=(4 if distance < 100.0 else 3), column=0, columnspan=10)

  # Choose proposed item
  label_choose_proposed_item = tk.Label(
    master=window, 
    text=f'Please choose your proposed item:', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE
  ))
  label_choose_proposed_item.grid(
    row=(5 if distance < 100.0 else 4), 
    column=0, 
    columnspan=10,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

  # Choose proposed item table (header)
  for col_index, item_column in enumerate(my_items_columns):
    table_my_items_header = tk.Label(
      master=scrollable_frame,
      text=item_column, 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_LABEL
      ),
      width=10)
    table_my_items_header.grid(
      row=(6 if distance < 100.0 else 5), 
      column=col_index, 
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y,
      sticky='ew')

  # Choose proposed item table (values)
  for row_index, my_item in enumerate(my_items_data):
    original_row_index = row_index
    row_index += (7 if distance < 100.0 else 6) # layout starts at row 6 or 7
    
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
        width=18,
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
    select_rb = tk.Radiobutton(
      master=scrollable_frame,
      text='Select',
      font=(
        LABEL_FONT_FAMILY, 
        LABEL_FONT_SIZE, 
        LABEL_FONT_WEIGHT_VALUE),
      variable=selection_rb_var,
      value=my_items_data[original_row_index][0]
    )
    select_rb.grid(
      row=row_index,
      column=5,
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y, 
      sticky='w'
    )

  # Confirm button
  table_my_items_details_btn = tk.Button(
    master=window, 
    text='Confirm',
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE,
    ),
    command=propose_swap_confirm_exec
    # command=lambda item_number=get_selection_rb_var(): propose_swap_confirm_exec(item_number)
  )
  table_my_items_details_btn.grid(
    row=(row_index+21 if distance < 100.0 else row_index+20),
    column=0,
    columnspan=10,
    pady=20,
    padx=WINDOW_PADDING_X,
    sticky='w'
    )

  # Close button
  close_button = tk.Button(
    master=window, 
    text='Close',
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE,
    ),
    command=return_to_search_exec)
  close_button.grid(
    row=(row_index+21 if distance < 100.0 else row_index+20), 
    column=1,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y+20,  
    sticky='w') 


  ##############################
  # EVENT LOOP
  ##############################
  # window.mainloop()