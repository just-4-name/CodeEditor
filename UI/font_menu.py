import tkinter as tk
from functools import partial


def create_font_menu(main_menu, code_area):
    font_menu = tk.Menu(main_menu, tearoff=0)
    font_menu.add_command(label='increase', command=partial(code_area.change_font, 1),
                          accelerator='Ctrl+Up')
    font_menu.add_command(label='decrease', command=partial(code_area.change_font, -1),
                          accelerator='Ctrl+Down')
    main_menu.add_cascade(label='Font', menu=font_menu)
    return font_menu
