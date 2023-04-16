import json
from datetime import datetime


def get_all_operation():
    with open('operation.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_operation_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    return x['date']


def get_operation_by_date(data):
    data = sorted(data, key=sorted_key, reverse=True)
    return data[:5]


def reformat_data(data):
    format_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = row['description']
        amount = row['operationAmount']['amount']
        name = row['operationAmount']['currency']['name']
        if 'from' in row:
            from_arrow = '->'
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            account_number = row['to'].split()
            to_the_account = account_number.pop(-1)
            to_the_account = f"Счет **{to_the_account[-4:]}"
        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""
            account_number = row['to'].split()
            to_the_account = account_number.pop(-1)
            to_the_account = f"**{to_the_account[-4:]}"

        format_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {to_the_account}
{amount} {name}
        """)
    return format_data
