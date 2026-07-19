# qa_python

## Перечень тестов

- test_add_new_book_add_two_books

- test_set_genre_to_book_validation_genre_in_list_and_not_in_list

- test_add_book_in_favorites_add_book

- test_delete_book_from_favorites_add_and_del_book

- test_get_list_of_favorites_books_add_and_get_book

- test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book

- test_get_books_for_children_rate_and_not_rate_book

## Описание тестов

- test_add_new_book_add_two_books - Добавление 2 книг в словарь books_genre.

- test_set_genre_to_book_validation_genre_in_list_and_not_in_list - параметризованный, Добавление книги в словарь books_genre, Проверка добавления существующего/несуществующего в списке жанров(genre) жанра в словарь books_genre, Сравнение результата проверки добавления с ОР нахождения в словаре жанра в списке genre — is_in_list_genre.

- test_add_book_in_favorites_add_book - Добавление книги в словарь books_genre, Добавление книги в список избранных favorites.

- test_delete_book_from_favorites_add_and_del_book - Добавление книги в словарь books_genre, Добавление книги в список избранных favorites, Удаление книги из списка избранных favorites.

- test_get_list_of_favorites_books_add_and_get_book - Добавление книги в словарь books_genre, Добавление книги в список избранных favorites, Получение списка книг из списка избранных favorites.

- test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book - параметризованный, Добавление книги в словарь books_genre, Добавление жанра книге в словарь books_genre, Запись ФР проверки - есть ли книга жанра 'n' в запрошенном по жанру списке книг, Сравнение ФР с ОР параметр is_requested.

- test_get_books_for_children_rate_and_not_rate_book - параметризованный, Добавление книги в словарь books_genre, добавление жанра книге в словарь books_genre, запись результата проверка на принадлежность жанра списку жанров с ограничением возраста genre_age_rating, Сравнение ФР проверки с ОР параметр is_child_book.
