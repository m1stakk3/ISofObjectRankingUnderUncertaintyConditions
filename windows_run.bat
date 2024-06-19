@echo off

if not exist venv (
    rem Создаем виртуальное окружение
    python -m venv venv
)

rem Активируем виртуальное окружение
call venv\Scripts\activate

rem Устанавливаем зависимости
python -m pip install -r requirements.txt

rem Запускаем скрипт
python main.py
