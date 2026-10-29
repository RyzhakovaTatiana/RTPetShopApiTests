import pytest
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"

@pytest.fixture(scope = "function")
def create_pet():
    payload = {"id": 1,
                "name": "Buddy",
                "status": "available"}
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200, "Не удалось создать питомца в фикстуре"
    return response.json() #получение ответа без удаления питомца
    #yield response.json() #получение ответа с удалением данных о питомце
    #requests.delete(f"{BASE_URL}/pet/{payload["id"]}") # отправка запроса на удаление данных о питомце
