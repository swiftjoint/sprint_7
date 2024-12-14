import allure
import pytest

import data
from data import TEST_DATA
from methods.order_methods import OrderMethods


class TestOrder:
    @allure.title('Проверяем создание заказа, с тремя тестовыми данными, с один цветом, с двумя и без цвета')
    @pytest.mark.parametrize(
        "first_name, last_name, address, metro_station, phone, rent_time, delivery_date, color",
        TEST_DATA
    )
    def test_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, color):
        order_methods = OrderMethods()
        response = order_methods.order_create(
            first_name, last_name, address, metro_station, phone, rent_time, delivery_date, color
        )
        assert response.status_code == data.SUCCESS_STATUS_CODE, f"Ожидаем статус-код {data.SUCCESS_STATUS_CODE}, получили {response.status_code}"
        assert f"{data.EXPECTED_MESSAGE} in response.json(), Ожидаем, что в ответе будет поле {data.EXPECTED_MESSAGE}"

    @allure.title('Проверяем, что при запросе списка заказов, получаем в ответ список,и в нем есть orders')
    def test_get_order_list(self):
        order_methods = OrderMethods()
        response = order_methods.get_orders_list()
        assert data.ORDERS_MESSAGE in response, f"Ответ не содержит ключ {data.ORDERS_MESSAGE}"
        assert len(response["orders"]) >= 0
