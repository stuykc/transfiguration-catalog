from time import time, clock
from credentials import email, password
from constants import BOOKS_OFFSET, BIG_BOOKS_OFFSET
import gspread

class BookLists:
    def __init__(self):
        global books
        global big_books
        global books_values
        global big_books_values
        global updated_book_time
        global updated_big_book_time
        books = None
        books_values = None
        big_books = None
        big_books_values = None
        updated_book_time = "fake"
        updated_big_book_time = "fake"
        self.update()

    def login(self):
        gc = gspread.login(email, password)
        spreadsheet = gc.open_by_key('1UCIE9Iy9xOjLQXSGON_1R40QldjjtRTsE5vGotZ0_vw')
        return spreadsheet

    def update(self):
        start = clock()
        spreadsheet = self.login()
        global books
        global big_books
        books = spreadsheet.worksheet("Book List")
        big_books = spreadsheet.worksheet("Big Book List")

        global books_values
        global big_books_values
        global updated_book_time
        global updated_big_book_time
        if books.updated != updated_book_time:
            books_values = books.get_all_values()[BOOKS_OFFSET:]
            updated_book_time = books.updated
        if big_books.updated != updated_big_book_time:
            big_books_values = big_books.get_all_values()[BIG_BOOKS_OFFSET:]
            updated_big_book_time = books.updated
        print "Initialized Book Lists in " + str(clock() - start) + " seconds."

    def get_books(self):
        return books

    def get_books_values(self):
        return books_values

    def get_books_barcodes(self):
        barcodes = []
        for row in books_values:
            barcodes.append(row[0])
        return barcodes

    def get_books_titles(self):
        titles = []
        for row in books_values:
            titles.append(row[1])
        return titles

    def get_books_stickers(self):
        stickers = []
        for row in books_values:
            stickers.append(row[4])
        return stickers

    def get_book_info(self, book_row):
        return books_values[book_row]

    def get_big_books(self):
        return big_books

    def get_big_books_values(self):
        return big_books_values

    def get_big_books_barcodes(self):
        barcodes = []
        for row in big_books_values:
            barcodes.append(row[0])
        return barcodes

    def get_big_books_titles(self):
        titles = []
        for row in big_books_values:
            titles.append(row[1])
        return titles

    def get_big_books_stickers(self):
        stickers = []
        for row in big_books_values:
            stickers.append(row[4])
        return stickers

    def get_big_book_info(self, book_row):
        return big_books_values[book_row]
