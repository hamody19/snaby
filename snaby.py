import requests
from env import *
from multiprocessing import Pool
from userGenerator import UserGenerator
from time import sleep


def check_username(username):
    response = requests.get(URL + username)
    if response.status_code == 404:
        print(colors["green"] + f"[+]" + colors["white"] + " Valid username: " + colors["blue"] + username + colors["white"])
    elif response.status_code == 200 or response.status_code == 204:
        print(colors["red"] + f"[-]" + colors["white"] + "Invalid username: " + username)
    elif response.status_code == 429:
        for i in range(30, -1, -1):
            print(
                "\r" + colors["red"] + f"[!] " + colors["white"] +
                " you're being ratelimited! Sleeping for {red}{i}{white}s ....", end=''
            )
            sleep(1)
        print()
    else:
        print(colors["red"] + "[?] Unknown Error occur while the program run")


def check_for_valid_names():
    create_users = UserGenerator(10000, 4)
    create_users.user_name_generator()
    with Pool(processes=4) as pool:
        results = pool.map(check_username, create_users.user_names)

    with open("validUserNames.txt", 'a') as f:
        for result in results:
            if result:
                f.writelines(result + '\n')


if __name__ == "__main__":
    check_for_valid_names()

