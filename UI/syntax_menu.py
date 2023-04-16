import tkinter as tk
from functools import partial
from UI.code_area import valid_languages


def create_syntax_menu(main_menu, code_area):
    syntax_menu = tk.Menu(main_menu, tearoff=0)
    for language in valid_languages():
        syntax_menu.add_command(label=language, command=partial(code_area.set_language, language))
    main_menu.add_cascade(label='Syntax', menu=syntax_menu)
    return syntax_menu
