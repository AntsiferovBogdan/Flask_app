Flask-приложение
=====
Данное приложение создано в рамках изучения Flask. Сайт занимается сбором новостей, отображает текущую погоду, а также имеет функционал регистрации и авторизации пользователей.

Установка
---------
Создайте и активируйте виртуальное окружение:

.. code-block:: text

    pip install -r requirements.txt

Настройка
---------
Создайте файл config.py, добавьте следующие настройки:

.. code-block:: python

  import os

  from datetime import timedelta

  basedir = os.path.abspath(os.path.dirname(__file__))

  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                        '..', 'webapp.db'
                                                        )
  WEATHER_DEFAULT_CITY = 'CITY,COUNTRY'
  WEATHER_API_KEY = 'API_KEY'
  WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

  SECRET_KEY = 'SECRET_KEY'
  REMEMBER_COOKIE_DURATION = timedelta(days=30)

  SQLALCHEMY_TRACK_MODIFICATIONS = False

Запуск
-------

В активированном виртуальном окружении введите:

.. code-block:: text

    ./run.sh
