from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import fsm.fsm
from app import keyboards as kb

from app.keyboards import help_url
from config.config import admin_id

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from tools.ML.app import recognize
from data.data_functions import words

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f'Здравствуйте,{message.from_user.first_name.capitalize()}! Задайте мне свой вопрос я постораюсь вам помочь!\n',
                         reply_markup=kb.main)
    await state.set_state(fsm.fsm.ImgOrText.neutral)


@router.message(F.text == 'Чат с оператором 💬')
async def new_record(message: Message, state: FSMContext):
    await message.answer('Грустно, что я не смог вам помочь!👋\n'
                         'Для связи с оператором нажмите на кнопку ниже\n',
                         reply_markup=help_url)

@router.message(Command(commands=['add_questions']))
async def answer_for_user(message: Message, state: FSMContext):
    if message.from_user.id == int(admin_id):
         await message.answer('Вы зашли в режим админа, для выхода используйте /start\n'
                              'Для добавления вопроса и ответа, напишите их в формате:\n'
                              'Вопрос:Ответ. Обратите внимание, символ ":" должен быть один\n')
         await state.set_state(fsm.fsm.ImgOrText.add)
    else:
        await message.answer('Вы не админ')

@router.message(fsm.fsm.ImgOrText.add)
async def generate_image(message: Message):
    key, values = message.text.split(":")
    words[key] = values
    await message.answer("Записал, пришлите еще один или используйте /start")



@router.message(fsm.fsm.ImgOrText.neutral)
async def generate_image(message: Message):
    # Обучение модели на data_set
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.values()))


    await message.answer(recognize(message.text, vectorizer, clf))

