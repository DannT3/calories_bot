import logging
import asyncio
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import user_handlers

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    logger.info('Starting bot')
    
    config: Config = load_config()

    
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(user_handlers)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

    


    