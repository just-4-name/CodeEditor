import tkinter as tk
from UI.code_area import CodeArea
from UI.syntax_menu import create_syntax_menu
from utils.file_manager import FileManager
from UI.font_menu import create_font_menu
from UI.file_menu import create_file_menu
from UI.find_replace_menu import create_find_replace_menu, create_find_menu
from utils.singleton import Singleton


class Window:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title('Current file: None')
        self.__window.geometry('1000x800+0+0')
        self.__code_area = CodeArea(self.__window)
        self.__file_manager = FileManager(self.__window)
        self.__main_menu = tk.Menu(self.__window)
        self.__window.config(menu=self.__main_menu)
        self.__file_menu = create_file_menu(self.__window, self.__main_menu, self.__file_manager, self.__code_area)
        self.__font_menu = create_font_menu(self.__main_menu, self.__code_area)
        self.__syntax_menu = create_syntax_menu(self.__main_menu, self.__code_area)
        self.__find_replace_menu = create_find_replace_menu(self.__code_area, self.__main_menu)
        self.__window.bind_all('<Control-s>', self.__save)
        self.__window.bind_all('<Control-w>', self.__save_as)
        self.__window.bind_all('<Control-o>', self.__open_file)
        self.__window.bind_all('<Control-x>', self.quit)
        self.__window.bind_all('<Control-Up>', self.__increase_font)
        self.__window.bind_all('<Control-Down>', self.__decrease_font)
        self.__window.bind_all('<Control-f>', self.__find_substr)
        self.__window.mainloop()

    def __find_substr(self, e):
        create_find_menu(self.__code_area)

    def __open_file(self, e): self.__file_manager.open_file(self.__code_area)

    def __save(self, e): self.__file_manager.save(self.__code_area)

    def __save_as(self, e): self.__file_manager.save_as(self.__code_area)

    def quit(self, e): self.__window.quit()

    def __increase_font(self, e): self.__code_area.change_font(1)

    def __decrease_font(self, e): self.__code_area.change_font(-1)
