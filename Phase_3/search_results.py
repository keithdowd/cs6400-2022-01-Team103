from haversine import haversine
from global_variables import *
import propose_swap
import search
from sql import sql__search_results__get_item_data_from_item_numbers
from sql import sql__search__get_lat_lon_by_postal_code
from sql import sql__search__get_postal_code_by_email
from sql import sql__search_results__get_lat_lon_from_item_number

def search_results(emailAddr, item_numbers, selection, context):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_SIZE_HEIGHT = 450
  WINDOW_SIZE_WIDTH = 900
  WINDOW_TITLE = 'Search Results'


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
    width=WINDOW_SIZE_WIDTH, 
    height=WINDOW_SIZE_HEIGHT)

  # Create scrollable window for my search results table
  container = ttk.Frame(window)

  canvas = tk.Canvas(
    container, 
    width=WINDOW_SIZE_WIDTH-50, 
    height=350)

  v_scrollbar = ttk.Scrollbar(
    container, 
    orient='vertical', 
    command=canvas.yview)
  
  h_scrollbar = ttk.Scrollbar(
    container, 
    orient='horizontal', 
    command=canvas.xview)
    
  scrollable_frame = ttk.Frame(canvas)

  scrollable_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(
      scrollregion=canvas.bbox('all')
    )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
  canvas.configure(yscrollcommand=v_scrollbar.set)
  canvas.configure(xscrollcommand=h_scrollbar.set)

  container.grid(row=7, column=0, columnspan=9, sticky='nesw')
  canvas.grid(row=0, column=0, sticky='nesw')
  v_scrollbar.grid(row=0, column=7, sticky='nse')
  h_scrollbar.grid(row=10, column=0, sticky='we')


  ##############################
  # SEARCH RESULTS
  ##############################

  ########## DATA

  def return_to_search_exec():
    search.search(emailAddr)
    window.destroy()

  search_results_table_columns = [
      'Item #',
      'Game Type',
      'Title',
      'Condition',
      'Description',
      'Distance'
    ]

  # Convert selection and context to a human-readable string
  def selection_to_context(selection, context):
    if selection == 1:
      return f'keyword "{context}"'
    elif selection == 2:
      return f'my postal code "{context}"'
    elif selection == 3:
      return f'with "{context}" miles of me'
    elif selection == 4:
      return f'other postal code "{context}"'
    return 'error'

  selection_to_context_str = selection_to_context(selection, context)

  def compute_distance(item_number):
    # Get users lat, lon
    df = pd.read_sql_query(sql__search__get_postal_code_by_email(emailAddr), cnx)
    user_postal_code = df['postalcode'].values[0]
    df = pd.read_sql_query(sql__search__get_lat_lon_by_postal_code(user_postal_code), cnx)
    user_lat = float(df['addr_latitude'].values[0])
    user_lon = float(df['addr_longitude'].values[0])
    
    # Get item numbers lat, lon
    df = pd.read_sql_query(sql__search_results__get_lat_lon_from_item_number(item_number), cnx)
    item_lat = float(df['addr_latitude'].values[0])
    item_lon = float(df['addr_longitude'].values[0])

    # Compute distance
    distance = round(haversine(user_lat, item_lat, user_lon, item_lon), 1)

    # Return distance
    return distance

  # Get item data from item numbers
  # TODO: Refactor match my_items.py and adjust description
  def get_item_data_from_item_numbers(item_numbers):
    item_data = []
    for item_number in item_numbers:
      query = sql__search_results__get_item_data_from_item_numbers(item_number)
      df = pd.read_sql_query(query, cnx)
      item = df.values[0].tolist()
      item.append(compute_distance(item_number))
      item_data.append(item)
    return item_data

  item_data = get_item_data_from_item_numbers(item_numbers)
  item_data = pd.DataFrame(item_data, columns=search_results_table_columns)
  
  def truncate_description(description):
    if len(description) > 100:
      return description[0:100] + '...'
    else:
      return description
  
  item_data['Description'] = item_data['Description'].apply(truncate_description)

  item_data.sort_values(by=['Distance', 'Item #'], ascending=True, inplace=True)
  item_data = item_data.values.tolist()

  def propose_swap_exec(emailAddr, item_number):
    propose_swap.propose_swap(emailAddr, item_number)
    window.destroy()

  ########## VIEW

  # Header
  header = tk.Label(
    master=window, 
    text=f'Search results: {selection_to_context_str}', 
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE))
  header.grid(
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

  if len(item_data) > 0: # Show table view if the user has at least one item
    # Results table (header)
    for col_index, column_name in enumerate(search_results_table_columns):
      search_results_table_header = tk.Label(
        master=scrollable_frame, 
        text=column_name, 
        font=(
          LABEL_FONT_FAMILY,
          LABEL_FONT_SIZE,
          LABEL_FONT_WEIGHT_LABEL
        ),
        width=16)
      search_results_table_header.grid(
        row=2, 
        column=col_index, 
        padx=WINDOW_PADDING_X, 
        pady=WINDOW_PADDING_Y,
        sticky='w')

    # Table (Values)
    for row_index, my_item in enumerate(item_data):
      row_index += 3 # layout starts at row 3
      
      for col_index, my_item_value in enumerate(my_item):
        # center item number distance and left justify all other fields
        if col_index == 0 or col_index == 5:
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
          bg='cyan' if selection == 1 and isinstance(my_item_value, str) and my_item_value.lower().find(context) >= 0 else None,
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
        command=lambda item_number=my_item[0]: propose_swap_exec(emailAddr, item_number)
      )
      table_my_items_details_btn.grid(
        row=row_index,
        column=col_index+1, # add button after (to the right of) the last my items column
        sticky='e'
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
      row=10, 
      column=0,
      padx=20, 
      pady=WINDOW_PADDING_Y,  
      sticky='w') 

  else: # Show a message instead of the items table if the user has no items
    label_my_items = tk.Label(
      master=scrollable_frame,
      text='Sorry, no results found!', 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_VALUE
    ))
    label_my_items.grid(
      row=2, 
      column=0, 
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y, 
      sticky='w')
    
    return_to_search_btn = tk.Button(
        master=scrollable_frame, 
        text='Return to Search',
        font=(
          LABEL_FONT_FAMILY,
          LABEL_FONT_SIZE,
          LABEL_FONT_WEIGHT_VALUE,
        ),
        command=return_to_search_exec
      )
    return_to_search_btn.grid(
      row=3,
      column=0,
      padx=WINDOW_PADDING_X,
      pady=WINDOW_PADDING_Y,
      sticky='w'
    )


##############################
# EVENT LOOP
##############################
# if __name__ == "__main__":
#   window.mainloop()