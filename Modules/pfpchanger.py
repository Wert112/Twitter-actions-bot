import asyncio
import os
import twitter
from .acc_init import init_account, create_account
from config import CAPSOLVER_API_KEY
from colorama import init, Fore

init(autoreset=True)

accounts_data = init_account()

images_path = "./Images"
image_files = [os.path.join(images_path, f) for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

image_files = image_files[:len(accounts_data)]

async def update_pfp(account, proxy, image_path):
    async with twitter.Client(account, proxy=proxy, verify=False, capsolver_api_key=CAPSOLVER_API_KEY) as twitter_client:
        with open(image_path, "rb") as image_file:
            image = image_file.read()
            media_id = await twitter_client.upload_image(image)
            await twitter_client.update_profile_avatar(media_id)
            print(Fore.GREEN + f'Profile picture at {account.username} updated successfully')

async def main():

    if not image_files:
        print(Fore.RED + ("В папке Images нет изображений"))

    if len(image_files) < len(accounts_data):
        print(Fore.RED +f"Недостаточно изображений для всех {len(accounts_data)} аккаунтов. Количество изображений: {len(image_files)}. Пожалуйста, добавьте ещё изображения.")

    if len(image_files) >= len(accounts_data):
        tasks = []
        for account_data, image_path in zip(accounts_data, image_files):
            account = create_account(account_data)
            proxy = account_data.get('proxy')
            task = asyncio.create_task(update_pfp(account, proxy, image_path))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
