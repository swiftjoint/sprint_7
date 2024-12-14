import allure
import requests

from config_urls import BASE_URL, COURIER_URL, LOGIN
from data import LOGIN_DATA_1, LOGIN_DATA_DUBLICATE
from helpers import register_new_courier_and_return_login_password


class CourierMethods:
    @allure.step('Отправляем запрос, на создание курьера')
    @allure.description('Запрос на ручку api/v1/courier/, данные для регистрации создает метод '
                        'register_new_courier_and_return_login_password')
    def courier_create(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f"{BASE_URL}{COURIER_URL}", json=payload)
        return response, login, password, first_name

    @allure.step('Отправляем запрос, на создание 2х курьеров, с одинаковыми данными')
    @allure.description('Запрос на ручку api/v1/courier/, данные статичные, хранятся в файле data,LOGIN_DATA_DUBLICATE')
    def courier_create_duplicate(self):
        payload = LOGIN_DATA_DUBLICATE
        response_1 = requests.post(f"{BASE_URL}{COURIER_URL}", json=payload)
        response_2 = requests.post(f"{BASE_URL}{COURIER_URL}", json=payload)
        login = payload["login"]
        password = payload["password"]
        first_name = payload["first_name"]
        return response_1, response_2, login, password, first_name

    @allure.step('Отправляем запрос, на создание курьера, без логина и пароля')
    @allure.description('Запрос на ручку api/v1/courier/, данные статичные, хранятся в файле data, '
                        'TEST_DATA_3')
    def courier_create_without_login_and_password(self, login, password, first_name):
        data = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        response = requests.post(f"{BASE_URL}{COURIER_URL}", json=data)
        return response

    @allure.step('Отправляем запрос, на авторизацию курьера, без логина и пароля')
    @allure.description('Запрос на ручку api/v1/courier/login/, данные статичные, хранятся в файле data, '
                        'TEST_DATA_2')
    def courier_without_login_and_password(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(f"{BASE_URL}{COURIER_URL}{LOGIN}", json=data)
        return response


    @allure.step('Отправляем запрос, на авторизацию курьера, с несуществующим логином')
    @allure.description('Запрос на ручку api/v1/courier/login/, данные статичные, хранятся в файле data, '
                        'LOGIN_DATA_1')
    def courier_login_with_non_existent_login(self):
        payload = LOGIN_DATA_1
        response = requests.post(f"{BASE_URL}{COURIER_URL}{LOGIN}", json=payload)
        return response

    @allure.step('Отправляем запрос, на авторизацию курьера, с несуществующим паролем')
    @allure.description('Запрос на ручку api/v1/courier/login/, метод принимает логин и пароль, потом к паролю '
                        'добавляет слово')
    def courier_login_with_invalid_password(self, login, password):
        invalid_password = password + "wrong"
        payload = {
            "login": login,
            "password": invalid_password
        }
        response = requests.post(f"{BASE_URL}{COURIER_URL}{LOGIN}", json=payload)
        return response

    @allure.step('Отправляем запрос, на авторизацию курьера')
    @allure.description('Запрос на ручку api/v1/courier/login/, метод принимает логин и пароль, затем получает id '
                        'курьера')
    def get_id_courier(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        response_id = requests.post(f"{BASE_URL}{COURIER_URL}{LOGIN}", json=payload)
        if response_id.status_code == 200:
            courier_id = response_id.json().get("id")
        else:
            courier_id = None

        return response_id, courier_id

    @allure.step('Отправляем запрос, на удаление курьера')
    @allure.description('Запрос на ручку api/v1/courier/, метод принимает id курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f"{BASE_URL}{COURIER_URL}{courier_id}")
        return response
