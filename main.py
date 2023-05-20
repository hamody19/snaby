from snaby import seek_for_usernames
from userGenerator import UserGenerator
from env import colors, accepting

if __name__ == "__main__":
    number_of_names_to_generate = int(input(colors["green"] + "[+]" + colors["white"] +
                                            "How many user names you want to generate? : "
                                            ))
    username_length = int(input(colors["green"] + "[+]" + colors["white"] + "Enter length of usernames \n" +
                                colors["red"] + "[-] note the usernames length shouldn't be less than 2 or " +
                                "greater than 24 TIKTOK does not allow it : " + colors["white"]))
    generate_users = UserGenerator(number_of_names_to_generate, username_length)

    save_in_file = input(colors["green"] + "[+]" + colors["white"] +
                         "do you want to save the user names in a file? [y][yes]/[n][no] : "
                         )

    generate_users.user_name_generator()
    seek_for_usernames(generate_users.user_names, save_in_file in accepting)


