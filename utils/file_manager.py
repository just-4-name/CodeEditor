from tkinter.filedialog import askopenfilename, asksaveasfilename
from resources import extensions
from os import path


class FileManager:
    __current_file_path = None

    def __init__(self, window):
        self.__window = window

    def open_file(self, code_area, initial_dir='.'):
        self.__current_file_path = askopenfilename(filetypes=extensions, initialdir=initial_dir)
        if self.__current_file_path is None or self.__current_file_path == '':
            return
        with open(self.__current_file_path, 'r') as file:
            content = file.read()
        code_area.set_text(content)
        self.__update_title()
        self.__update_syntax(code_area)

    def save(self, code_area):
        if self.__current_file_path is None:
            self.save_as(code_area)
            return
        with open(self.__current_file_path, 'w') as file:
            file.write(code_area.get_text())
        self.__update_syntax(code_area)

    def save_as(self, code_area, initial_dir='.'):
        new_path = asksaveasfilename(filetypes=extensions, initialdir=initial_dir)
        if new_path is None or new_path == '':
            return
        self.__current_file_path = new_path
        with open(self.__current_file_path, 'w') as file:
            file.write(code_area.get_text())
        self.__update_title()
        self.__update_syntax(code_area)

    def __update_title(self):
        self.__window.title(f'current file: {self.__current_file_path}')

    def __update_syntax(self, code_area):
        current_extension = path.splitext(self.__current_file_path)[1]
        for language, extension in extensions:
            if current_extension == extension:
                code_area.set_language(language)
