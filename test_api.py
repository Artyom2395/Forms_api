import requests

# URL приложения
BASE_URL = "http://127.0.0.1:8000"

# Список тестовых данных для отправки
test_data_list = [
    {
        "user_email": "test@example.com",
        "user_phone": "+7 900 123 45 67"
    },
    {
        "customer_email": "test@customer.com", 
        "message": "Hello, world =))"
    },
    {
        "username": "John", 
        "password": "john123", 
        "birth_date": "07.07.1995"
    },
    {
        "user_email": "test@example.com",
        "user_phone": "+7 900 123 45 67",
        "message": "Hello, world =))"
    },
    {
        "username": "John",
        "surname": "Smith",
        "password": "john123",
        'keyword': "john",
        "birth_date": "07.07.1934"
    },
    {
        "admin_email": "test@admin.com",
        "admin_phone": "+7 777 000 33 22",
        "admin_privileges": "yes"
    },
]

# Отправка POST запросов для тестирования
for test_data in test_data_list:
    response = requests.post(f"{BASE_URL}/get_form", json=test_data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print("--------------------------")

