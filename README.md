# "Практикум по программированию". Лабораторная работа №1

## Реализованные тесты
В данной работе реализованы следующие тесты:
1. Добавление и удаление нескольких товаров в корзину
2. Проверка сохранения содержимого корзины после выхода из системы и повторного входа
3. Проверка сортировки товаров по цене
4. Оформление заказа
5. Добавление одного товара в корзину
6. Проверка успешного входа в систему


Для работы с проектом необходимо клонировать репозиторий:

```bash
git clone https://github.com/OverCart345/omgtu_practticum/tree/e2e
```

Установить необходимые зависимости:

```bash
pip install -r requirements.txt
```

Установить браузеры Playwright следующей командой:

```bash
python -m playwright install
```

После установки зависимостей вы можете запустить тесты с помощью команды:

```bash
pytest
```