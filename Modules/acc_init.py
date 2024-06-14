import random
import sys
import asyncio
import os
import twitter

def init_account():
    if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    base_dir = os.path.dirname(os.path.abspath(__file__))
    accounts_path = os.path.join(base_dir, '../accounts.txt')
    proxy_path = os.path.join(base_dir, '../proxy.txt')

    with open(accounts_path, 'r') as file:
        accounts = file.read().splitlines()

    with open(proxy_path, 'r') as file:
        proxies = file.read().splitlines()

    accounts_data = []
    for account_info in accounts:
        account_fields = account_info.split(':')
        if len(account_fields) == 1:
            auth_token = account_fields[0].strip()
            account_data = {
                'auth_token': auth_token,
                'username': None,
                'password': None,
                'email': None,
                'proxy': None
            }
        else:
            username, password, email, auth_token = account_fields
            account_data = {
                'auth_token': auth_token.strip(),
                'username': username.strip(),
                'password': password.strip(),
                'email': email.strip(),
                'proxy': None
            }

        accounts_data.append(account_data)

    for i, account in enumerate(accounts_data):
        if i < len(proxies):
            account['proxy'] = proxies[i]
        else:
            account['proxy'] = random.choice(proxies)

    return accounts_data

def create_account(account_data):
    return twitter.Account(
        auth_token=account_data['auth_token'],
        ct0=None,
        id=None,
        name=None,
        username=account_data['username'],
        password=account_data['password'],
        email=account_data['email'],
        key2fa=None,
        backup_code=None
    )
