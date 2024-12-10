import allure

from methods.courier_methods import CourierMethods


class TestCourier:
    @allure.title('Проверяем успешное создание курьера, ожидаем статус-код 201 и что в ответе будет "ok: True"')
    def test_courier_create_success(self):
        courier_methods = CourierMethods()

        response, login, password, first_name = courier_methods.courier_create()

        assert response.status_code == 201 and response.json().get("ok") == True, \
            f"Ожидаем статус-код 201 и 'ok: true', получили статус-код {response.status_code} и ответ {response.json()}"
        response_id, courier_id = courier_methods.get_id_courier(login, password)
        response_delete = courier_methods.delete_courier(courier_id)
        assert response_delete.status_code == 200, f"Ожидаем статус-код 200 при удалении, получили {response_delete.status_code}"
    @allure.title('Проверяем создание 2х курьеров с одинаковыми данными,первое создание ожидаем 201, второе 409 и '
                  'текст, что логин уже испольхуется')
    def test_courier_create_duplicate(self):
        courier_methods = CourierMethods()

        response_1, response_2, login, password, first_name = courier_methods.courier_create_duplicate()

        assert response_1.status_code == 201, f"Ожидаем статус 201, получили {response_1.status_code}"
        assert response_2.status_code == 409 and response_2.json().get(
            "message") == "Этот логин уже используется. Попробуйте другой.", \
            f"Ожидаем статус 409 и сообщение об ошибке 'Этот логин уже используется. Попробуйте другой.', " \
            f"получили статус {response_2.status_code} и сообщение: {response_2.json().get('message')}"
        response_id, courier_id = courier_methods.get_id_courier(login, password)
        assert courier_id, "Не удалось найти курьера для удаления"
        response_delete = courier_methods.delete_courier(courier_id)
        assert response_delete.status_code == 200, f"Ожидаем статус-код 200 при удалении, получили {response_delete.status_code}"

    @allure.title('Проверяем создание курьера, без логина, ожидаем 400 и текст о нехватке данных')
    def test_courier_create_without_login(self):
        courier_methods = CourierMethods()

        response = courier_methods.courier_create_without_login()

        assert response.status_code == 400 and response.json().get(
            "message") == "Недостаточно данных для создания учетной записи", \
            f"Ожидаем статус 400 и сообщение 'Недостаточно данных для создания учетной записи', " \
            f"получили статус {response.status_code} и сообщение: {response.json().get('message')}"

    @allure.title('Проверяем создание курьера, без пароля, ожидаем 400 и текст о нехватке данных')
    def test_courier_create_without_password(self):
        courier_methods = CourierMethods()

        response = courier_methods.courier_create_without_password()

        assert response.status_code == 400 and response.json().get(
            "message") == "Недостаточно данных для создания учетной записи", \
            f"Ожидаем статус 400 и сообщение 'Недостаточно данных для создания учетной записи', " \
            f"получили статус {response.status_code} и сообщение: {response.json().get('message')}"

    @allure.title('Проверяем успешную авторизацию курьера, ожидаем 200 и что в ответе будет id курьера')
    def test_courier_login(self):
        courier_methods = CourierMethods()

        response, login, password, first_name = courier_methods.courier_create()
        response_id, courier_id = courier_methods.get_id_courier(login, password)

        assert response_id.status_code == 200 and "id" in response_id.json(), \
            f"Ожидаем статус 200 и наличие поля 'id', " \
            f"получили статус {response_id.status_code} и ответ: {response_id.json()}"
        response_delete = courier_methods.delete_courier(courier_id)
        assert response_delete.status_code == 200

    @allure.title('Проверяем аторизацию курьера, без логина, ожидаем 400 и текст о нехватке даных')
    def test_courier_without_login(self):
        courier_methods = CourierMethods()

        response = courier_methods.courier_without_login()

        assert response.status_code == 400, f"Ожидаем статус 400, получили {response.status_code}"
        assert response.json().get("message") == "Недостаточно данных для входа", \
            f"Ожидаем сообщение об ошибке, получили: {response.json()}"

    @allure.title('Проверяем аторизацию курьера, без пароля, ожидаем 400 и текст о нехватке даных')
    def test_courier_without_password(self):
        courier_methods = CourierMethods()

        response = courier_methods.courier_without_password()

        assert response.status_code == 400, f"Ожидаем статус 400, получили {response.status_code}"
        assert response.json().get("message") == "Недостаточно данных для входа", \
            f"Ожидаем сообщение об ошибке, получили: {response.json()}"

    @allure.title('Проверяем авторизацию с не существующем логином, ждем 400 и текст учетная запись не найдена')
    def test_courier_login_with_non_existent_login(self):
        courier_methods = CourierMethods()

        response = courier_methods.courier_login_with_non_existent_login()

        assert response.status_code == 404, f"Ожидаем статус 404, получили {response.status_code}"
        assert response.json().get("message") == "Учетная запись не найдена", \
            f"Ожидаем сообщение об ошибке, получили: {response.json()}"

    @allure.title('Проверяем авторизацию с не существующем паролем, ждем 400 и текст учетная запись не найдена')
    def test_courier_login_with_invalid_password(self):
        courier_methods = CourierMethods()

        response, login, password, first_name = courier_methods.courier_create()

        response_invalid_login = courier_methods.courier_login_with_invalid_password(login, password)

        assert response_invalid_login.status_code == 404 and response_invalid_login.json().get(
            "message") == "Учетная запись не найдена", \
            f"Ожидаем статус 404 и сообщение 'Учетная запись не найдена', получили: статус {response_invalid_login.status_code}, " \
            f"сообщение: {response_invalid_login.json().get('message')}"
