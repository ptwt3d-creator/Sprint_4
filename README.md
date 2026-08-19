# qa_python

## Перечень тестов

- `test_add_new_book_add_two_books`

- `test_set_genre_to_book_validation_genre_in_list_and_not_in_list`

- `test_add_book_in_favorites_add_book`

- `test_delete_book_from_favorites_add_and_del_book`

- `test_get_list_of_favorites_books_add_and_get_book`

- `test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book`

- `test_get_books_for_children_rate_and_not_rate_book`

- `test_get_book_genre_add_book_set_get_genre`

- `test_get_books_genre_add_book_get_list_book_genre`

- `test_add_new_book_name_len_validation`

- `test_add_new_book_add_two_identical`

## Перечень фикстур

- `collector_book`

## Описание тестов

- `test_add_new_book_add_two_books` - Добавление в коллекцию 2 книг

- `test_set_genre_to_book_validation_genre_in_list_and_not_in_list` - параметризованный, Проверка валидации при установке жанра (Сейчас проверяется только присвоение существующего и несуществующего в списке жанра).

- `test_add_book_in_favorites_add_book` - Проверка добавления книги в избранное.

- `test_delete_book_from_favorites_add_and_del_book` - Проверка удаления книги из списка избранных.

- `test_get_list_of_favorites_books_add_and_get_book` - Проверка получения списка избранных книг.

- `test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book` - параметризованный, Проверка вывода списка книг по жанру (сейчас проверяется только что выведены книги запрошенного жанра и что не выводятся книги чей жанр отличается от запрашиваемого).

- `test_get_books_for_children_rate_and_not_rate_book` - параметризованный, Проверка возрастного ограничения книг, вывод списка из книги без ограничений возраста и проверка то что книги с ограничением возраста не попадают в список 'для детей'.

- `test_get_book_genre_add_book_set_get_genre` - Проверка получения жанра по названию книги.

- `test_get_books_genre_add_book_get_list_book_genre` - Проверка вывода списка книг.

- `test_add_new_book_name_len_validation` - Валидация длины имени книги 0 - 42 символа.

- `test_add_new_book_add_two_identical` - Проверка, что дубликаты книг не добавляются в коллекцию повторно.

## Описание фикстур

- `collector` - Создание чистого объекта BooksCollector перед каждым тестом.