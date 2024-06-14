import asyncio
import random
import twitter
from colorama import init, Fore
from config import CAPSOLVER_API_KEY, list_of_new_usernames
from .acc_init import init_account, create_account

init(autoreset=True)


accounts_data = init_account()

new_usernames = list_of_new_usernames


async def change_username(account, proxy, sleep_duration, used_usernames):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        try:
            for username in new_usernames:
                if username not in used_usernames:
                    used_usernames.add(username)
                    await asyncio.sleep(10)
                    old_username = account.username
                    await twitter_client.change_username(username)
                    print(Fore.GREEN + f'{old_username} changed username to {username} successfully')

                    # Update the username in the .env file
                    set_key('../.env', f'USERNAME_{account.username_index}', username)
                    break
                else:
                    print(Fore.RED + f"{account.username}: Username {username} is already used, skipping.")
        except Exception as e:
            await asyncio.sleep(10)
            print(Fore.RED + f"{account.username}: Error occurred while changing username: {e}")

async def main():
    if len(list_of_new_usernames) == 0:
        print(Fore.RED + 'Please add names you want to use for changing in confing.py')

    if len(list_of_new_usernames) < len(accounts_data):
        print(Fore.RED +f"Not enough new usernames for all {len(accounts_data)} accounts. The number of usernames: {len(list_of_new_usernames)}. Please,add more usernames.")

    if len(list_of_new_usernames) >= len(accounts_data):
        tasks = []
        used_usernames = set()
        for i, account_data in enumerate(accounts_data):
            account_data['username_index'] = str(i + 1)
            account = create_account(account_data)
            proxy = account_data.get('proxy')
            sleep_duration = random.randint(1, 10)
            task = asyncio.create_task(change_username(account, proxy, sleep_duration, used_usernames))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    main()
