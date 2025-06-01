from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatType

router = Router()


@router.message(Command("help"), F.chat.type == ChatType.PRIVATE)
async def help_command(message: Message):
    await send_help(message)


@router.message(F.text.lower() == "команды", F.chat.type == ChatType.PRIVATE)
async def help_text(message: Message):
    await send_help(message)


async def send_help(message: Message):
    help_text = (
        "📋 <b>Справка по командам бота-менеджера:</b>\n"
        "Команды можно вводить с префиксом <code>/</code> или <code>!</code>.\n\n"
        "<u>🔹 Приватный режим</u>:\n"
        "/start — стартовое меню и выбор чатов для управления\n"
        "/help, команды — эта справка\n\n"
        "<u>⚙️ Управление чатом (только для админов)</u>:\n"
        "/rules — показать правила чата\n"
        "/setup — регистрация чата для управления\n"
        "/ban <code>@username|reply</code> — забанить пользователя\n"
        "/unban <code>@username|reply</code> — разбанить пользователя\n"
        "/mute <code>@username|reply</code> <code>часы</code> — замутить пользователя\n"
        "/unmute <code>@username|reply</code> — размутить пользователя\n"
        "/checkperms <code>@username|reply</code> — проверить права пользователя\n"
        "/ro — переключить режим только для чтения\n"
        "/resetwarn <code>@username|reply</code> — обнулить варны пользователя\n"
        "/resetwarnsall — обнулить все варны в чате\n"
        "/setwelcomedelete <code>секунд</code> — задать таймаут авто-удаления приветствия\n"
        "/getwelcomedelete — показать текущую настройку авто-удаления\n"
        "/setkw <code>слово</code> — добавить ключевое слово в фильтр\n"
        "/remfromkw <code>слово</code> — удалить ключевое слово из фильтра\n"
        "/listkw — показать все ключевые слова\n"
        "/demon — включить Devil mode (только с матами)\n"
        "/demoff — выключить Devil mode\n"
        "/weather <code>город</code> — метеорологические данные на текущий момент для заданного города\n"
        "/setweather <code>город</code> <code>время(МСК)</code> — ежедневная рассылка погоды в заданное время для заданного города\n"
        "/delweather — отключение ежедневной рассылки погоды\n\n"
        "<u>🔗 Фильтры в меню управления</u>:\n"
        "Переключайте фильтры ссылок, капса, спама, стикеров, мата и ключевых слов через графический интерфейс.\n"
        "Статус каждого фильтра отображается в меню."
    )
    await message.answer(help_text, parse_mode="HTML")


def register_handlers_help(dp):
    dp.include_router(router)
