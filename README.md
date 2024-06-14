# Twitter Bot

Welcome to the Twitter Bot! This bot allows you to perform various actions with your Twitter accounts, including transferring tweets from Telegram to Twitter, checking account statuses, following accounts, changing usernames, and updating profile pictures.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Actions](#actions)
  - [Tg to Twitter](#tg-to-twitter)
  - [Accounts Checker](#accounts-checker)
  - [Follow](#follow)
  - [Namechanger](#namechanger)
  - [Pfpchanger](#pfpchanger)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.7 or higher
- Required Python packages:
  - asyncio
  - colorama
  - tweepy-self

Ensure you have the necessary API keys and tokens for CapSolver and Telegram.

## Installation

- Clone the repository or download the script

- Install the required Python packages:
    ```bash
    pip install asyncio colorama
    ```

- Set your CapSolver API key, Telegram Bot Token, and Telegram Chat ID in the script

## Configuration

- **CapSolver API Key**: Used for various automated tasks
  ```python
  CAPSOLVER_API_KEY = 'your_capsolver_api_key'


**Telegram Bot Toke**: Needed to interact with the Telegram API

TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'

**Telegram Chat ID**: The ID of the Telegram chat where the bot will send messages
TELEGRAM_CHAT_ID = 'your_telegram_chat_id'

**Number of Likes/Retweets/Replies/Quotes**: Configure how many likes, retweets, replies, and quotes the bot should perform. Setting a value to 0 means the action will not be performed


NUM_LIKES = 1
NUM_RETWEETS = 1
NUM_REPLIES = 0
NUM_QUOTES = 0

**Delay Between Actions**: Set the minimum and maximum delay between bot actions in seconds

MIN_DELAY = 10
MAX_DELAY = 30

**Accounts to Follow**: List of accounts the bot should follow

list_of_accounts_to_follow = [
    'ElonMusk', 'ElonMusk2',
]

**New Usernames**: List of new usernames for the namechanger module


list_of_new_usernames = [
    'New_username1', 'New_username2'
]

## Usage

**Run the script**:

python main.py

## Actions

**Tg to Twitter**
Transfers tweets from Telegram to Twitter. Requires you to send the Twitter link to the Telegram bot.

**Accounts Checker**
Checks the status of Twitter accounts.

**Follow**
Follows the accounts listed in list_of_accounts_to_follow.

**Namechanger**
Changes the username of your Twitter account to one of the names listed in list_of_new_usernames.

**Pfpchanger**
Changes the profile picture of your Twitter account to one of the puctures from **Images** folder. 

## Contributing

Feel free to submit issues and pull requests for new features, bug fixes, or enhancements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
