from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.city import City

cities = [
    {"name": "Київ",               "latitude": 50.4501,   "longitude": 30.5234},

    {"name": "Харків",              "latitude": 49.9935,   "longitude": 36.2304},
    {"name": "Одеса",              "latitude": 46.4825,   "longitude": 30.7233},
    {"name": "Дніпро",             "latitude": 48.4647,   "longitude": 35.0462},
    {"name": "Запоріжжя",          "latitude": 47.8388,   "longitude": 35.1396},
    {"name": "Львів",              "latitude": 49.8397,   "longitude": 24.0297},
    {"name": "Кривий Ріг",         "latitude": 47.9105,   "longitude": 33.3918},
    {"name": "Миколаїв",           "latitude": 46.9750,   "longitude": 31.9946},
    {"name": "Вінниця",            "latitude": 49.2328,   "longitude": 28.4800},
    {"name": "Херсон",             "latitude": 46.6550,   "longitude": 32.6178},
    {"name": "Полтава",            "latitude": 49.5883,   "longitude": 34.5514},
    {"name": "Чернігів",           "latitude": 51.4948,   "longitude": 31.2893},
    {"name": "Черкаси",            "latitude": 49.4444,   "longitude": 32.0598},
    {"name": "Суми",               "latitude": 50.9077,   "longitude": 34.7981},
    {"name": "Житомир",            "latitude": 50.2547,   "longitude": 28.6587},
    {"name": "Рівне",              "latitude": 50.6199,   "longitude": 26.2516},
    {"name": "Івано-Франківськ",   "latitude": 48.9226,   "longitude": 24.7104},
    {"name": "Чернівці",           "latitude": 48.2915,   "longitude": 25.9403},
    {"name": "Ужгород",            "latitude": 48.6208,   "longitude": 22.2879},
    {"name": "Тернопіль",          "latitude": 49.5535,   "longitude": 25.5948},
    {"name": "Луцьк",              "latitude": 50.7472,   "longitude": 25.3254},
    {"name": "Кропивницький",     "latitude": 48.5108,   "longitude": 32.2593},

    # Frontline-adjacent towns
    {"name": "Бахмут",             "latitude": 48.59472, "longitude": 38.00083},
    {"name": "Авдіївка",          "latitude": 48.14528, "longitude": 37.74500},
    {"name": "Мар’їнка",           "latitude": 47.94194, "longitude": 37.50361},
    {"name": "Соледар",            "latitude": 48.67935, "longitude": 38.08902},
    {"name": "Вугледар",           "latitude": 47.78300, "longitude": 37.25000},
    {"name": "Часів Яр",           "latitude": 48.58844, "longitude": 37.83588},
    {"name": "Покровськ",         "latitude": 48.19472, "longitude": 37.04861},
    {"name": "Донецьк",            "latitude": 48.01587, "longitude": 37.80285},
    {"name": "Маріуполь",         "latitude": 47.09710, "longitude": 37.54340},
    {"name": "Волноваха",         "latitude": 47.53500, "longitude": 37.47420},
    {"name": "Краматорськ",       "latitude": 48.72310, "longitude": 37.53280},
    {"name": "Слов’янськ",        "latitude": 48.86670, "longitude": 37.61670},
    {"name": "Сєвєродонецьк",      "latitude": 48.94930, "longitude": 38.49140},
    {"name": "Лисичанськ",        "latitude": 48.91550, "longitude": 38.40040},
    {"name": "Попасна",            "latitude": 48.63000, "longitude": 38.21700},
    {"name": "Дебальцеве",         "latitude": 48.33330, "longitude": 38.43330},
    {"name": "Горлівка",           "latitude": 48.30390, "longitude": 38.05450},
    {"name": "Первомайськ",        "latitude": 48.55750, "longitude": 39.33500},
    {"name": "Лиман",              "latitude": 48.93440, "longitude": 37.94750},
    {"name": "Світлодарськ",       "latitude": 49.11670, "longitude": 38.18330},
    {"name": "Рубіжне",            "latitude": 49.00310, "longitude": 38.38690},
    {"name": "Кремінна",           "latitude": 49.08530, "longitude": 38.80330},
    {"name": "Ізюм",               "latitude": 49.21390, "longitude": 37.25720},
    {"name": "Куп’янськ",          "latitude": 49.71080, "longitude": 37.61370},
    {"name": "Золоте",             "latitude": 48.73330, "longitude": 38.33330},
    {"name": "Щастя",              "latitude": 48.67110, "longitude": 39.33690},
    {"name": "Новоайдар",          "latitude": 48.84,     "longitude": 39.14},

    # Kharkiv Oblast towns
    {"name": "Балаклія",         "latitude": 49.7225,   "longitude": 37.2683},
    {"name": "Вовчанськ",        "latitude": 50.3658,   "longitude": 36.5122},
    {"name": "Чугуїв",           "latitude": 49.4017,   "longitude": 36.6908},
    {"name": "Богодухів",        "latitude": 50.1556,   "longitude": 36.4806},
    {"name": "Лозова",           "latitude": 48.8768,   "longitude": 37.8733},

    # Zaporizhzhia Oblast towns
    {"name": "Мелітополь",       "latitude": 46.8487,   "longitude": 35.3631},
    {"name": "Бердянськ",        "latitude": 46.8381,   "longitude": 36.7928},
    {"name": "Енергодар",        "latitude": 47.5015,   "longitude": 34.6608},
    {"name": "Токмак",           "latitude": 47.2178,   "longitude": 35.6028},
    {"name": "Василівка",        "latitude": 47.4454,   "longitude": 34.8450},

    # Mykolaiv Oblast towns
    {"name": "Вознесенськ",      "latitude": 47.6883,   "longitude": 31.3339},
    {"name": "Южноукраїнськ",    "latitude": 48.2806,   "longitude": 31.5317},
    {"name": "Очаків",           "latitude": 46.6106,   "longitude": 31.4887},
    {"name": "Баштанка",         "latitude": 47.4114,   "longitude": 31.5106},

    # Odesa Oblast towns
    {"name": "Білгород-Дністровський", "latitude": 46.1996,   "longitude": 30.3554},
    {"name": "Ізмаїл",             "latitude": 45.3488,   "longitude": 28.8440},
    {"name": "Чорноморськ",        "latitude": 46.3392,   "longitude": 30.6451},
    {"name": "Южне",               "latitude": 46.4036,   "longitude": 30.6872},
    {"name": "Подільськ",           "latitude": 47.4685,   "longitude": 29.2834},
]

async def seed_cities(session: AsyncSession) -> None:
    existing = set(await session.scalars(select(City.name)))
    for c in cities:
        if c["name"] not in existing:
            session.add(City(
                name=c["name"],
                latitude=c["latitude"],
                longitude=c["longitude"]
            ))
    await session.commit()
