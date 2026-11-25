from operator import length_hint

orders = [
    {"id": 1, "status": "PAID", "amount": 1500},
    {"id": 2, "status": "NEW", "amount": 700},
    {"id": 3, "status": "PAID", "amount": 2500},
    {"id": 4, "status": "CANCELLED", "amount": 900},
]


def calculate_paid_total(orders):
    total = 0
    for order in orders:
        if order["status"] == "PAID":
            total = total + order["amount"]
    return total


assert calculate_paid_total(orders) == 4000
assert calculate_paid_total([]) == 0
assert calculate_paid_total([
    {"id": 10, "status": "NEW", "amount": 500}
]) == 0
assert calculate_paid_total([
    {"id": 11, "status": "PAID", "amount": 300}
]) == 300

assert calculate_paid_total([
    {"id": 4, "status": "CANCELLED", "amount": 100}
]) == 0
assert calculate_paid_total([
    {"id": 15, "status": "PAID", "amount": 100.5}
]) == 100.5


def filter_orders_by_status(orders, status):
    order_list = []
    for order in orders:
        if status == order["status"]:
            order_list.append(order)
    return order_list


assert filter_orders_by_status(orders, "PAID") == [
    {"id": 1, "status": "PAID", "amount": 1500},
    {"id": 3, "status": "PAID", "amount": 2500},
]
assert filter_orders_by_status(orders, "REFUNDED") == []
assert filter_orders_by_status([], "PAID") == []
assert filter_orders_by_status(orders, "NEW") == [
    {"id": 2, "status": "NEW", "amount": 700},
]
assert filter_orders_by_status(orders, []) == []


def count_orders_by_status(orders):
    count_orders = {}
    for order in orders:
        status_count = order["status"]
        if status_count not in count_orders:
            count_orders[status_count] = 1
        elif status_count in count_orders:
            count_orders[status_count] = count_orders[status_count] + 1

    return count_orders


assert count_orders_by_status(orders) == {
    "PAID": 2,
    "NEW": 1,
    "CANCELLED": 1,
}
assert count_orders_by_status([]) == {}
assert count_orders_by_status([
    {"id": 2, "status": "NEW", "amount": 700}]
) == {
           "NEW": 1,
       }

assert count_orders_by_status([
    {"id": 1, "status": "PAID", "amount": 700},
    {"id": 3, "status": "PAID", "amount": 700},
    {"id": 8, "status": "PAID", "amount": 700},
    {"id": 12, "status": "PAID", "amount": 700},
]
) == {
           "PAID": 4,
       }


def build_orders_report(orders):
    report = {
        "total_orders": len(orders),
        "paid_total": calculate_paid_total(orders),
        "orders_by_status": count_orders_by_status(orders)
    }
    return report

assert build_orders_report(orders) == {
    "total_orders": 4,
    "paid_total": 4000,
    "orders_by_status": {
        "PAID": 2,
        "NEW": 1,
        "CANCELLED": 1,
    },
}


# print(orders[0]["amount"])
#
#
# assert orders[2]["amount"] == 2500
# assert orders[3]["status"] == "CANCELLED"
#
# orders[0]["status"] = "NEW"
# print(orders[0])
#
# keys = orders[0].keys()
# print(list(keys))
#
# for order in orders:
#     keys = list(order.keys())
#     print(keys)
#
# for order in orders:
#     values = list(order.values())
#     print(values)
#
# first_order = list(orders[0].items())
# print(first_order)
#
