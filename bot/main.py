import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web
from aiogram.types import Update
from config import API_TOKEN, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH
from handlers import start, registration
from aiogram.enums import ParseMode

async def on_startup(app: web.Application):
    logging.info('Устанавливаем вебхук...')
    bot: Bot = app['bot']
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(app: web.Application):
    logging.info('Удаляем вебхук...')
    bot: Bot = app['bot']
    await bot.delete_webhook()
    await bot.session.close()


async def handle_webhook(request: web.Request):
    try:
        data = await request.json()
        update = Update(**data)
        bot: Bot = request.app['bot']
        dp: Dispatcher = request.app['dispatcher']
        await dp.feed_update(bot, update)
        return web.Response()
    except Exception as e:
        logging.error(f"Ошибка при обработке вебхука: {e}")
        return web.Response(status=500, text="Internal Server Error")


def create_app() -> web.Application:
    app = web.Application()
    
    # Инициализация бота с использованием DefaultBotProperties
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    
    # Сохранение бота и диспетчера в приложении для доступа в других местах
    app['bot'] = bot
    app['dispatcher'] = dp
    
    # Регистрация обработчиков
    dp.include_router(start.router)
    dp.include_router(registration.router)
    
    # Регистрация маршрута вебхука
    app.router.add_post(WEBHOOK_PATH, handle_webhook)
    
    # Регистрация функций старта и завершения
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    
    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
