import os

# Telegram Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN', '8333708065:AAFwXyuHT_FetktrQzxcJwsONQ2aE7U7Iu0')
CHAT_ID = os.getenv('CHAT_ID', '597030382')

# Telegram Channels to Monitor
CHANNELS = {
    'sport_y_doma_kzn': {
        'name': 'Спорт у Дома Казань',
        'category': '🏃 СПОРТ',
        'url': 'https://t.me/sport_y_doma_kzn',
        'keywords': ['спорт', 'тренировка', 'марафон', 'забег', 'соревнование', 'тренинг', 'фитнес']
    },
    'delovorot': {
        'name': 'Деловой Оборот',
        'category': '💼 ДЕЛОВЫЕ СОБЫТИЯ',
        'url': 'https://t.me/delovorot',
        'keywords': ['конференция', 'вебинар', 'лекция', 'обучение', 'семинар', 'финансы', 'маркетплейс']
    }
}

# Timezone
TIMEZONE = 'Europe/Moscow'

# Days for digest
DAYS_FORWARD = 7
