import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from lzt import LolzteamApi
import messages
import inline_keyboard
import warnings
warnings.filterwarnings("ignore")


with open("auth") as f:
    auth = f.read().split('\n')
BOT_API_TOKEN = auth[2]
with open("ids") as f:
    VAL = list(map(int, f.read().split('\n')))
not_origin = [
    'stealer',
    'fishing',
    'brute',
    'resale',
    'personal',
    'retrive',
    'autoreg',
]

filter1 = {'min_age': 15, 'vk_friend_min': 40, 'not_origin[]': not_origin[4:]}
STOP = 1
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)

api = LolzteamApi(auth[0], int(auth[1]))


@dp.message_handler(commands=['start'])
async def show_hello(message: types.Message):
    await message.answer(text=messages.hello())


@dp.message_handler(commands=['start_ch'])
async def start_checker(message: types.Message):
    global STOP
    STOP = 1

    async def checker():
        def isi(items: dict):
            valids = []
            for item in items:
                if item["vk_id"] in VAL:
                    valids.append("https://lzt.market/" + str(item["item_id"]) + "\n" + item["accountLink"])
            return valids

        while STOP:
            accs = api.market_list(category="vkontakte", optional=filter1)
            valid = isi(accs['items'])
            if len(valid) > 0:
                await message.answer(text=' '.join(valid))
            await asyncio.sleep(3.3)

    task_wait = asyncio.create_task(checker())
    await message.answer(text=messages.started())
    await task_wait


@dp.message_handler(commands=['stop_ch'])
async def start_checker(message: types.Message):
    global STOP
    STOP = 0
    await message.answer(text=messages.stop())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

