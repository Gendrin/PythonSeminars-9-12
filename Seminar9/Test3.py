import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
API_TOKEN = '5664442295:AAGp5Zv0mdVbKJCwRqd9Fc3qdI3zUobl-UM'
bot = Bot(token=API_TOKEN)
#bot = Bot(token="12345678:AaBbCcDdEeFfGgHh")
# Диспетчер
#dp = Dispatcher()
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Хэндлер на команду /test1
@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /test2
@dp.message_handler(commands=["test2"])
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    #dp.message_handler().register(cmd_test2, commands=["test2"])