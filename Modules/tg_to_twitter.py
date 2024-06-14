import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import re
from Modules import twitterfunc
from config import TELEGRAM_BOT_TOKEN
from colorama import init, Fore

init(autoreset=True)

twitter_link_regex = r'https?://x.com/\w+/status/\d+'

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(Fore.BLUE + f"Received message: {text}")

    if re.match(twitter_link_regex, text):
        try:
            await twitterfunc.like_random_accounts(text)
        except Exception as like_error:
            logging.error(Fore.RED + f"Error liking tweet: {like_error}")

        try:
            await twitterfunc.retweet_random_accounts(text)
        except Exception as retweet_error:
            logging.error(Fore.RED + f"Error retweeting tweet: {retweet_error}")

        try:
            await twitterfunc.reply_random_accounts(text)
        except Exception as reply_error:
            logging.error(Fore.RED + f"Error replying to tweet: {reply_error}")

        try:
            await twitterfunc.quote_random_accounts(text)
        except Exception as quote_error:
            logging.error(Fore.RED + f"Error quoting tweet: {quote_error}")

        print(Fore.CYAN + "All twitter actions succeeded! Waiting  for a new link to tg bot")

    else:
        logging.info(Fore.RED + "Message does not contain a Twitter link")

def launch_tg_twitter():
    logging.getLogger("telegram.ext").setLevel(logging.ERROR)
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    msg_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    application.add_handler(msg_handler)

    application.run_polling()
    application.run_polling()

if __name__ == "__main__":
    launch_tg_twitter()