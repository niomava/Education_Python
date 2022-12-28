import pytest
import fake_useragent
from requests import request
from datetime import datetime
import json


# constants
SPACE = " "
CLIENT_ID = "credit_card_service_client"
CLIENT_SECRET = "******"
fua = fake_useragent.UserAgent()
Base_URL = "http://65.108.***.***/"

"""Авторизация"""
url = "https://sso.paymatrix.ru/realms/master/protocol/openid-connect/token"
data = {"grant_type": "client_credentials"}
response_auth = request("POST", url, auth=(CLIENT_ID, CLIENT_SECRET), data=data, verify=False)
access_token = response_auth.json()["access_token"]
token_type = response_auth.json()["token_type"]
authorization = token_type + SPACE + access_token


def test_authorize_values_count():
    assert len(data) == 1, "В объекте 1 значение"

def test_authorize_status_code():
    assert response_auth.status_code == 200, "Код выполнения запроса 200"


"""Создание карты"""

EVENT_ID = "api/CreditCard"
now = datetime.now().isoformat()
url = f"{Base_URL}{EVENT_ID}"
headers = {"Authorization": authorization, "User-Agent": fua.random, "Accept": "text/plain",
           "Content-Type": "application/json"}
body = {"pan": "4182600317433042", "expiry": "01/23", "owner": 0}
response_createcard = request("POST", url, headers=headers, data=json.dumps(body))
ID_Card = response_createcard.json()

def test_CreditCard_headers():
    assert len(response_createcard.headers) == 4, "В объекте 4 значения"

def test_CreditCard_lenbody():
    assert len(body) == 3, "В body 3 значения"

def test_CreditCard_headers_content_type():
    assert response_createcard.headers['Content-Type'] == 'application/json; charset=utf-8', "Хедер Content-Type"

def test_CreditCard_Body():
    assert isinstance(body["pan"], (str)), "Поле pan строка"
    assert isinstance(body["expiry"], (str)), "Поле expiry строка"
    assert isinstance(body["owner"], (int)), "Поле owner число"

def test_CreditCard_Body_value_count_pan():
    assert len(body["pan"]) == 16, "В поле pan 16 символов"

def test_CreditCard_Body_value_count_expiry():
    assert len(body["expiry"]) == 5, "В поле expiry 5 символов"

def test_CreditCard_Body_value_count_owner():
    assert len(str(body["owner"])) != 0, "В поле owner есть символы"

def test_CreditCard_Body_value_count_owner_min():
    assert len(str(body["owner"])) >= 1, "В поле owner >= 1 символа"

def test_CreditCard_Body_value_count_owner_max():
    assert len(str(body["owner"])) <= 18, "В поле owner <= 18 символов"

def test_CreditCard_status_code():
    assert response_createcard.status_code == 200, "Код выполнения запроса 200"


"""Проверка наличия карты в системе"""

Value_CreditCardId = str(ID_Card)
Value_PageNumber = 0
Value_PageSize = 0
PN = "PageNumber="
PS = "PageSize="
a = "&"
EVENT_ID = "api/AccessLogs?"
now = datetime.now().isoformat()
url = f"{Base_URL}{EVENT_ID}{Value_CreditCardId}{a}{PN}{Value_PageNumber}{a}{PS}{Value_PageSize}"
headers = {"Authorization": authorization, "User-Agent": fua.random, "Accept": "text/plain"}
response_Accesslog = request("GET", url, headers=headers)


def test_AccessLogs_headers():
    assert len(response_Accesslog.headers) == 4, "В объекте 4 значения"

def test_AccessLogs_headers_content_type():
    assert response_Accesslog.headers['Content-Type'] == 'application/json; charset=utf-8', "Хедер Content-Type"

def test_AccessLogs_Query_Params():
    assert isinstance(Value_CreditCardId, (str)), "Параметр CreditCardId строка"
    assert isinstance(Value_PageNumber, (int)), "Параметр PageNumber число"
    assert isinstance(Value_PageSize, (int)), "Параметр PageSize число"

def test_AccessLogs_status_code():
    assert response_Accesslog.status_code == 200, "Код выполнения запроса 200"

"""Редактирование данных карты"""

EVENT_ID = "api/CreditCard/"
now = datetime.now().isoformat()
url = f"{Base_URL}{EVENT_ID}{ID_Card}"
headers = {"Authorization": authorization, "User-Agent": fua.random, "Accept": "text/plain",
           "Content-Type": "application/json"}
body = {"pan": "4182600317433042", "expiry": "01/28", "owner": 42}
response_PUT = request("PUT", url, headers=headers, data=json.dumps(body))


def test_PUT_api_CreditCard_id_status_code():
    assert response_PUT.status_code == 200, "Код выполнения запроса 200"

"""Удаление данных карты"""

EVENT_ID = "api/CreditCard/"
now = datetime.now().isoformat()
url = f"{Base_URL}{EVENT_ID}{ID_Card}"
headers = {"Authorization": authorization, "User-Agent": fua.random, "Accept": "*/*",
           "Content-Type": "application/json"}
response_DELETE = request("DELETE", url, headers=headers)

def test_DELETE_api_CreditCard_id_status_code():
    assert response_DELETE.status_code == 200, "Код выполнения запроса 200"
