import requests
from pages.all_books_page import AllBooksPage

page_content=requests.get("http://books.toscrape.com").content
page=AllBooksPage(page_content)
list_books=page.books
for book in list_books:
    print(book)
