from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State


storage = MemoryStorage()


class FSMGifRegister(StatesGroup):
    gif_id = State()
    gif_tag = State()
