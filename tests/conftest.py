import pytest


@pytest.fixture
def test_func():
    return [{
        "id": 634356296,
        "state": "EXECUTED",
        "date": "2018-01-21T01:10:28.317704",
        "operationAmount": {
            "amount": "96900.90",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 33407225454123927865",
        "to": "Счет 79619011266276091215"
    },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
        },
        {
            "id": 970724427,
            "state": "CANCELED",
            "date": "2019-01-15T17:58:27.064377",
            "operationAmount": {
                "amount": "90688.44",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2241653116508487",
            "to": "Счет 26494285169417058486"
        },
    ]
