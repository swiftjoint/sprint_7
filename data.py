TEST_DATA = [
    ("geraone", "Uchiho", "Гоголя 150", 1, "+7 800 355 35 50", 1, "2024-12-15", ["BLACK"]),
    ("geratwo", "Uchiho", "Гоголя 150", 1, "+7 800 355 35 50", 1, "2024-12-15", ["BLACK", "GRAY"]),
    ("gerafree", "Uchiho", "Гоголя 150", 1, "+7 800 355 35 50", 1, "2024-12-15", [])
]
LOGIN_DATA_1 = {
    "login": "Quesnelle",
    "password": "Qwe123"
}
LOGIN_DATA_2 = {
    "login": "",
    "password": "Qwe123"
}
LOGIN_DATA_3 = {
    "login": "Quesnelle",
    "password": ""
}
LOGIN_DATA_WITHOUT_LOGIN = {
    "login": "",
    "password": "Qwe123",
    "first_name": "Wilson"
}
LOGIN_DATA_WITHOUT_PASSWORD = {
    "login": "Quesnelle",
    "password": "",
    "first_name": "Wilson"
}
LOGIN_DATA_DUBLICATE = {
    "login": "Quesnelle",
    "password": "Qwe123",
    "first_name": "Wilson"
}
