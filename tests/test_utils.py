import pytest
from src.utils import filter_and_sorting, get_date, mask_prepare_message_number, mask_card_number, mask_account_number, prepare_user_message

def test_filter_and_sorting():
    data = [
        {"state": "EXECUTED", "date": "2022-01-01"},
        {"state": "PENDING", "date": "2022-01-02"},
        {"state": "EXECUTED", "date": "2022-01-03"},
        {"state": "EXECUTED", "date": "2022-01-04"},
    ]

    result = filter_and_sorting(data)

    assert len(result) == 3
    assert result[0]["date"] == "2022-01-04"
    assert result[1]["date"] == "2022-01-03"
    assert result[2]["date"] == "2022-01-01"

def test_get_date():
    date = "2022-01-01"

    result = get_date(date)

    assert result == "01.01.2022"

def test_mask_prepare_message_number():
    message_1 = "Счет 1234567890123456"
    message_2 = "Карта 1234567890123456"
    message_3 = None

    result_1 = mask_prepare_message_number(message_1)
    result_2 = mask_prepare_message_number(message_2)
    result_3 = mask_prepare_message_number(message_3)

    assert result_1 == "Счет **** **** **** 3456"
    assert result_2 == "Карта **** **** **** 3456"
    assert result_3 is None

def test_mask_card_number():

    number_1 = "1234567890123456"
    number_2 = "12345678"

    masked_number_1 = mask_card_number(number_1)
    print(masked_number_1)

    masked_number_2 = mask_card_number(number_2)
    print(masked_number_2)


