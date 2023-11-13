from tinydb import TinyDB

db = TinyDB('db.json')

# Создаем таблицы и добавляем записи
forms_table = db.table('_default')

forms_table.insert({
    "name": "ContactForm",
    "fields": {
        "user_email": "email",
        "user_phone": "phone"
    }
})

forms_table.insert({
    "name": "RegistrationForm",
    "fields": {
        "username": "text",
        "password": "text",
        "birth_date": "date"
    }
})

forms_table.insert({
    "name": "FeedbackForm",
    "fields": {
        "customer_email": "email",
        "message": "text"
    }
})