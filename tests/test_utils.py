import pytest
import src.utils

def test_filter_and_sorting():
    data = [
        {"state": "EXECUTED", "date": "2023-10-12"},
        {"state": "NOT_EXECUTED", "date": "2023-10-11"},
        {"state": "EXECUTED", "date": "2023-10-10"}
    ]
    result = src.utils.filter_and_sorting(data)
    assert len(result) == 2, "Should have filtered to 2 items"
    assert result[0]['date'] == "2023-10-12", "Should be sorted by date in descending order"

def test_get_date():
    date_str = "2023-10-12T14:30:00Z"
    result = src.utils.get_date(date_str)
    assert result == '12.10.2023', "Should format date correctly"


def test_mask_account_number():
    account_number = '12345678'
    result = src.utils.mask_account_number(account_number)
    assert result == '**5678', "Should mask account number correctly"


def test_mask_prepare_message_number():
    message = 'Счет 12345678'
    result = src.utils.mask_prepare_message_number(message)
    assert result == 'Счет **5678', "Should replace account number correctly"

