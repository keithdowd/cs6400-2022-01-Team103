from global_variables import *


def search(emailAddr):
  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_SIZE_HEIGHT = 275
  WINDOW_SIZE_WIDTH = 400
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
  selection_rb = tk.IntVar()

  keyword_rb = tk.Radiobutton(
    master=window,
    text='By keyword:',
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    variable=selection_rb,
    value=1
  ).grid(
    row=2,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  keyword_entry = tk.Entry(
    master=window
  ).grid(
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
    variable=selection_rb,
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
    text='Within X miles of me:',
    font=(
      LABEL_FONT_FAMILY, 
      LABEL_FONT_SIZE, 
      LABEL_FONT_WEIGHT_VALUE),
    variable=selection_rb,
    value=3
  ).grid(
    row=4,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  miles_sb = tk.Spinbox(
    master=window,
    width=3,
    from_=0,
    to=999
  ).grid(
    row=4,
    column=0,
    padx=180,
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
    variable=selection_rb,
    value=4
  ).grid(
    row=5,
    column=0,
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w'
  )

  other_postal_code_entry = tk.Entry(
    master=window
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
    ))
  search_button.grid(
    row=7, 
    columnspan=10,
    padx=20, 
    pady=WINDOW_PADDING_Y,  
    sticky='e') 

  # command=lambda item_number=my_item[0]: view_item(item_number)


##############################
# EVENT LOOP
##############################
# if __name__ == "__main__":
#   window.mainloop()