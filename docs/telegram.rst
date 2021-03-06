Телеграм
========

Подключаем бота
----------------

Через ЛК
^^^^^^^^

После регистрации пользователь может подключить телеграм бота. 
В ЛК ставновится кликабельной кнопка:

.. image:: _static/tg/tg_button.png

.. note::
    Кнопка содержит ссылку с уникальным кодом следующего вида:

    ``https://telegram.me/comon_tg_bot?start=46e15db7661d0663``
    
    Код позволяет идентифицировать пользователя и связать его учетную запись в тг с учетной записью в MoneyWork.


После клика происходит редирект в телеграм. И если нажать ``/start`` - мы успешно заинтегрируем пользователя:

.. image:: _static/tg/bot_connected.png


Через бота напрямую
^^^^^^^^^^^^^^^^^^^^

Если случайный пользователь откроет бота, 
то при попытке интерактива, 
ему предложат регистрацию на сайте:

.. image:: _static/tg/start_bot.png

Базовые команды
---------------

.. image:: _static/tg/commands.png

Cуществует три команды:
 - /start
 - /account
 - /help


 Команда  ``/start`` описана выше



 Команда ``/account`` выдает пользователю данные его профиля со статусами по подписке:

 .. image:: _static/tg/bot_account.png



 
 Команда ``/help`` служит мостиком между тех поддержкой и пользователем

 Алгоритм работы следующий:

 
 .. mermaid::

    graph TD
        A[Команда /support] --> B[Просьба описать вопрос];
        B --> C[Ввод вопроса];
        C --> Y{Отправить вопрос?}
        Y -- Да --> E[Отправка вопроса в саппорт]
        E --> G
        Y -- Нет --> G[Завершение]

Пример из интерфейса:

Вопрос от пользователя:

.. image:: _static/tg/bot_support_ask.png

Ответ от тех-поддержки через бота:

.. image:: _static/tg/bot_support_answer.png

.. note::
    Описание работы тех-поддержки в другом разделе





Долгоживущая сессия чата с тех-поддержкой
-----------------------------------------
    
.. warning::
    Это обновленная логика работы с тех-поддержкой
    

.. image:: _static/tg/help.gif
    
    