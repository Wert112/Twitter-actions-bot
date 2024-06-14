import asyncio
import os
import random
import re
import aiohttp
import twitter
from colorama import init, Fore

from config import *
from .acc_init import init_account, create_account

init(autoreset=True)
#####################################################

accounts_data = init_account()

# Read comments dictionary
base_dir = os.path.dirname(os.path.abspath(__file__))
comments_path = os.path.join(base_dir, '../comments.txt')

with open(comments_path, 'r') as file:
    commentsList = file.read().splitlines()

#####################################################

async def like(account, url, proxy, sleep_duration):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        tweet_id = re.search(r'/status/(\d+)', url).group(1)
        await asyncio.sleep(sleep_duration)
        await twitter_client.like(tweet_id)
        print(Fore.GREEN + f'Liked {tweet_id} with {account.username}')

async def retweet(account, url, proxy, sleep_duration):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        tweet_id = re.search(r'/status/(\d+)', url).group(1)
        await asyncio.sleep(sleep_duration)
        await twitter_client.repost(tweet_id)
        print(Fore.GREEN + f'Retweeted {tweet_id} with {account.username}')

async def reply(account, url, proxy, sleep_duration):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        random_comment = random.choice(commentsList)
        tweet_id = re.search(r'/status/(\d+)', url).group(1)
        await asyncio.sleep(sleep_duration)
        await twitter_client.reply(tweet_id, random_comment, media_id=None)
        print(Fore.GREEN + f'Commented {tweet_id} with {account.username}')

async def quote(account, url, proxy, sleep_duration):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        random_comment = random.choice(commentsList)
        tweet_id = re.search(r'/status/(\d+)', url).group(1)
        await asyncio.sleep(sleep_duration)
        await twitter_client.quote(tweet_url=url, text=random_comment)
        print(Fore.GREEN + f'Quoted {tweet_id} with text: {random_comment} with {account.username}')

#####################################################

async def like_random_accounts(url, num_accounts=NUM_LIKES):
    accounts_to_use = random.sample(accounts_data, num_accounts)
    tasks = []
    for account_data in accounts_to_use:
        account = create_account(account_data)
        proxy = account_data['proxy']
        sleep_duration = random.randint(MIN_DELAY, MAX_DELAY)
        tasks.append(like(account, url, proxy, sleep_duration))
    await asyncio.gather(*tasks)

async def retweet_random_accounts(url, num_accounts=NUM_RETWEETS):
    accounts_to_use = random.sample(accounts_data, num_accounts)
    tasks = []
    for account_data in accounts_to_use:
        account = create_account(account_data)
        proxy = account_data['proxy']
        sleep_duration = random.randint(MIN_DELAY, MAX_DELAY)
        tasks.append(retweet(account, url, proxy, sleep_duration))
    await asyncio.gather(*tasks)

async def reply_random_accounts(url, num_accounts=NUM_REPLIES):
    accounts_to_use = random.sample(accounts_data, num_accounts)
    tasks = []
    for account_data in accounts_to_use:
        account = create_account(account_data)
        proxy = account_data['proxy']
        sleep_duration = random.randint(MIN_DELAY, MAX_DELAY)
        tasks.append(reply(account, url, proxy, sleep_duration))
    await asyncio.gather(*tasks)

async def quote_random_accounts(url, num_accounts=NUM_QUOTES):
    accounts_to_use = random.sample(accounts_data, num_accounts)
    tasks = []
    for account_data in accounts_to_use:
        account = create_account(account_data)
        proxy = account_data['proxy']
        sleep_duration = random.randint(MIN_DELAY, MAX_DELAY)
        tasks.append(quote(account, url, proxy, sleep_duration))
    await asyncio.gather(*tasks)

#####################################################
