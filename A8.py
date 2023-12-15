#Jonathan Rozeff
#Assignment Number: 8
#Date: 4/23/18
#Section: 2-3:30pm


class Book:
    def __init__(self, ISBN, title, author, publisher, price):
        self.__ISBN = ISBN
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__price = price

    def set_ISBN(self, ISBN, new_ISBN):
        self.__ISBN

    def set_title(self, title):
        self.__title

    def set_author(self, author):
        self.__author

    def set_publisher(self, publisher):
        self.__publisher

    def set_price(self, price):
        self.__price = price

    def get_ISBN(self):
        return self.__ISBN

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def get_price(self):
        return self.__price

    def __str__(self):
        return 'ISBN: ' + str(self.__ISBN) + \
               '\nTitle: ' + str(self.__title) + \
               '\nAuthor: ' + str(self.__author) + \
               '\nPublisher: ' + str(self.__publisher) + \
               '\nPrice: $' + str(self.__price) + '\n'
            
               

class AudioBook(Book):
    def __init__(self, ISBN, title, author, publisher, price, narrator):

        Book.__init__(self, ISBN, title, author, publisher, price)
        self.__narrator = narrator
        self.__ISBN = ISBN
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__price = price
        
    def set_narrator(self):
        self.__narrator 

    def get_narrator(self, narrator):
        return self.__narrator

    def __str__(self):
        return 'ISBN: ' + str(self.__ISBN) + \
               '\nTitle: ' + str(self.__title) + \
               '\nAuthor: ' + str(self.__author) + \
               '\nPublisher: ' + str(self.__publisher) + \
               '\nPrice: $' + str(self.__price) + \
               '\nNarrator: ' + str(self.__narrator) + '\n'
            
