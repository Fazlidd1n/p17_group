import asyncio
import logging
import sys

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = '6334253807:AAHuBzG7B-hIlQw41Fw2TTYHiWaQ1XxF6lY'
dp = Dispatcher(storage=MemoryStorage())


class BTN(StatesGroup):
    btn1 = State()
    btn2 = State()
    btn3 = State()


def button1():
    btn1 = KeyboardButton(text="btn1")
    return ReplyKeyboardMarkup(keyboard=[[btn1]], resize_keyboard=True, one_time_keyboard=True)


def button2():
    btn2 = KeyboardButton(text='btn2')
    back = KeyboardButton(text='back')
    return ReplyKeyboardMarkup(keyboard=[[btn2, back]], resize_keyboard=True, one_time_keyboard=True)

def button3():
    btn3 = KeyboardButton(text='btn3')
    btn4 = KeyboardButton(text='btn4')
    back = KeyboardButton(text='back')
    return ReplyKeyboardMarkup(keyboard=[[btn3, btn4, back]], resize_keyboard=True, one_time_keyboard=True)


@dp.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(f"Hello {msg.from_user.full_name}")
    await msg.answer("Buttonlardan birini talang ⤵️", reply_markup=button1())
    await state.set_state(BTN.btn1)


@dp.message(BTN.btn1)
async def btn_handler(msg: Message, state: FSMContext):
    await msg.answer(text='Buttonlardan birini talang ⤵️', reply_markup=button2())
    await state.set_state(BTN.btn2)


@dp.message(BTN.btn2)
async def btn_handler(msg: Message, state: FSMContext):
    if msg.text == 'btn2':
        await msg.answer("Buttonlardan birini talang ⤵️", reply_markup=button3())
        await state.set_state(BTN.btn3)
    elif msg.text == 'back':
        await msg.answer("Buttonlardan birini talang ⤵️", reply_markup=button1())
        await state.set_state(BTN.btn1)


@dp.message(BTN.btn3)
async def btn_handler(msg: Message, state: FSMContext):
    if msg.text == 'btn3':
        await msg.answer("Tugadi ❗️", reply_markup=button3())
        await state.set_state(BTN.btn3)
    elif msg.text == 'btn4':
        await msg.answer("Tugadi ❗️", reply_markup=button3())
        await state.set_state(BTN.btn3)
    elif msg.text == 'back':
        await msg.answer("Buttonlardan birini talang ⤵️", reply_markup=button2())
        await state.set_state(BTN.btn2)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
