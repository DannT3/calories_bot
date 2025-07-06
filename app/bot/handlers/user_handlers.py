from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from states.states import FSMFillUserData


r = Router()

@r.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text="Привет! Этот бот помогает вам считать калории, а также худеть или набирать вес"
    )

@r.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.asnwer(
        text="Вы вышли из состояния заполнения анкеты\n,"
        "Отправьте команду /fillform, чтобы начать заново."
    )

@r.message(Command(commands="fillform"), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста, введите Ваше имя.")
    await state.set_state(FSMFillUserData.fill_name)

@r.message(StateFilter(FSMFillUserData.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Спасибо! Теперь выберите вашу цель.")
    await state.set_state(FSMFillUserData.choose_goal)

@r.message(StateFilter(FSMFillUserData.fill_name))
async def warning_not_name(message: Message):
    await message.answer("Вы ввели не имя.\n"
                         "Введите, пожалуйста, имя или команду /cancel,"
                         "если хотите прервать заполнение анкеты.")

    
