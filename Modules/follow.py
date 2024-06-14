import asyncio
import random
import twitter
from config import CAPSOLVER_API_KEY, list_of_accounts_to_follow
from .acc_init import init_account, create_account
from colorama import init, Fore

init(autoreset=True)

accounts_data = init_account()
all_usernames_to_follow = list_of_accounts_to_follow

async def follow(account, usernames_to_follow, proxy):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        daily_follow_count = 0
        max_daily_follows = 4
        while daily_follow_count < max_daily_follows and usernames_to_follow:
            username = random.choice(usernames_to_follow)
            try:
                user_id = await twitter_client.request_user_by_username(username=username)
                await twitter_client.follow(user_id)
                print(Fore.GREEN + f'{account.username} followed account {username} successfully')
                daily_follow_count += 1
                usernames_to_follow.remove(username)
            except Exception as e:
                print(Fore.RED + f"{account.username}: Error occurred while following {username}: {e}")
            # Добавляем случайную задержку от 10 до 30 секунд
            await asyncio.sleep(random.uniform(10, 30))

async def main():
    tasks = []
    for account_data in accounts_data:
        account = create_account(account_data)
        proxy = account_data.get('proxy')
        usernames_to_follow = all_usernames_to_follow.copy()
        task = asyncio.create_task(follow(account, usernames_to_follow, proxy))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    main()