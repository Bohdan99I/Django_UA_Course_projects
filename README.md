# Django_UA_Course_projects

## ІНСТРУКЦІЯ ПО ЗАПУСКУ DJANGO БЛОГУ

1. Встановіть Django:
   pip install -r requirements.txt

2. Створіть базу даних та застосуйте міграції:
   python manage.py makemigrations
   python manage.py migrate

3. Створіть суперкористувача для доступу до адмін-панелі:
   python manage.py createsuperuser

4. Запустіть сервер:
   python manage.py runserver

5. Відкрийте браузер:
   - Головна сторінка: http://127.0.0.1:8000/
   - Адмін-панель: http://127.0.0.1:8000/admin/
