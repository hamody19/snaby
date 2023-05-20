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
        # the length of user name list how many users contain
        characters = string.ascii_lowercase + "_." + string.digits
        while self.user_names.__len__() < self.__list_length:
            self.user_names. \
                add("".
                    join(random.choice(characters) for _ in range(self.__user_name_length)))
