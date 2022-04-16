from global_variables import *
# from my_items import my_items
from search import search

WINDOW_TITLE = 'My Items'

def setup(title='My Window', width=800, height=400):
  window = tk.Tk()
  window.title(title)
  window.geometry(f'{width}x{height}')
  return window

window = setup(title=WINDOW_TITLE, width=WINDOW_SIZE_WIDTH, height=WINDOW_SIZE_HEIGHT)

tk.Button(window, text='Click me', command=search).pack()

window.mainloop()

# command=lambda email='keith.dowd@gmail.com': my_items(email)