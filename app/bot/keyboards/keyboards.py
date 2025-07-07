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

    

    



