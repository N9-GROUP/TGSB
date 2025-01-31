import asyncio
import json
import logging
import sys

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

sys.path.append("../")
from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp


async def developer_panel():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="🚀 Service management", callback_data="service_ctrl"
        )
    )
    builder.add(types.InlineKeyboardButton(text="💬 SMS spam (beta)", callback_data="sms_spam"))
    builder.adjust(1)

    logger.debug("Create developer panel")

    return builder.as_markup()
