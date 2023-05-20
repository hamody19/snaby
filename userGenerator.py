import string
import random


class UserGenerator:
    user_names = set()
    __list_length = 50
    __user_name_length = 10

    def __init__(self, list_length: int, user_name_length):
        self.__list_length = list_length
        if user_name_length < 0 or user_name_length > 24:
            print(
                "\033[91;1m[-] user name length error TIKTOK allow the username that only consisting from 24 " +
                "letters\033[97;1m"
            )
        else:
            self.__user_name_length = user_name_length

    def get_list_length(self):
        return self.__list_length

    def get_name_length(self):
        return self.__user_name_length

    def user_name_generator(self):
        characters = string.ascii_lowercase
        while self.user_names.__len__() < self.__list_length:
            user_name = ""
            while len(user_name) < self.__user_name_length:
                user_name += random.choice(characters)
            if user_name[0] not in "._0123456789" and user_name[-1] not in "._0123456789":
                self.user_names.add(user_name)
            if user_name[0] in "._0123456789":
                user_name = user_name[1:]
            if user_name[-1] in "._0123456789":
                user_name = user_name[:-1]

