# Выпускная квалификационная работа

## Тема "Проектирование интеллектуальной системы ранжирования в условиях неопределенности"

---
* Кабардино-Балкарский Государственный Университет им. Х.М. Бербекова
* Институт Искусственного Интеллекта и Цифровых Технологий
* Информатика и вычислительная техника

---

## Постановка задачи
```
Имеется статистика игроков NBA с разбивкой по командам. Требуется определить наиболее эффективных игроков на количество сыгранного времени.
Требуется провести сравнение на основе данных за сезон 2023-2024. 
Подход с использованием fuzzy нейросети (нечеткая логика) должен помочь совершить обезличенный выбор, без человеческого фактора и случайных временных колебаний показателей игроков по ходу игрового сезона.
```
## Окружение
* Возможность кроссплатформенного запуска (Windows, Linux, MacOS)
* Python 3.11+ (на MacOS желателен запуск под 3.11)
* Flask web server для GUI через браузер

---

## Как запустить?
* в папке с программой вызвать CMD и создать виртуальное окружение:
```commandline
python -m venv venv
```
* активировать виртуальное окружение:
  * на Windows:
      ```commandline
      venv\Scripts\activate
      ```
  * на Unix
    ```commandline
    source venv/bin/activate
    ```
* установить зависимости
```commandline
python -m pip install -r requirements.txt
```
* запустить программу
```commandline
python main.py
```
---
### Источник данных

https://www.basketball-reference.com/teams/