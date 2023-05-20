from snaby import seek_for_usernames
from usernamesGenerator import UsernamesGenerator
from env import accepting
from colorama import Fore, init
init()
if __name__ == "__main__":
    number_of_names_to_generate = int(input(f"{Fore.GREEN}[+] {Fore.RESET}" +
                                            "How many user names you want to generate? : "
                                            ))
    username_length = int(input(f"{Fore.GREEN}[+] {Fore.RESET} Enter length of usernames \n" +
                                f"{Fore.RED}[-] note the usernames length shouldn't be less than 2 or " +
                                f"greater than 24 TIKTOK does not allow it :  {Fore.RESET}"))
    generate_users = UsernamesGenerator(number_of_names_to_generate, username_length)

    save_in_file = input(f"{Fore.GREEN}[+] {Fore.RESET}" +
                         "do you want to save the user names in a file? [y][yes]/[n][no] : "
                         )

    generate_users.user_name_generator()
    seek_for_usernames(generate_users.user_names, save_in_file in accepting)


