import datetime
import json
from .utils import mask_card, mask_account

def display_operations():
    with open('data/operations.json') as file:
        operations = json.load(file)

    operations = [op for op in operations if op['state'] == 'EXECUTED']

    for operation in operations[-5:][::-1]:
        transfer_date = datetime.datetime.strptime(operation['date'], "%d/%m/%Y %H:%M:%S")
        description = operation['description']
        from_acct = mask_card(operation['from']) if operation['from'].count(' ') == 2 else mask_account(operation['from'])
        to_acct = mask_account(operation['to'])
        amount = operation['operationAmount']

        print(f'{transfer_date}\n{description}\n{from_acct} -> {to_acct}\n{amount}\n')

if __name__ == "__main__":
    display_operations()
