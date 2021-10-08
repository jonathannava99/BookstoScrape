from get_books_links import books_links
from categories import categories_function
from pages import pages_check
from get_book import get_book_function
from save_data import save
from get_image import save_image

exit = "y"

while exit != "n":
    books = []
    categories = categories_function()

    mode = input("Choisissez le mode automatique 'A' pour avoir toutes les catégories.\n"
                 "Choisissez le mode manuel pour 'm' avoir une categorie précise. (A/m)")

    if mode == "A":
        for category in categories.keys():
            if category == "Books":
                continue
            pages = pages_check(categories[category])

            for page in pages:
                book = books_links(page)
                for book_link in book:
                    get_book = get_book_function(book_link)
                    books.append(get_book)

            file = category.lower()
            save(books, file, category, "csv")
            save_image(books, category, "image")
            del books[:]

        exit = input("Voulez vous continuer:(Y/n)")

    else:
        condition = True

        while condition:
            category = input("Category:")
            try:
                pages = pages_check(categories[category])
                condition = False
            except KeyError as err:
                print("Cette catégorie n'existe pas.\n Renseignez vous sur le site de "
                      "https://books.toscrape.com/index.html pour voir les bonnes catégories.")

        for page in pages:
            book = books_links(page)
            for book_link in book:
                get_book = get_book_function(book_link)
                books.append(get_book)

        file = input("Nom du fichier csv:")
        save(books, file, category, "csv")
        save_image(books, category, "image")

        exit = input("Voulez vous continuer:(Y/n)")
