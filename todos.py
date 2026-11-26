import json

with open("todos.json", encoding="utf-8") as file:
    response = json.load(file)
todos = response["todos"]


# print(todos)
# print(todos[0]["todo"])


def get_unfinished_titles(todos):
    unfinished = []
    for task in todos:
        if task["completed"] == False:
            unfinished.append(task["todo"])
    return unfinished


assert get_unfinished_titles(todos) == ['Do something nice for someone you care about', 'Watch a documentary',
                                        'Invest in cryptocurrency',
                                        'Contribute code or a monetary donation to an open-source software project',
                                        'Go see a Broadway production']
assert get_unfinished_titles([]) == []
assert get_unfinished_titles([
    {"id": 1, "todo": "Купить продукты", "completed": False},
    {"id": 2, "todo": "Оплатить интернет", "completed": True},
    {"id": 3, "todo": "Забрать посылку", "completed": False},
]
) == ["Купить продукты", "Забрать посылку"]

assert get_unfinished_titles([
    {"id": 1, "todo": "Купить продукты", "completed": True},
    {"id": 2, "todo": "Оплатить интернет", "completed": True},
    {"id": 3, "todo": "Забрать посылку", "completed": True},
]
) == []


def count_completed(todos):
    total_completed = 0
    for task in todos:
        completed_task = task["completed"]
        if completed_task == True:
            total_completed = total_completed + 1
    return total_completed


assert count_completed(todos) == 5
assert count_completed([]) == 0
assert count_completed([
    {"id": 1, "todo": "Купить продукты", "completed": False},
    {"id": 2, "todo": "Оплатить интернет", "completed": False},
    {"id": 3, "todo": "Забрать посылку", "completed": False},
]) == 0
