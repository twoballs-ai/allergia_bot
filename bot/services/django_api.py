import logging
from typing import Optional
import aiohttp
from config import DJANGO_API_URL

class DjangoAPI:
    def __init__(self):
        self.base_url = DJANGO_API_URL
        self.session = aiohttp.ClientSession()

    async def is_user_registered(self, telegram_id: int) -> bool:
        url = f"{self.base_url}users/{telegram_id}/"
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    return True
                elif response.status == 404:
                    return False
                else:
                    logging.error(f"Ошибка при проверке регистрации пользователя: {response.status}")
                    return False
        except Exception as e:
            logging.error(f"Исключение при проверке регистрации пользователя: {e}")
            return False

    async def register_user(self, telegram_id: int, username: str) -> bool:
        url = f"{self.base_url}users/register/"
        payload = {
            'telegram_id': telegram_id,
            'username': username,
        }
        headers = {'Content-Type': 'application/json'}
        try:
            async with self.session.post(url, json=payload, headers=headers) as response:
                if response.status == 201:
                    return True
                else:
                    logging.error(f"Ошибка при регистрации пользователя: {response.status}")
                    return False
        except Exception as e:
            logging.error(f"Исключение при регистрации пользователя: {e}")
            return False

    async def close(self):
        await self.session.close()
