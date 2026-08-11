# Проект FitLife - MVP версия 1.0

WATER_ML_PER_KG = 30
ML_IN_LITER = 1000

# 1. Приветствие
print("Добро пожаловать в приложение FitLife!")

# 2. Сбор данных
user_name = input("Введите ваше имя: ")

while True:
    try:
        user_age = int(input("Введите ваш возраст: "))
        if user_age <= 0:
            print("Возраст должен быть больше нуля.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите корректный возраст (число).")

while True:
    try:
        user_weight = float(input("Введите ваш вес в кг: "))
        if user_weight <= 0:
            print("Вес должен быть больше нуля.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите корректный вес (число).")

while True:
    try:
        user_height = float(input("Ваш рост в метрах (например, 1.75): "))
        if user_height <= 0:
            print("Рост должен быть больше нуля.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите корректный рост (число).")

# 3. Расчеты
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_ML_PER_KG
water_l = water_ml / ML_IN_LITER

# 4. Вывод красивого результата
print(
    "_" * 30,
    "",
    f"Отчет для пользователя: {user_name} ({user_age} г.)",
    f"Твой индекс массы тела: {bmi}",
    f"Рекомендуемая норма воды: {water_l:.1f} л. в день",
    "",
    "Расчет окончен. Будьте здоровы!",
    "",
    sep="\n"
)
