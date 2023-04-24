import tkinter as tk
from utils.text_replacer import replace
from utils.text_searcher import TextSearcher


def create_find_replace_menu(code_area, main_menu):
    find_replace_menu = tk.Menu(main_menu, tearoff=0)
    find_replace_menu.add_command(label='replace', command=lambda: create_text_replace_menu(code_area))
    find_replace_menu.add_command(label='find', command=lambda: create_find_menu(code_area),
                                  accelerator='Ctrl+F')
    main_menu.add_cascade(label='Find/Replace', menu=find_replace_menu)
    return find_replace_menu


def create_text_replace_menu(code_area):
    top_window = tk.Toplevel()
    top_window.geometry('+850+0')
    old_str = tk.StringVar()
    new_str = tk.StringVar()
    old_substr_label = tk.Label(top_window, text='Enter substr-to-change:')
    new_substr_label = tk.Label(top_window, text='Enter new-substr:')
    old_substr_entry = tk.Entry(top_window, textvariable=old_str)
    new_substr_entry = tk.Entry(top_window, textvariable=new_str)
    results_info = tk.Label(top_window, text='0 results')
    highlighter = Highlighter(code_area, old_str, results_info)
    old_substr_entry.bind('<KeyRelease>', highlighter.update)
    old_substr_label.pack(fill='x')
    old_substr_entry.pack(fill='x')
    new_substr_label.pack(fill='x')
    new_substr_entry.pack(fill='x')
    results_info.pack(fill='x')
    replace_button = tk.Button(top_window, text="Replace",
                               command=lambda: replace(code_area, old_str.get(), new_str.get()))
    replace_button.pack(fill='x')


class Highlighter:
    def __init__(self, code_area, substr, results_info):
        self.__substr = substr
        self.__text_searcher = TextSearcher(results_info, code_area)

    def update(self, e):
        self.__text_searcher.highlight_all_occurences(self.__substr.get())


def update(code_area, substr, results_info, e):
    print(substr.get())
    text_searcher = TextSearcher(results_info, code_area)
    text_searcher.highlight_all_occurences(substr.get())


def create_find_menu(code_area):
    top_window = tk.Toplevel()
    top_window.geometry('+850+0')
    text = tk.StringVar()
    entry = tk.Entry(top_window, textvariable=text)
    results_info = tk.Label(top_window, text='0 results')
    text_searcher = TextSearcher(results_info, code_area)
    entry.pack(fill='x')

    button_prev = tk.Button(top_window, text="<-", command=lambda: text_searcher.find_prev(text.get()))
    button_prev.pack(fill='x')
    button_next = tk.Button(top_window, text="->", command=lambda: text_searcher.find_next(text.get()))
    button_next.pack(fill='x')
    results_info.pack(fill='x')
