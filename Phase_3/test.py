from global_variables import *
from my_items import my_items

WINDOW_TITLE = 'My Items'

def setup(title='My Window', width=800, height=400):
  window = tk.Tk()
  window.title(title)
  window.geometry(f'{width}x{height}')
  return window

window = setup(title=WINDOW_TITLE, width=WINDOW_SIZE_WIDTH, height=WINDOW_SIZE_HEIGHT)

tk.Button(window, text='Click me', command=my_items).pack()

window.mainloop()