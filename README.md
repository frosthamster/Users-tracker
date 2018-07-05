# Users tracker
Тестовое приложение на свзке `flask` + `bootstrap`


## Зависимости
- `Python` >=3.6
- Все модули из `requirements.txt`


## Запуск
```
py -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
set FLASK_APP=users_tracker.py
flask db upgrade
flask run
```