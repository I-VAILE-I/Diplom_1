## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ python -m pytest --cov --cov-report=html`
 

> Module	statements	missing	excluded	coverage
> __init__.py	0	0	0	100%
> praktikum\__init__.py	0	0	0	100%
> praktikum\bun.py	8	0	0	100%
> praktikum\database.py	21	0	0	100%
> praktikum\ingredient.py	11	2	0	82%
> praktikum\ingredient_types.py	2	0	0	100%
> tests\__init__.py	0	0	0	100%
> tests\test_data_base.py	26	3	0	88%
> Total	68	5	0	93%
