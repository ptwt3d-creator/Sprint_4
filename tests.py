from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector_book(self):
        self.collector = BooksCollector()

    @pytest.fixture
    def favorite_book(self):
        book_in_favorites = 'Букварь'

        self.collector.add_new_book(book_in_favorites)
        self.collector.add_book_in_favorites(book_in_favorites)

        return book_in_favorites
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # добавляем две книги
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает нам метод get_books_genre, имеет длину 2
        assert len(self.collector.get_books_genre()) == 2

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

    def test_add_book_in_favorites_add_book(self, favorite_book):

        assert favorite_book in self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_add_and_del_book(self, favorite_book):
        
        self.collector.delete_book_from_favorites(favorite_book)

        assert favorite_book not in self.collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_and_get_book(self, favorite_book):

        assert favorite_book in self.collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'book, genre, is_requested',
        [
            ('Дневник кота-убийцы', 'Комедии', True),
            ('оно', 'Ужасы', False)
        ]
    )
    def test_get_books_with_specific_genre_filtering_check_return_requested_and_not_requested_book(self, book, genre, is_requested):
        
        self.collector.add_new_book(book)
        self.collector.set_book_genre(book, genre)
        
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
        self.collector.set_book_genre(book, genre)
        
        result = book in self.collector.get_books_for_children()
        assert result == is_child_book

    def test_get_book_genre_add_book_set_get_genre(self):

        book ='Десять негритят'
        genre = 'Детективы'

        self.collector.add_new_book(book)
        self.collector.set_book_genre(book, genre)

        assert genre == self.collector.get_book_genre(book)

    def test_get_books_genre_add_book_get_list_book_genre(self):
        self.collector.add_new_book('Федотов, заверните кота!')

        assert 'Федотов, заверните кота!' in self.collector.get_books_genre()
        