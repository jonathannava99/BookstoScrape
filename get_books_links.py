import requests

from bs4 import BeautifulSoup


def books_links(url):
    url = url
    # nous renvoie 200 si la requete fonctionne
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

    books = []
    books_bis2 = ""
    books_list = []
    books_bis = soup.find_all("div", class_="image_container")
    # transformer le tableau de div en string
    for book in books_bis:
        books_bis2 += str(book)

    # transformer le string de div en objet soup
    soup2 = BeautifulSoup(books_bis2, "html.parser")
    books_bis = soup2.find_all("a")

    for link in books_bis:
        # on attribue à un dictionnaire sa clé ici la categorie
        # et sa valeur ici son lien
        # strip sert a éliminer les espaces inutiles
        books_list.append(link.get('href').split("../../../"))

    for i in range(0, len(books_list), 1):
        if len(books_list[0]) == 1:
            book = (books_list[i][0]).split("../../")
            books.append("http://books.toscrape.com/catalogue/" + book[1])
        else:
            books.append("http://books.toscrape.com/catalogue/" + books_list[i][1])

    return books
