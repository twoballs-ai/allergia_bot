import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env файла

API_TOKEN = os.getenv('API_TOKEN')

# Настройки вебхука
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')  # Например, 'https://yourdomain.com'
WEBHOOK_PATH = '/webhook/bot'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Настройки веб-сервера
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3000

# Настройки Django API
DJANGO_API_URL = os.getenv('DJANGO_API_URL')  # Например, 'https://yourdjangoapp.com/api/'
