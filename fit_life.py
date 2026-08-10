# Проект FitLife - MVP версия 1.0


# 1. Приветствие
print("Добро пожаловать в приложение FitLife!")

# 2. Сбор данных
user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))

user_weight = float(input("Введите ваш вес в кг: "))
user_height = float(input("Введите ваш рост в метрах (например, 1.75): "))


# 3. Расчеты
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_l = water_ml / 1000

# 4. Вывод красивого результата
print("_" * 30)
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
