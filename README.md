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

## ФУНКЦІОНАЛ:

- Перегляд всіх статей на головній сторінці
- Перегляд окремої статті за посиланням
- Фільтрування статей за тегами
- Пагінація (10 статей на сторінку)
- Адмін-панель для управління статтями та тегами

## СТРУКТУРА ПРОЕКТУ:

blog_project/         # Основний проект
├── settings.py       # Налаштування проекту
├── urls.py          # Головні URL
├── wsgi.py          # WSGI конфігурація
└── asgi.py          # ASGI конфігурація

blog/                # Застосунок блогу
├── models.py        # Моделі (Article, Tag)
├── views.py         # Відображення (article_list, article_detail)
├── urls.py          # URL маршрути блогу
└── admin.py         # Налаштування адмін-панелі

templates/           # Шаблони
├── base.html        # Базовий шаблон
└── blog/
    ├── article_list.html    # Список статей
    └── article_detail.html  # Деталі статті
