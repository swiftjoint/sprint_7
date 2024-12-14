import allure
import pytest

import data
from data import TEST_DATA_2, TEST_DATA_3
from methods.courier_methods import CourierMethods


class TestCourier:
    @allure.title('Проверяем успешное создание курьера, ожидаем статус-код 201 и что в ответе будет "ok: True"')
    def test_courier_create_success(self):
        courier_methods = CourierMethods()

        response, login, password, first_name = courier_methods.courier_create()

        assert response.status_code == data.SUCCESS_STATUS_CODE and response.json().get("ok") == True, \
            f"Ожидаем статус-код {data.SUCCESS_STATUS_CODE}, получили статус-код {response.status_code} и ответ {response.json()}"
        response_id, courier_id = courier_methods.get_id_courier(login, password)
        courier_methods.delete_courier(courier_id)

    @allure.title('Проверяем создание 2х курьеров с одинаковыми данными,первое создание ожидаем 201, второе 409 и '
                  'текст, что логин уже испольхуется')
    def test_courier_create_duplicate(self):
        courier_methods = CourierMethods()

        response_1, response_2, login, password, first_name = courier_methods.courier_create_duplicate()

        assert response_1.status_code == data.SUCCESS_STATUS_CODE, f"Ожидаем статус {data.SUCCESS_STATUS_CODE}, получили {response_1.status_code}"
        assert response_2.status_code == data.DUPLICATE_STATUS_CODE and response_2.json().get(
            "message") == data.DUPLICATE_MESSAGE, \
            f"Ожидаем статус{data.DUPLICATE_STATUS_CODE} и сообщение об ошибке {data.DUPLICATE_MESSAGE}" \
            f"получили статус {response_2.status_code} и сообщение: {response_2.json().get('message')}"
        response_id, courier_id = courier_methods.get_id_courier(login, password)
        if courier_id:
            courier_methods.delete_courier(courier_id)

    @allure.title('Проверяем создание курьера, без логина и пароля, ожидаем 400 и текст о нехватке данных')
    @pytest.mark.parametrize(
        "login, password, first_name", TEST_DATA_3
    )
    def test_courier_create_without_login_and_password(self, login, password, first_name):
        courier_methods = CourierMethods()

        response = courier_methods.courier_create_without_login_and_password(login, password, first_name)

        assert response.status_code == data.EXPECTED_STATUS_CODE and response.json().get(
            "message") == data.COURIER_CREATE_WITHOUT_LOGIN_AND_PASSWORD_MESSAGE, \
            f"Ожидаем статус {data.EXPECTED_STATUS_CODE} и сообщение {data.COURIER_CREATE_WITHOUT_LOGIN_AND_PASSWORD_MESSAGE}" \
            f"Получили статус {response.status_code} и сообщение: {response.json().get('message')}"


    @allure.title('Проверяем успешную авторизацию курьера, ожидаем 200 и что в ответе будет id курьера')
    def test_courier_login(self):
        courier_methods = CourierMethods()

        response, login, password, first_name = courier_methods.courier_create()
        response_id, courier_id = courier_methods.get_id_courier(login, password)

        assert response_id.status_code == data.AUTH_SUCCESS_STATUS_CODE and data.AUTH_SUCCESS_MESSAGE in response_id.json(), \
            f"Ожидаем статус {data.AUTH_SUCCESS_STATUS_CODE} и наличие поля {data.AUTH_SUCCESS_MESSAGE}," \
            f"Получили статус {response_id.status_code} и ответ: {response_id.json()}"
        courier_methods.delete_courier(courier_id)


    @allure.title('Проверяем аторизацию курьера, без логина и пароля, ожидаем 400 и текст о нехватке даных')
    @pytest.mark.parametrize(
        "login, password", TEST_DATA_2
    )
    def test_courier_without_login_and_password(self, login, password):
        courier_methods = CourierMethods()

        response = courier_methods.courier_without_login_and_password(login, password)

        assert response.status_code == data.EXPECTED_STATUS_CODE, f"Ожидаем статус {data.EXPECTED_STATUS_CODE}, получили {response.status_code}"
        assert response.json().get("message") == data.AUTH_WITHOUT_LOGIN_PASSWORD_MESSAGE, \
            f"Ожидаем сообщение {data.AUTH_WITHOUT_LOGIN_PASSWORD_MESSAGE}, получили: {response.json()}"

    @allure.title('Проверяем авторизацию с не существующем логином, ждем 400 и текст учетная запись не найдена')
    def test_courier_login_with_non_existent_login(self):
        courier_methods = CourierMethods()

        response = courier_methods.courier_login_with_non_existent_login()

        assert response.status_code == data.AUTH_INVALID_LOGIN_PASSWORD_STATUS_CODE, \
            f"Ожидаем статус {data.AUTH_INVALID_LOGIN_PASSWORD_STATUS_CODE}, получили {response.status_code}"
        assert response.json().get("message") == data.AUTH_INVALID_LOGIN_PASSWORD_MESSAGE, \
            f"Ожидаем сообщение {data.AUTH_INVALID_LOGIN_PASSWORD_MESSAGE}, получили: {response.json()}"

    @allure.title('Проверяем авторизацию с не существующем паролем, ждем 400 и текст учетная запись не найдена')
    def test_courier_login_with_invalid_password(self):
        courier_methods = CourierMethods()

        response, login, password, first_name = courier_methods.courier_create()

        response_invalid_login = courier_methods.courier_login_with_invalid_password(login, password)

        assert response_invalid_login.status_code == data.AUTH_INVALID_LOGIN_PASSWORD_STATUS_CODE and response_invalid_login.json().get(
            "message") == data.AUTH_INVALID_LOGIN_PASSWORD_MESSAGE, \
            f"Ожидаем статус {data.AUTH_INVALID_LOGIN_PASSWORD_STATUS_CODE} и сообщение {data.AUTH_INVALID_LOGIN_PASSWORD_MESSAGE}, получили: статус {response_invalid_login.status_code}, " \
            f"сообщение: {response_invalid_login.json().get('message')}"
