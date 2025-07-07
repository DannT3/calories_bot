from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                                            CallbackQuery)


def create_goal_keyboard() -> InlineKeyboardMarkup:
    button_lose_weight = InlineKeyboardButton(text="Сбросить вес",
                                                                            callback_data="lose_weight_pressed")
    button_keep_weight = InlineKeyboardButton(text="Сохранить вес",
                                                                            callback_data="keep_weight_pressed")
    button_gain_weight = InlineKeyboardButton(text="Набрать вес",
                                                                            callback_data="gain_weight_pressed")
    goal_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button_lose_weight,
                                    button_gain_weight,
                                     button_gain_weight ]]
    )


def create_gender_buttons() -> InlineKeyboardMarkup:
    male_button = InlineKeyboardButton(text="М",
                                                                callback_data="male_presse")
    female_button = InlineKeyboardButton(text="Ж",
                                                                    callback_data="female pressed")
    gender_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[male_button,
                                female_button]]
    )
    



