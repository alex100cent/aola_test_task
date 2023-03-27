# Test task for Aola
## Инструкция как запустить приложение
1. Отредактируйте файл `./aola/aola/.env`. Вам нужно указать ваши значения для переменных, добавлять переменные не нужно.
2. (опционально) если вы используете `pyenv` активируйте нужную версию python командой `pyenv local 3.11.1`. Если нужной версии python нет, то установите командой `pyenv install python 3.11.1`
3. Установите зависимости командой `poetry install`
4. Сделайте миграции `poetry run python3 manage.py migrate`
5. загрузите fixtures `poetry run python3 manage.py loaddata fixtures/data_dump.json`
6. Запустите тесты `poetry run python3 manage.py test main.tests`
7. Запустите приложение `poetrt run python3 manage.py runserver`
8. В программе Postman импортируйте `postman_collection.json` и сделайте запросы