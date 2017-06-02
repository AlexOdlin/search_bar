# Search Bar

Homework №2

Проект **Search Bar** создан для нахождения ближайшего из московских баров по введенным координатам. Входные данные пользователь вводит с клавиатуры.

Программа получает на вход следующие данные для дальнейшей работы:
* data - массив данных, загруженный из базы данных Bars.json, содержащий список московских баров.
* longitude - долгота пользователя
* latitude - широта пользователя

Методы модуля search_bar:
* load_data() - загрузка данных из Bars.json
* get_closest_bar() - нахождение ближйшего бара

Выходными данными являются:
1. Название бара - успешное выполнение программы
2. None - если загрузка из Bars.json не удалась (массив пустой) или если широта/долгота не заданы
3. SyntaxError - если формат данных является невалидным

Тестирование модуля осуществляется с помощью фреймворка PyTest, тесты содержатся в файле get_closest_bar_test.py в директории search_bar

[![Build Status](https://travis-ci.org/AlexOdlin/search_bar.svg?branch=master)](https://travis-ci.org/AlexOdlin/search_bar)
