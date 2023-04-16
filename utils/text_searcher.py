class TextSearcher:
    def __init__(self, label, code_area):
        self.__pos = None
        self.__search_string = ''
        self.__label = label
        self.__code_area = code_area

    def find_next(self, string, highlight_all=False):
        text = self.__code_area.get_text()
        if self.__pos is None or string != self.__search_string:
            self.__pos = 0
        else:
            self.__pos = (self.__pos + len(string)) % len(text)
        self.__search_string = string
        ind = text.find(string, self.__pos)
        if ind == -1:
            ind = text.find(string)
        if ind != -1 and string != '':
            self.__pos = ind
            self.__label.config(text=f'{text.count(string, 0, ind + 1)}/{text.count(string)}')
            self.__code_area.found_substr(ind, ind + len(string), highlight_all)
        else:
            self.__label.config(text='0 results')

    def find_prev(self, string):
        text = self.__code_area.get_text()
        if self.__pos is None or string != self.__search_string:
            self.__pos = 0
        self.__search_string = string
        ind = text.rfind(string, 0, self.__pos)
        if ind == -1:
            ind = text.rfind(string)
        if ind != -1 and string != '':
            self.__pos = ind
            self.__label.config(text=f'{text.count(string, 0, ind + 1)}/{text.count(string)}')
            self.__code_area.found_substr(ind, ind + len(string))
        else:
            self.__label.config(text='0 results')

    def highlight_all_occurences(self, string):
        self.__code_area.remove_tag()
        content = self.__code_area.get_text()
        for i in range(content.count(string)):
            self.find_next(string, True)
