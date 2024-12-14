TEST_DATA = [
    ("geraone", "Uchiho", "Гоголя 150", 1, "+7 800 355 35 50", 1, "2024-12-15", ["BLACK"]),
    ("geratwo", "Uchiho", "Гоголя 150", 1, "+7 800 355 35 50", 1, "2024-12-15", ["BLACK", "GRAY"]),
    ("gerafree", "Uchiho", "Гоголя 150", 1, "+7 800 355 35 50", 1, "2024-12-15", [])
]
TEST_DATA_2 = [
    ("", "Qwe123"),
    ("Quesnelle", "")
]
TEST_DATA_3 = [
    ("", "Qwe123", "Wilson"),
    ("Quesnelle", "", "Wilson")
]
LOGIN_DATA_1 = {
    "login": "Quesnelle",
    "password": "Qwe123"
}
LOGIN_DATA_DUBLICATE = {
    "login": "Quesnelle",
    "password": "Qwe123",
    "first_name": "Wilson"
}
SUCCESS_STATUS_CODE = 201
AUTH_SUCCESS_STATUS_CODE = 200
DUPLICATE_STATUS_CODE = 409
EXPECTED_STATUS_CODE = 400
DUPLICATE_MESSAGE = "Этот логин уже используется. Попробуйте другой."
COURIER_CREATE_WITHOUT_LOGIN_AND_PASSWORD_MESSAGE = "Недостаточно данных для создания учетной записи"
AUTH_SUCCESS_MESSAGE = "id"
AUTH_WITHOUT_LOGIN_PASSWORD_MESSAGE = "Недостаточно данных для входа"
AUTH_INVALID_LOGIN_PASSWORD_STATUS_CODE = 404
AUTH_INVALID_LOGIN_PASSWORD_MESSAGE = "Учетная запись не найдена"
EXPECTED_MESSAGE = "track"
ORDERS_MESSAGE = "orders"
