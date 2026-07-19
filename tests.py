from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector_book(self):
        self.collector = BooksCollector()
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса Booksself.self.collector
        # добавляем две книги
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(self.collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    @pytest.mark.parametrize(
        'book, genre, is_in_list_genre',
        [
            ('Что делать, если ваш кот хочет вас убить', 'Комедии', True),
            ('Что делать, если ваш кот хочет вас убить', 'Синий', False)
        ]
    )
    def test_set_genre_to_book_validation_genre_in_list_and_not_in_list(self, book, genre, is_in_list_genre):
        
        self.collector.add_new_book(book)
        self.collector.set_book_genre(book, genre)
        
        result = self.collector.get_book_genre(book) == genre
        assert result == is_in_list_genre

    def test_add_book_in_favorites_add_book(self):
        self.collector.add_new_book('Букварь')
        self.collector.add_book_in_favorites('Букварь')

        assert 'Букварь' in self.collector.favorites

    def test_delete_book_from_favorites_add_and_del_book(self):
        book = 'Букварь'

        self.collector.add_new_book(book)
        assert book in self.collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'
        
        self.collector.add_book_in_favorites(book)
        assert book in self.collector.favorites, 'Книга не добавилась в favorites - необходимо для продолжения теста'
        
        self.collector.delete_book_from_favorites(book)
        assert book not in self.collector.favorites

    def test_get_list_of_favorites_books_add_and_get_book(self):
        book = 'Букварь2.0'

        self.collector.add_new_book(book)
        assert book in self.collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'
        
        self.collector.add_book_in_favorites(book)
        assert book in self.collector.favorites, 'Книга не добавилась в favorites - необходимо для продолжения теста'

        assert book in self.collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'book, genre, is_requested',
        [
            ('Дневник кота-убийцы', 'Комедии', True),
            ('оно', 'Ужасы', False)
        ]
    )
    def test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book(self, book, genre, is_requested):
        self.collector.add_new_book(book)
        assert book in self.collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'

        self.collector.set_book_genre(book, genre)
        assert genre in self.collector.books_genre[book] , 'Книге в books_genre не добавился genre - необходимо для продолжения теста'
        
        result = book in self.collector.get_books_with_specific_genre('Комедии')
        assert result == is_requested
    
    @pytest.mark.parametrize(
        'book, genre, is_child_book',
        [
            ('Бойцовский клуб', 'Детективы', False),
            ('Винни-Пух', 'Комедии', True)
        ]
    )
    def test_get_books_for_children_rate_and_not_rate_book(self, book, genre, is_child_book):

        self.collector.add_new_book(book)
        assert book in self.collector.books_genre , 'Книга не добавилась в books_genre - необходимо для продолжения теста'

        self.collector.set_book_genre(book, genre)
        assert genre in self.collector.books_genre[book] , 'Книге в books_genre не добавился genre - необходимо для продолжения теста'
        
        result = book in self.collector.get_books_for_children()
        assert result == is_child_book
        