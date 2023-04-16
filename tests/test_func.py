from utils.func import get_operation_data, get_operation_by_date, reformat_data, get_all_operation


def test_get_operation_data(test_func):
    successful_operation = get_operation_data(test_func)
    assert [x['state'] for x in successful_operation] == ['EXECUTED', 'EXECUTED']


def test_get_operation_by_date(test_func):
    date_of_operation = get_operation_by_date(test_func)
    assert [x['date'] for x in date_of_operation] == ["2019-01-15T17:58:27.064377", "2018-11-23T23:52:36.999661",
                                                      "2018-01-21T01:10:28.317704"]


def test_reformat_data(test_func):
    format_data = reformat_data(test_func)
    assert [format_data[2]] == ['\n'
                                '15.01.2019 Перевод организации\n'
                                'Visa Platinum 2241 65** **** 8487 -> Счет **8486\n'
                                '90688.44 USD\n'
                                '        ']
