import asyncio
import twitter
from config import CAPSOLVER_API_KEY
from .acc_init import init_account, create_account
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

accounts_data = init_account()


async def handle_account(account_data, account_number):
    account = create_account(account_data)
    try:
        async with twitter.Client(
                account, proxy=account_data['proxy'], capsolver_api_key=CAPSOLVER_API_KEY
        ) as twitter_client:
            print(
                Fore.GREEN + f'[{account_number}] {account.username}, ({account.id}), {account.followers_count} followers, created: {account.created_at} - {account.status}')
            await asyncio.sleep(1)
        return True  # Если аккаунт обработан без исключений, он валиден
    except twitter.errors.TwitterException as e:
        print(Fore.RED + f"[{account_number}] Error with account {account.username}: {e}")
    except Exception as e:
        print(Fore.RED + f"[{account_number}] Error with account {account.username}: {e}")
    return False  # Если был exception, аккаунт не валиден


async def main():
    tasks = []
    account_number = 1
    for account_data in accounts_data:
        tasks.append(handle_account(account_data, account_number))
        account_number += 1

    results = await asyncio.gather(*tasks)
    valid_accounts_count = sum(results)
    print('')
    print(Fore.GREEN + f'The number of vaild accounts: {valid_accounts_count}')


if __name__ == "__main__":
    asyncio.run(main())
