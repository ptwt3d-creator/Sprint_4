from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_genre_one_new_book(self):
        collector = BooksCollector()
        genre = 'Комедии'

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)

        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == genre

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Букварь')
        collector.add_book_in_favorites('Букварь')

        assert 'Букварь' in collector.favorites

    def test_delete_book_from_favorites_add_and_del_book(self):
        collector = BooksCollector()
        book = 'Букварь'

        collector.add_new_book(book)
        assert book in collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'
        
        collector.add_book_in_favorites(book)
        assert book in collector.favorites, 'Книга не добавилась в favorites - необходимо для продолжения теста'
        
        collector.delete_book_from_favorites(book)
        assert book not in collector.favorites

    def test_get_list_of_favorites_books_add_and_get_book(self):
        collector = BooksCollector()
        book = 'Букварь2.0'

        collector.add_new_book(book)
        assert book in collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'
        
        collector.add_book_in_favorites(book)
        assert book in collector.favorites, 'Книга не добавилась в favorites - необходимо для продолжения теста'

        assert book in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_genre_add_and_get_book(self):
        collector = BooksCollector()
        book = 'Дневник кота-убийцы'

        collector.add_new_book(book)
        assert book in collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'

        collector.set_book_genre(book, 'Комедии')
        assert collector.books_genre[book] in collector.genre , 'Книге в books_genre не добавился genre - необходимо для продолжения теста'
        
        assert collector.get_book_genre(book) == collector.books_genre[book]

    def test_get_books_for_children_rait_book(self):
        collector = BooksCollector()
        book = 'Бойцовский клуб'

        collector.add_new_book(book)
        assert book in collector.books_genre, 'Книга не добавилась в books_genre - необходимо для продолжения теста'

        collector.set_book_genre(book, 'Детективы')
        assert collector.books_genre[book] in collector.genre , 'Книге в books_genre не добавился genre - необходимо для продолжения теста'
        
        assert book not in collector.get_books_for_children()