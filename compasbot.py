import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

updater = Updater('6645829381:AAHQtqgIReTSkXVPm6HqYP1DFH8Clggu_Os')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat
    logger.info(f"User {name.username} (ID {name.id}) started the conversation.")

    button = ReplyKeyboardMarkup([['/main']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Для начала работы нажми кнопку внизу'.format(name.first_name),
        reply_markup=button)


def main_page(update, context):
    chat = update.effective_chat
    keyboard = [
        [
            InlineKeyboardButton("Тип сети", callback_data=str(chain_type)),
            InlineKeyboardButton("Ассортимент", callback_data=str(ranges)),
        ],
        [
            InlineKeyboardButton("Периодные активности", callback_data=str(activities)),
            InlineKeyboardButton("Калькулятор AHS", callback_data=str(calculator)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=chat.id,
        text='Выбери необходимый раздел из меню',
        reply_markup=reply_markup)


def chain_type(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Локальная", callback_data=str(local)),
         InlineKeyboardButton("Национальная", callback_data=str(national))],
        [InlineKeyboardButton("Назад", callback_data=str(main))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери тип сети",
        reply_markup=reply_markup
    )


def ranges(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/range.pdf', 'rb'))


def activities(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/activities.pdf', 'rb'))


def calculator(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/calculator.xlsx', 'rb'))


def local(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Мария-Ра", callback_data=str(maria)),
            InlineKeyboardButton("Лама", callback_data=str(lama)),
        ],
        [
            InlineKeyboardButton("Быстроном", callback_data=str(bystronom)),
            InlineKeyboardButton("Аникс", callback_data=str(aniks)),
        ],
        [
            InlineKeyboardButton("Холифуд", callback_data=str(holifood)),
            InlineKeyboardButton("Доброцен", callback_data=str(dobrocen)),
        ],
        [
            InlineKeyboardButton("Красный Яр", callback_data=str(krasniyar)),
            InlineKeyboardButton("Батон", callback_data=str(baton)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(chain_type))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери сеть",
        reply_markup=reply_markup
    )


def national(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Пятёрочка", callback_data=str(x5)),
            InlineKeyboardButton("Магнит", callback_data=str(tander)),
        ],
        [
            InlineKeyboardButton("FixPrice", callback_data=str(fixprice)),
            InlineKeyboardButton("METRO", callback_data=str(metro)),
        ],
        [
            InlineKeyboardButton("Лента", callback_data=str(lenta)),
            InlineKeyboardButton("Окей", callback_data=str(okey)),
        ],
        [
            InlineKeyboardButton("Ашан", callback_data=str(auchan)),
            InlineKeyboardButton("Монетка", callback_data=str(monetka)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(chain_type))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери сеть",
        reply_markup=reply_markup
    )


def maria(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            # InlineKeyboardButton("Бриф", callback_data=str(maria_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(maria_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(maria_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(maria_plano)),
            # InlineKeyboardButton("АП", callback_data=str(maria_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def maria_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/maria-ra/...', 'rb'))


def maria_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/maria-ra/...', 'rb'))


def maria_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/maria-ra/...', 'rb'))


def maria_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/maria-ra/...', 'rb'))


def maria_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/maria-ra/...', 'rb'))


def lama(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(lama_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(lama_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(lama_range)),
        ],
        [
            InlineKeyboardButton("Планограмма", callback_data=str(lama_plano)),
            # InlineKeyboardButton("АП", callback_data=str(lama_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def lama_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lama/lama_brief.jpeg', 'rb'))


def lama_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lama/lama_work.pptx', 'rb'))


def lama_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lama/lama_range.pdf', 'rb'))


def lama_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lama/lama_plano_KSO.JPG', 'rb'))
    updater.bot.send_document(chat_id=chat.id, document=open('data/lama/lama_plano_MS.JPG', 'rb'))


def lama_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lama/lama_ap.pdf', 'rb'))


def bystronom(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(bystronom_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(bystronom_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(bystronom_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(bystronom_plano)),
            # InlineKeyboardButton("АП", callback_data=str(bystronom_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def bystronom_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/bystronom/bystronom_brief.pdf', 'rb'))


def bystronom_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/bystronom/bystronom_work.pptx', 'rb'))


def bystronom_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/bystronom/...', 'rb'))


def bystronom_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/bystronom/...', 'rb'))


def bystronom_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/bystronom/...', 'rb'))


def aniks(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            # InlineKeyboardButton("Бриф", callback_data=str(aniks_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(aniks_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(aniks_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(aniks_plano)),
            # InlineKeyboardButton("АП", callback_data=str(aniks_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def aniks_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/aniks/...', 'rb'))


def aniks_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/aniks/...', 'rb'))


def aniks_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/aniks/...', 'rb'))


def aniks_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/aniks/...', 'rb'))


def aniks_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/aniks/...', 'rb'))


def holifood(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            # InlineKeyboardButton("Бриф", callback_data=str(holifood_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(holifood_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(holifood_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(holifood_plano)),
            # InlineKeyboardButton("АП", callback_data=str(holifood_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def holifood_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/holifood/...', 'rb'))


def holifood_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/holifood/...', 'rb'))


def holifood_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/holifood/...', 'rb'))


def holifood_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/holifood/...', 'rb'))


def holifood_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/holifood/...', 'rb'))


def dobrocen(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            # InlineKeyboardButton("Бриф", callback_data=str(dobrocen_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(dobrocen_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(dobrocen_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(dobrocen_plano)),
            # InlineKeyboardButton("АП", callback_data=str(dobrocen_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def dobrocen_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/dobrocen/...', 'rb'))


def dobrocen_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/dobrocen/...', 'rb'))


def dobrocen_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/dobrocen/...', 'rb'))


def dobrocen_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/dobrocen/...', 'rb'))


def dobrocen_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/dobrocen/...', 'rb'))


def krasniyar(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            # InlineKeyboardButton("Бриф", callback_data=str(krasniyar_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(krasniyar_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(krasniyar_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(krasniyar_plano)),
            # InlineKeyboardButton("АП", callback_data=str(krasniyar_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def krasniyar_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/krasniyar/...', 'rb'))


def krasniyar_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/krasniyar/...', 'rb'))


def krasniyar_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/krasniyar/...', 'rb'))


def krasniyar_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/krasniyar/...', 'rb'))


def krasniyar_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/krasniyar/...', 'rb'))


def baton(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            # InlineKeyboardButton("Бриф", callback_data=str(baton_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(baton_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(baton_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(baton_plano)),
            # InlineKeyboardButton("АП", callback_data=str(baton_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(local))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def baton_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/baton/...', 'rb'))


def baton_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/baton/...', 'rb'))


def baton_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/baton/...', 'rb'))


def baton_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/baton/...', 'rb'))


def baton_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/baton/...', 'rb'))


def x5(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(x5_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(x5_work)),
            InlineKeyboardButton("Ассортимент", callback_data=str(x5_range)),
        ],
        [
            InlineKeyboardButton("Планограмма", callback_data=str(x5_plano)),
            InlineKeyboardButton("АП", callback_data=str(x5_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def x5_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/x5_brief.pdf', 'rb'))


def x5_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/x5_work.pptx', 'rb'))


def x5_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/x5_range.xlsx', 'rb'))


def x5_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/x5_plano_CO_WISH.JPG', 'rb'))
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/x5_plano_KSO_MUST.JPG', 'rb'))
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/x5_display_WISH.JPG', 'rb'))


def x5_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/Х5_АП_SNICKERS Навеска сент-окт.xlsx', 'rb'))
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/Х5_АП_Орбит_навеска_препак_сент_окт.xlsx', 'rb'))
    updater.bot.send_document(chat_id=chat.id, document=open('data/x5/Х5_АП_Фигуры_рамки_август', 'rb'))


def tander(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(tander_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(tander_work)),
            InlineKeyboardButton("Доверенности", callback_data=str(tander_range)),
        ],
        [
        #     InlineKeyboardButton("Планограмма", callback_data=str(tander_plano)),
        #     InlineKeyboardButton("АП", callback_data=str(tander_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def tander_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/tander/tander_brief.pdf', 'rb'))


def tander_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/tander/tander_work.pptx', 'rb'))


def tander_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/tander/Доверенность_Orbit Гранат_102.07.23.pdf', 'rb'))
    updater.bot.send_document(chat_id=chat.id, document=open('data/tander/Доверенность_Прокачайся_в_экологии.pdf', 'rb'))


def tander_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/tander/...', 'rb'))


def tander_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/tander/...', 'rb'))


def fixprice(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(fixprice_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(fixprice_work)),
            InlineKeyboardButton("Ассортимент", callback_data=str(fixprice_range)),
        ],
        [
            InlineKeyboardButton("Планограмма", callback_data=str(fixprice_plano)),
            # InlineKeyboardButton("АП", callback_data=str(fixprice_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def fixprice_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/fixprice/fixprice_brief.pdf', 'rb'))


def fixprice_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/fixprice/fixprice_work.pptx', 'rb'))


def fixprice_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/fixprice/fixprice_range.xlsx', 'rb'))


def fixprice_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/fixprice/fixprice_plano.jpeg', 'rb'))


def fixprice_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/fixprice/...', 'rb'))



def metro(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(metro_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(metro_work)),
            InlineKeyboardButton("Ассортимент", callback_data=str(metro_range)),
        ],
        [
            InlineKeyboardButton("Планограмма", callback_data=str(metro_plano)),
            # InlineKeyboardButton("АП", callback_data=str(metro_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def metro_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/metro/metro_brief.pdf', 'rb'))


def metro_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/metro/metro_work.pptx', 'rb'))


def metro_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/metro/metro_range.xlsx', 'rb'))


def metro_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/metro/metro_plano.pptx', 'rb'))


def metro_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/metro/...', 'rb'))


def lenta(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(lenta_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(lenta_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(lenta_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(lenta_plano)),
            # InlineKeyboardButton("АП", callback_data=str(lenta_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def lenta_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lenta/lenta_brief.pdf', 'rb'))


def lenta_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lenta/lenta_work.pptx', 'rb'))


def lenta_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lenta/...', 'rb'))


def lenta_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lenta/...', 'rb'))


def lenta_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/lenta/...', 'rb'))


def okey(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(okey_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(okey_work)),
            InlineKeyboardButton("Ассортимент", callback_data=str(okey_range)),
        ],
        [
            InlineKeyboardButton("Разрешение навеска", callback_data=str(okey_plano)),
            InlineKeyboardButton("АП", callback_data=str(okey_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def okey_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/okey/okey_brief.pptx', 'rb'))


def okey_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/okey/okey_work.pptx', 'rb'))


def okey_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/okey/okey_range.xlsb', 'rb'))


def okey_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/okey/Окей_Разрешение_на_размещение_навески.jpeg', 'rb'))


def okey_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/okey/okey_АП_Сникерс.xlsx', 'rb'))


def auchan(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(auchan_brief))
        ],
        [
            InlineKeyboardButton("Особенности работы", callback_data=str(auchan_work)),
            InlineKeyboardButton("Ассортимент", callback_data=str(auchan_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(auchan_plano)),
            # InlineKeyboardButton("АП", callback_data=str(auchan_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def auchan_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/auchan/auchan_brief.pdf', 'rb'))


def auchan_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/auchan/auchan_work.pptx', 'rb'))


def auchan_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/auchan/auchan_range.xlsx', 'rb'))


def auchan_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/auchan/...', 'rb'))


def auchan_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/auchan/...', 'rb'))


def monetka(update, context):
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [
            InlineKeyboardButton("Бриф", callback_data=str(monetka_brief))
        ],
        [
            # InlineKeyboardButton("Особенности работы", callback_data=str(monetka_work)),
            # InlineKeyboardButton("Ассортимент", callback_data=str(monetka_range)),
        ],
        [
            # InlineKeyboardButton("Планограмма", callback_data=str(monetka_plano)),
            # InlineKeyboardButton("АП", callback_data=str(monetka_ap)),
        ],
        [InlineKeyboardButton("Назад", callback_data=str(national))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Выбери необходимый файл",
        reply_markup=reply_markup
    )


def monetka_brief(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/monetka/monetka_brief.pdf', 'rb'))


def monetka_work(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/monetka/...', 'rb'))


def monetka_range(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/monetka/...', 'rb'))


def monetka_plano(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/monetka/...', 'rb'))


def monetka_ap(update, context):
    chat = update.effective_chat
    updater.bot.send_document(chat_id=chat.id, document=open('data/monetka/...', 'rb'))


def main():

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('main', main_page))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_page, pattern='^' + str(main) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(chain_type, pattern='^' + str(chain_type) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(ranges, pattern='^' + str(ranges) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(activities, pattern='^' + str(activities) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(calculator, pattern='^' + str(calculator) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(local, pattern='^' + str(local) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(national, pattern='^' + str(national) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(maria, pattern='^' + str(maria) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(maria_brief, pattern='^' + str(maria_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(maria_work, pattern='^' + str(maria_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(maria_range, pattern='^' + str(maria_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(maria_plano, pattern='^' + str(maria_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(maria_ap, pattern='^' + str(maria_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(lama, pattern='^' + str(lama) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lama_brief, pattern='^' + str(lama_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lama_work, pattern='^' + str(lama_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lama_range, pattern='^' + str(lama_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lama_plano, pattern='^' + str(lama_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lama_ap, pattern='^' + str(lama_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(bystronom, pattern='^' + str(bystronom) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(bystronom_brief, pattern='^' + str(bystronom_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(bystronom_work, pattern='^' + str(bystronom_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(bystronom_range, pattern='^' + str(bystronom_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(bystronom_plano, pattern='^' + str(bystronom_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(bystronom_ap, pattern='^' + str(bystronom_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(aniks, pattern='^' + str(aniks) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(aniks_brief, pattern='^' + str(aniks_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(aniks_work, pattern='^' + str(aniks_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(aniks_range, pattern='^' + str(aniks_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(aniks_plano, pattern='^' + str(aniks_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(aniks_ap, pattern='^' + str(aniks_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(holifood, pattern='^' + str(holifood) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(holifood_brief, pattern='^' + str(holifood_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(holifood_work, pattern='^' + str(holifood_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(holifood_range, pattern='^' + str(holifood_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(holifood_plano, pattern='^' + str(holifood_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(holifood_ap, pattern='^' + str(holifood_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(dobrocen, pattern='^' + str(dobrocen) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(dobrocen_brief, pattern='^' + str(dobrocen_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(dobrocen_work, pattern='^' + str(dobrocen_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(dobrocen_range, pattern='^' + str(dobrocen_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(dobrocen_plano, pattern='^' + str(dobrocen_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(dobrocen_ap, pattern='^' + str(dobrocen_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(krasniyar, pattern='^' + str(krasniyar) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(krasniyar_brief, pattern='^' + str(krasniyar_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(krasniyar_work, pattern='^' + str(krasniyar_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(krasniyar_range, pattern='^' + str(krasniyar_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(krasniyar_plano, pattern='^' + str(krasniyar_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(krasniyar_ap, pattern='^' + str(krasniyar_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(baton, pattern='^' + str(baton) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(baton_brief, pattern='^' + str(baton_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(baton_work, pattern='^' + str(baton_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(baton_range, pattern='^' + str(baton_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(baton_plano, pattern='^' + str(baton_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(baton_ap, pattern='^' + str(baton_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(tander, pattern='^' + str(tander) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tander_brief, pattern='^' + str(tander_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tander_work, pattern='^' + str(tander_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tander_range, pattern='^' + str(tander_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tander_plano, pattern='^' + str(tander_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(tander_ap, pattern='^' + str(tander_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(fixprice, pattern='^' + str(fixprice) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fixprice_brief, pattern='^' + str(fixprice_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fixprice_work, pattern='^' + str(fixprice_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fixprice_range, pattern='^' + str(fixprice_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fixprice_plano, pattern='^' + str(fixprice_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(fixprice_ap, pattern='^' + str(fixprice_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(metro, pattern='^' + str(metro) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(metro_brief, pattern='^' + str(metro_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(metro_work, pattern='^' + str(metro_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(metro_range, pattern='^' + str(metro_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(metro_plano, pattern='^' + str(metro_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(metro_ap, pattern='^' + str(metro_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(lenta, pattern='^' + str(lenta) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lenta_brief, pattern='^' + str(lenta_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lenta_work, pattern='^' + str(lenta_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lenta_range, pattern='^' + str(lenta_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lenta_plano, pattern='^' + str(lenta_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(lenta_ap, pattern='^' + str(lenta_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(okey, pattern='^' + str(okey) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(okey_brief, pattern='^' + str(okey_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(okey_work, pattern='^' + str(okey_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(okey_range, pattern='^' + str(okey_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(okey_plano, pattern='^' + str(okey_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(okey_ap, pattern='^' + str(okey_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(auchan, pattern='^' + str(auchan) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(auchan_brief, pattern='^' + str(auchan_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(auchan_work, pattern='^' + str(auchan_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(auchan_range, pattern='^' + str(auchan_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(auchan_plano, pattern='^' + str(auchan_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(auchan_ap, pattern='^' + str(auchan_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(monetka, pattern='^' + str(monetka) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monetka_brief, pattern='^' + str(monetka_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monetka_work, pattern='^' + str(monetka_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monetka_range, pattern='^' + str(monetka_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monetka_plano, pattern='^' + str(monetka_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(monetka_ap, pattern='^' + str(monetka_ap) + '$'))

    updater.dispatcher.add_handler(CallbackQueryHandler(x5, pattern='^' + str(x5) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(x5_brief, pattern='^' + str(x5_brief) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(x5_work, pattern='^' + str(x5_work) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(x5_range, pattern='^' + str(x5_range) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(x5_plano, pattern='^' + str(x5_plano) + '$'))
    updater.dispatcher.add_handler(CallbackQueryHandler(x5_ap, pattern='^' + str(x5_ap) + '$'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
