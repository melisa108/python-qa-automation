# -*- coding: utf-8 -*-
"""Примеры из «Python Core · Практика 02».

Это не решения задач: нужно самостоятельно написать функции
validate_registration(), get_unfinished_titles() и count_completed().
Проверки для них оставлены комментариями, чтобы файл запускался
до выполнения заданий. Все фрагменты PDF, включая JSON, также
собраны в соседнем .txt-файле для удобного копирования.
"""

# --------------------------------------------------------------------
# Страницы 1–2. Форма регистрации
# --------------------------------------------------------------------

form = {
    "name": "Liza",
    "email": "",
    "agreed": True,
}


def validate_registration(form):
    errors = []
    if form["name"] == "":
        errors.append("name_required")
    if form["email"] == "":
        errors.append("email_required")
    if form["agreed"] == False:
        errors.append("consent_required")
    return errors


assert validate_registration(form) == ["email_required"]
assert validate_registration({
    "name": "Лиза", "email": "liza@example.com", "agreed": True
}) == []
assert validate_registration({
    "name": "", "email": "", "agreed": False
}) == ["name_required", "email_required", "consent_required"]
assert validate_registration({
    "name": "",  "email": "liza@example.com", "agreed": True
}) == ["name_required"]

# Для заданной формы ожидаем: ["email_required"]
# errors = []  # Начинаем с пустого списка найденных ошибок.

# Напиши функцию validate_registration(form), затем раскомментируй проверки:
# assert validate_registration(form) == ["email_required"]
# assert validate_registration({
#     "name": "Лиза", "email": "liza@example.com", "agreed": True
# }) == []
# assert validate_registration({
#     "name": "", "email": "", "agreed": False
# }) == ["name_required", "email_required", "consent_required"]
# Допиши свой assert для случая, когда не заполнено только имя.


# --------------------------------------------------------------------
# Страница 3. Список дел: учимся читать данные
# --------------------------------------------------------------------

todos = [
    {"todo": "Купить продукты", "completed": False},
    {"todo": "Оплатить интернет", "completed": True},
    {"todo": "Забрать посылку", "completed": False}
]

first_task = todos[0]  # Первый словарь из списка.

# Обращаемся к задачам по номерам (индексы начинаются с 0):
# todos[0]
# todos[1]
# todos[2]

# Обращаемся к двум полям выбранной задачи:
# first_task["todo"]
# first_task["completed"]

# Выведет: Купить продукты
print(first_task["todo"])

# Выведет все названия, включая уже выполненные дела:
for task in todos:
    print(task["todo"])

# --------------------------------------------------------------------
# Страница 4. Как устроен ответ API
# --------------------------------------------------------------------

# Учебный JSON из PDF (это именно JSON, не Python-словарь):
# {
#   "todos": [
#     {"id": 1, "todo": "Купить продукты", "completed": false},
#     {"id": 2, "todo": "Оплатить интернет", "completed": true}
#   ],
#   "total": 2
# }
# JSON: false/true. Python: False/True.

# Чтение файла и присваивание переменных показано ниже (страница 5).
# Когда response уже содержит словарь из JSON, можно писать:
# todos = response["todos"]
# first_task = todos[0]
# title = first_task["todo"]
# Или одной строкой:
# response["todos"][0]["todo"]


# --------------------------------------------------------------------
# Страница 5. Невыполненные дела из JSON
# --------------------------------------------------------------------

# Открой в браузере https://dummyjson.com/todos?limit=10
# Скопируй ответ в todos.json рядом с этим Python-файлом.
# Затем раскомментируй код ниже:
# import json
#
# with open("todos.json", encoding="utf-8") as file:
#     response = json.load(file)
#
# todos = response["todos"]
# first_task = todos[0]
# title = first_task["todo"]
# print(title)

sample = [
    {"id": 1, "todo": "Купить продукты", "completed": False},
    {"id": 2, "todo": "Оплатить интернет", "completed": True},
    {"id": 3, "todo": "Забрать посылку", "completed": False},
]

# Напиши функцию get_unfinished_titles(todos), затем раскомментируй:
# assert get_unfinished_titles(sample) == [
#     "Купить продукты", "Забрать посылку"
# ]
# assert get_unfinished_titles([]) == []
# Допиши свой assert, когда все дела выполнены.
# Если прочитала файл todos.json, можешь вывести результат:
# print(get_unfinished_titles(todos))


# --------------------------------------------------------------------
# Страница 6. Закрепляем (дополнительная задача)
# --------------------------------------------------------------------

# Напиши функцию count_completed(todos), затем раскомментируй:
# assert count_completed(sample) == 1
# assert count_completed([]) == 0

# Начинаем с нуля выполненных задач:
count = 0
