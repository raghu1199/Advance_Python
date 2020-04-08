from bs4 import BeautifulSoup
from locators.all_books_page import AllBookPageLocators
from parsers.book_parser import BookParser

class AllBooksPage:
    def __init__(self,page_content):
        self.soup=BeautifulSoup(page_content,"html.parser")

    @property
    def books(self):
        locator=AllBookPageLocators.Books
        list_of_books=self.soup.select(locator)
        return [BookParser(item) for item in list_of_books]
