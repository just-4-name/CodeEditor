import tkinter as tk
from tkcode import CodeEditor
from resources import code_editor_settings


def valid_languages():
    return CodeEditor.languages


class CodeArea:
    MIN_FONT_SIZE = 2
    MAX_FONT_SIZE = 30

    def __init__(self, window):
        self.__window = window
        self.__code_editor = CodeEditor(window, **code_editor_settings)
        self.__code_editor.pack(fill="both", expand=True)
        self.__code_editor.bind('<Control-m>', self.__to_line_end)
        self.__code_editor.bind('<Control-n>', self.__to_line_start)

    def __to_line_end(self, e):
        line = int(self.__code_editor.index(tk.INSERT).split('.')[0])
        self.__code_editor.mark_set("insert", "%d.%d" % (line, len(self.get_text())))

    def __to_line_start(self, e):
        line = int(self.__code_editor.index(tk.INSERT).split('.')[0])
        self.__code_editor.mark_set("insert", "%d.%d" % (line, 0))

    def set_text(self, text):
        self.__code_editor.delete(1.0, tk.END)
        self.__code_editor.insert(1.0, text)

    def __update(self):
        text = self.get_text()
        self.set_text(text)

    def get_text(self):
        return self.__code_editor.get(1.0, tk.END)

    def change_font(self, delta):
        if self.MIN_FONT_SIZE < self.__code_editor.font_size + delta < self.MAX_FONT_SIZE:
            self.__code_editor.font_size += delta

    def set_language(self, language):
        self.__code_editor.language = language
        self.__update()

    def remove_tag(self):
        self.__code_editor.tag_remove("substr", "1.0", "end")

    def found_substr(self, start, end, highlight_all=False):
        if not highlight_all:
            self.remove_tag()
            self.__code_editor.mark_set("insert", "1.0+%d chars" % start)
        self.__code_editor.tag_add("substr", "1.0+%d chars" % start, "1.0+%d chars" % end)
        self.__code_editor.tag_config("substr", background="black", foreground="white")
