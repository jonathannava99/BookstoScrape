import requests
from bs4 import BeautifulSoup


def categories_function():
    url = "https://books.toscrape.com/index.html"
    # nous renvoie 200 si la requete fonctionne
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

    # dictionnaire qui combine la catégorie
    # avec son lien
    categories = {}
    categories_bis2 = ""

    categories_bis = soup.find_all("ul", class_="nav")[0]
    soup2 = BeautifulSoup(str(categories_bis), "html.parser")
    categories_bis = soup2.find_all("a")

    # transformer la list avec toutes les balises a en string
    for category in categories_bis:
        categories_bis2 += str(category)

    # transformer en onbjet soup
    soup3 = BeautifulSoup(categories_bis2, "html.parser")

    for category, link in zip(categories_bis, soup3.find_all('a')):
        # on attribue à au dictionnaire sa clé ici la categorie
        # et sa valeur ici son lien
        # strip sert a éliminer les espaces inutiles
        categories[category.string.strip()] = "http://books.toscrape.com/"+link.get('href')

    return categories
