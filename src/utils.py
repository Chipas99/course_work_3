import json
import os.path

def filter_and_sorting(data: list):
    items = [item for item in data if item.get('state') == "EXECUTED"]

    items.sort(key=lambda x: x.get('date'), reverse=True)

    return items


def get_date(date: str):
    date_num = date[0:10].split('-')
    return date_num[2] + '.' + date_num[1] + '.' + date_num[0]

def mask_prepare_message_number(message):
    if message is None:
        return None

    words = message.split()
    masked_words = []

    for word in words:
        if word.isdigit() and len(word) == 16:
            masked_word = mask_card_number(word)
            masked_words.append(masked_word)
        else:
            masked_words.append(word)

    return ' '.join(masked_words)



def mask_card_number(number):
    if number.isdigit() and len(number) == 16:
        return "**** **** **** " + number[-4:]
    else:
        return number


def mask_account_number(number: str):
    if number.isdigit() and len(number) >= 4:
        return "**"+number[-4:]
    else:
        raise ValueError('Неправильный номер счета')



def prepare_user_message(item: dict):
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = mask_prepare_message_number(item.get('from'))
    to_ = mask_prepare_message_number(item.get('to'))
    amount = item.get('operationAmount', {}).get('amount')
    curr = item.get('operationAmount').get('currency').get('name')

    return f'{date} {desc}\n{from_} -> {to_}\n{amount} {curr}\n'
