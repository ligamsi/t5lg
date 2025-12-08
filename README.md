# Футбол - статистика

Веб-приложение на Django, которое показывает турнирные таблицы и статистику игроков в топ-лигах Европы.
Пользователь выбирает лигу и видит:
- турнирную таблицу
- статистику игроков

## 
Стек:

- Python 3.10
- Django
- PostgreSQL
- HTML + Bootstrap (CDN)

Основной шаблон: main_page.html, общий макет - base.html.

## Установка и запуск
1. Клонирование репозитория

```bash
git clone https://github.com/ligamsi/t5lg.git
cd t5lg
```

2. Создать виртуальное окружение и активировать его

```bash
python -m venv venv
venv\Scripts\activate
```
3. Установить зависимости
   
```bash
pip install -r requirements.txt
```

4. Создать файл .env в корне:

```ini
POSTGRES_DB=t5lgdb
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

5. Выполнить миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Создать суперпользователя

```bash
python manage.py createsuperuser
```

7. Запустить сервер

```bash
python manage.py runserver
```

##
Структура:
- League - модель лиги
- Team - уникальная команда
- TeamInLeague - статистика команды в конкретной лиге
- Player - игрок
- PlayerInLeague - статистика игрока в конкретной лиге
