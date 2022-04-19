from haversine import haversine
from global_variables import *
import search_results
from sql import sql__search__get_postal_code_by_email
from sql import sql__search__items_by_keyword
from sql import sql__search__get_lat_lon_by_postal_code
from sql import sql__search__items_by_my_postal_code
from sql import sql__search__items_by_other_postal_code
from sql import sql__search__get_all_postal_codes_lat_lon


def search(emailAddr='usr001@gt.edu'):
  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_SIZE_HEIGHT = 275
  WINDOW_SIZE_WIDTH = 450
  WINDOW_TITLE = 'Search'


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


  ##############################
  # SEARCH
  ##############################

  ########## DATA

  # Variables for input modals
  selection_rb_var = tk.IntVar(window)
  keyword_entry_var = tk.StringVar(window)
  miles_sb_var = tk.StringVar(window)
  other_postal_code_entry_var = tk.StringVar(window)
  
  # Getters for for input modal variables
  def get_selection_rb_var():
    return selection_rb_var.get()

  def get_keyword_entry_var():
    return keyword_entry_var.get()

  def get_miles_sb_var():
    return miles_sb_var.get()

  def get_other_postal_code_entry_var():
    return other_postal_code_entry_var.get()

  # Identify appropriate query for search results
  def get_search_query():
  
    # Get radio button selection
    selection = get_selection_rb_var()
    
    if selection == 1:
      # Keyword search
      keyword = get_keyword_entry_var()
      query = sql__search__items_by_keyword(emailAddr, keyword)
      return (query, selection)
      
    elif selection == 2:
      # My postal code search
      query = sql__search__items_by_my_postal_code(emailAddr)
      return (query, selection)

    elif selection == 3:
      # Within X miles

      # Get miles search criteria
      miles = get_miles_sb_var()
      
      # Get users postal code
      df_user_postal_code = pd.read_sql_query(sql__search__get_postal_code_by_email(emailAddr), cnx)
      user_postal_code = df_user_postal_code['postalcode'].values[0]

      # Get lat, lon of users postal code
      df_user_lat_lon = pd.read_sql_query(sql__search__get_lat_lon_by_postal_code(user_postal_code), cnx)
      user_lat_lon = (float(df_user_lat_lon['addr_latitude'].values[0]), float(df_user_lat_lon['addr_longitude'].values[0]))
      
      # Get lat, lon of all other postal codes
      df_all_postal_codes_lat_lon = pd.read_sql_query(sql__search__get_all_postal_codes_lat_lon(), cnx)

      # Compute distance between user lat, lon and all other lat, lon
      postal_codes_distances = {}
      for _, row in df_all_postal_codes_lat_lon.iterrows():
        other_postal_code = row['postalcode']
        other_lat_lon = (float(row['addr_latitude']), float(row['addr_longitude']))
        distance = haversine(user_lat_lon[0], other_lat_lon[0], user_lat_lon[1], other_lat_lon[1])
        postal_codes_distances[other_postal_code] = distance

      # Pull out postal codes that meet search criteria
      postal_codes_match = []
      for postal_code, distance in postal_codes_distances.items():
        if distance <= int(miles):
          postal_codes_match.append(postal_code)
      
      # Get all item numbers from postal codes that meet search criterria
      query = sql__search__items_by_other_postal_code(emailAddr, ','.join(postal_codes_match))

      return(query, selection)

    elif selection == 4:
      # Other postal code
      postal_code = get_other_postal_code_entry_var()
      query = sql__search__items_by_other_postal_code(emailAddr, postal_code)
      return (query, selection)
    
    # Return false if no query is generated (no selection is made)
    return (False, 0)
  
  def process_search_query_for_item_numbers(query):
    df = pd.read_sql_query(query, cnx)
    item_numbers = df['itemNumber'].to_list()
    return item_numbers
  
  def search_results_exec():
    # Generate the correct query based on search criteria (also pull back selection, e.g., keyword, miles, etc.)
    query, selection = get_search_query()

    if selection > 0:
      # Query for item numbers
      item_numbers = process_search_query_for_item_numbers(query)

      # Get user selection value
      selection = get_selection_rb_var()

      if selection == 1:
        # Keyword search
        context = get_keyword_entry_var()

      elif selection == 2:
        # My postal code search
        df = pd.read_sql_query(sql__search__get_postal_code_by_email(emailAddr), cnx)
        context = df['postalcode'].values[0]

      elif selection == 3:
        # Within X miles
        context = get_miles_sb_var()

      elif selection == 4:
        # Other postal code
        context = get_other_postal_code_entry_var()

      search_results.search_results(emailAddr, item_numbers, selection, context)

      window.destroy()


  ########## VIEW

  # Header
  header = tk.Label(
    master=window, 
    text='Search', 
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE))
  header.grid(
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
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='ew')

  # Content
  keyword_rb = tk.Radiobutton(
    master=window,
    text='By keyword:',
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    variable=selection_rb_var,
    value=1
  ).grid(
    row=2,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  keyword_entry = ttk.Entry(
    master=window,
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    textvariable=keyword_entry_var
  )
  keyword_entry.grid(
    row=2,
    column=0,
    padx=110,
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  my_postal_code_rb = tk.Radiobutton(
    master=window,
    text='In my postal code',
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    variable=selection_rb_var,
    value=2
  ).grid(
    row=3,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  miles_rb = tk.Radiobutton(
    master=window,
    text='Within 0-999 miles of me:',
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    variable=selection_rb_var,
    value=3
  ).grid(
    row=4,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  miles_sb = ttk.Spinbox(
    master=window,
    textvariable=miles_sb_var,
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    width=3,
    from_=0,
    to=999
  ).grid(
    row=4,
    column=0,
    padx=210,
    pady=WINDOW_PADDING_Y,  
    sticky='w'
  )

  other_postal_code_rb = tk.Radiobutton(
    master=window,
    text='In postal code:',
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    variable=selection_rb_var,
    value=4
  ).grid(
    row=5,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  other_postal_code_entry = ttk.Entry(
    master=window,
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
      textvariable=other_postal_code_entry_var
  ).grid(
    row=5,
    column=0,
    padx=140,
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  # Empty row
  empty_row = tk.Label(master=window, text='\n')
  empty_row.grid(row=6, column=0)

  # Search button
  search_button = tk.Button(
    master=window, 
    text='Search!',
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE,
    ),
    command=search_results_exec)
  search_button.grid(
    row=7, 
    columnspan=10,
    padx=20, 
    pady=WINDOW_PADDING_Y,  
    sticky='e') 
  
  # Close button
  # search_button = tk.Button(
  #   master=window, 
  #   text='Close',
  #   font=(
  #     LABEL_FONT_FAMILY,
  #     LABEL_FONT_SIZE,
  #     LABEL_FONT_WEIGHT_VALUE,
  #   ),
  #   command=close_exec)
  # search_button.grid(
  #   row=7, 
  #   column=0,
  #   columnspan=10,
  #   padx=20, 
  #   pady=WINDOW_PADDING_Y,  
  #   sticky='e') 


##############################
# EVENT LOOP
##############################
# if __name__ == "__main__":
#   window.mainloop()