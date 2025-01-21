from aiogram.fsm.state import StatesGroup, State

class ImgOrText(StatesGroup):
    add = State()
    neutral = State()
