from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import (CallbackQuery, Message)
from states.states import FSMFillUserData
from keyboards import keyboards


router = Router()

@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text="Привет! Этот бот помогает вам считать калории, а также худеть или набирать вес"
    )

@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.asnwer(
        text="Вы вышли из состояния заполнения анкеты\n,"
        "Отправьте команду /fillform, чтобы начать заново."
    )

@router.message(Command(commands="fillform"), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста, введите Ваше имя.")
    await state.set_state(FSMFillUserData.fill_name)

@router.message(StateFilter(FSMFillUserData.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Спасибо! Теперь выберите вашу цель.")
    await state.set_state(FSMFillUserData.choose_goal)

@router.message(StateFilter(FSMFillUserData.fill_name))
async def warning_not_name(message: Message):
    await message.answer("Вы ввели не имя.\n"
                         "Введите, пожалуйста, имя или команду /cancel,"
                         "если хотите прервать заполнение анкеты.")
    
@router.message(StateFilter(FSMFillUserData.choose_goal))
async def process_goal_choosing(message: Message, state: FSMContext):
    await message.answer(text="Выберите цель:",
                            reply_markup=keyboards.create_goal_keyboard())
    
@router.callback_query(F.data == "lose_weight_pressed")
async def process_lose_weight_pressed(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Сколько веса вы бы хотели потерять?"
    )
    await callback.answer()
    await state.set_state(FSMFillUserData.fill_weight_to_lose)

@router.message(StateFilter(FSMFillUserData.fill_weight_to_lose))
async def process_weight_to_lose(message: Message, state: FSMContext):
    if not message.text.isdigit():
        message.answer(text="Введите, пожалуйста, вес цифрами.")
    await message.answer(text="")







    

    

    
