from aiogram.dispatcher.filters.state import StatesGroup, State

class Article(StatesGroup):
    articles = State()


def lang(data:str):
    language = ['uz', 'en', 'ru']
