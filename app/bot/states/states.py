from aiogram import Router
from aiogram.fsm.state import default_state, State, StatesGroup


class FSMFillUserData(StatesGroup):
    fill_name = State()
    choose_goal = State()
    choose_gender = State()
    choose_activity_level = State()
    fill_current_weight = State()
    fill_current_hight = State()
    fill_birth_date = State()
    choose_region = State()

