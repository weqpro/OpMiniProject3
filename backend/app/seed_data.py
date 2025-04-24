from collections import namedtuple

Category = namedtuple("Category", ["id", "name"])

CATEGORIES = [
    Category(1, "Автозапчастини"),
    Category(2, "Енергозабезпечення"),
    Category(3, "Генератори"),
    Category(4, "Гігієна та санітарія"),
    Category(5, "Інструменти / будматеріали"),
    Category(6, "Медицина"),
    Category(7, "Навігація"),
    Category(8, "Одяг"),
    Category(9, "Побутові послуги"),
    Category(10, "Польовий побут"),
    Category(11, "Продукти харчування"),
    Category(12, "Ремонт"),
    Category(13, "Розвідка і спостереження"),
    Category(14, "Спорядження"),
    Category(15, "Техніка"),
    Category(16, "Транспорт"),
    Category(17, "Звʼязок"),
]
