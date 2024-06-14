from Modules import tg_to_twitter, checker, follow, namechanger, pfpchanger
import asyncio
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)


def main():
    # Introduction
    print(Fore.YELLOW + "Welcome to the Twitter Bot!")
    print(Fore.YELLOW + "This bot allows you to perform various actions with your Twitter accounts.")
    print(Fore.YELLOW + "Please choose an action from the list below:")

    print("List of actions:")
    print(Fore.GREEN + "1. Tg to Twitter")
    print(Fore.GREEN + "2. Accounts Checker")
    print(Fore.GREEN + "3. Follow")
    print(Fore.GREEN + "4. Namechanger")
    print(Fore.GREEN + "5. Pfpchanger")

    choice = input("Enter the number of action: ")

    if choice == '1':
        print(Fore.GREEN + 'Please send the Twitter link to the TG bot')
        asyncio.run(tg_to_twitter.launch_tg_twitter())
    elif choice == '2':
        asyncio.run(checker.main())
        return main()
    elif choice == '3':
        asyncio.run(follow.main())
    elif choice == '4':
        asyncio.run(namechanger.main())
    elif choice == '5':
        asyncio.run(pfpchanger.main())
    else:
        print(Fore.RED + "Invalid input. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
