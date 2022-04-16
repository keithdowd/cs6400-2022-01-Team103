from global_variables import *

keyword = 'tech'

##############################
# CONFIGURATION
##############################

# Window
WINDOW_SIZE_HEIGHT = 400
WINDOW_SIZE_WIDTH = 600
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


##############################
# SEARCH RESULTS
##############################

########## DATA

columns = [
    'Item #',
    'Game Type',
    'Title',
    'Condition',
    'Description',
    'Distance'
  ]

########## VIEW

# Header
header = tk.Label(
  master=window, 
  text=f'Search results: keyword "{keyword}"', 
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

# Results table


##############################
# EVENT LOOP
##############################
if __name__ == "__main__":
  window.mainloop()