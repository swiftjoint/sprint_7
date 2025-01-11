import allure
import requests

from config_urls import BASE_URL, ORDERS_URL, GET_ORDER_LIST


class OrderMethods:
    @allure.step('Отправляем запрос, на создание заказа')
    def order_create(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, color):
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "metro_station": metro_station,
            "phone": phone,
            "rent_time": rent_time,
            "delivery_date": delivery_date,
            "color": color
        }
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=data)
        return response

    @allure.step('Отправляем запрос, на получение списка заказов')
    def get_orders_list(self):
        response = requests.get(f"{BASE_URL}{GET_ORDER_LIST}")
        return response.json()
