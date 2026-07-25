from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает нам метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    @pytest.mark.parametrize(
        'book, genre, expected_genre',
        [
            ('Что делать, если ваш кот хочет вас убить', 'Комедии', 'Комедии'),
            ('Что делать, если ваш кот хочет вас убить', 'Синий', '')
        ]
    )
    def test_set_genre_to_book_validation_genre_in_list_and_not_in_list(self, collector, book, genre, expected_genre):
        
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        
        assert collector.get_book_genre(book) == expected_genre

    def test_add_book_in_favorites_add_book(self, collector):
        book = 'Букварь'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        
        assert book in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_add_and_del_book(self, collector):
        book = 'Букварь'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert book not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_and_get_book(self, collector):
        book = 'Букварь'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'book, genre, is_requested',
        [
            ('Дневник кота-убийцы', 'Комедии', True),
            ('Оно', 'Ужасы', False)
        ]
    )
    def test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book(self, collector, book, genre, is_requested):
        
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        
        result = book in collector.get_books_with_specific_genre('Комедии')
        assert result == is_requested
    
    @pytest.mark.parametrize(
        'book, genre, is_child_book',
        [
            ('Бойцовский клуб', 'Детективы', False),
            ('Винни-Пух', 'Комедии', True)
        ]
    )
    def test_get_books_for_children_rate_and_not_rate_book(self, collector, book, genre, is_child_book):

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        
        result = book in collector.get_books_for_children()
        assert result == is_child_book

    def test_get_book_genre_add_book_set_get_genre(self, collector):

        book ='Десять негритят'
        genre = 'Детективы'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_books_genre_add_book_get_list_book_genre(self, collector):
        collector.add_new_book('Федотов, заверните кота!')

        assert 'Федотов, заверните кота!' in collector.get_books_genre()
        