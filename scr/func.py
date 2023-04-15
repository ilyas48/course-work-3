import json


def load_operation():
    with open('operation.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all_operation():
    return load_operation()


def get_operation_by_date(date):
    for operation_date in load_operation():
        if operation_date['date'] == date:
            return operation_date
