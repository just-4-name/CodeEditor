import tkinter as tk


def create_file_menu(window, main_menu, file_manager, code_area):
    file_menu = tk.Menu(main_menu, tearoff=0)
    file_menu.add_command(label='open', command=lambda: file_manager.__open_file(code_area),
                          accelerator='Ctrl+O')
    file_menu.add_command(label='save', command=lambda: file_manager.__save(code_area),
                          accelerator='Ctrl+S')
    file_menu.add_command(label='save as', command=lambda: file_manager.___save_as(code_area),
                          accelerator='Ctrl+W')
    file_menu.add_command(label='exit', command=window.quit, accelerator='Ctrl+X')
    main_menu.add_cascade(label='File', menu=file_menu)
    return file_menu
