from env import URL
import requests
from multiprocessing import Pool
from time import sleep
from colorama import init, Fore

init()


def check_username(username, save_in_file: bool):
    response = requests.get(URL + username)
    if response.status_code == 404:
        print(f"{Fore.GREEN}[+] {Fore.RESET} Valid username: {Fore.CYAN}{username}{Fore.RESET}")
        if save_in_file:
            save_usernames_in_file(username)
        return username
    elif response.status_code == 200 or response.status_code == 204:
        print(f"{Fore.RED}[-] {Fore.RESET}Invalid username: {username}")
        return None
    elif response.status_code == 429:
        for i in range(30, -1, -1):
            print("\r" + f"{Fore.RED}[!] {Fore.RESET}" +
                  f"you're being ratelimited! Sleeping for {Fore.RED}{i}{Fore.RESET}s ....", end='')
            sleep(1)
        print()
    else:
        print(f"{Fore.RED}[?] Unknown Error occurred while the program was running")
        return None
    return None


def seek_for_usernames(usernames: list, save_in_file: bool = False):
    with Pool(processes=4) as pool:
        # remember to add print result function
        result = pool.starmap(check_username, [(username, save_in_file) for username in usernames])
        display_result(result)


def save_usernames_in_file(username):
    try:
        with open("available.txt", 'a') as txtFile:
            txtFile.writelines("Valid username: " + username + '\n')
    except FileNotFoundError:
        with open("available.txt", 'w') as txtFile:
            txtFile.writelines("Valid username: " + username + '\n')


def display_result(result: list):
    print(f"{Fore.GREEN}available user names{Fore.RESET}")
    for available_username in result:
        if available_username is not None:
            print(f"{Fore.CYAN}{available_username}{Fore.RESET}")
