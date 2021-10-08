import requests
from bs4 import BeautifulSoup

def get_book_function(url):
    url = url
    # nous renvoie 200 si la requete fonctionne
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

    # initialisation des variables
    infos = {"product_page_url":"","universal_product_code_(upc)":"",
             "title":"","price_including_tax":"","price_excluding_tax":"",
             "number_available":"","product_description":"","category":"",
             "review_rating":"","image_url":""
    }

    # scraing grâce à beautiful soup
    descriptions = soup.find_all("p")
    image = soup.find_all('img')
    soup2 = BeautifulSoup(str(image[0]), "html.parser")
    rating = soup.find_all("p",class_="star-rating")
    soup3 = BeautifulSoup(str(rating[0]), "html.parser")
    informations = soup.find_all("td")
    category = soup.find_all("a")[3].string
    image= soup2.img['src'].split("m")

    rating = (soup3.p['class'][1])

    if rating == "One":
        infos["review_rating"] = "1"

    elif rating ==  "Two":
        infos["review_rating"] = "2"

    elif rating == "Three":
        infos["review_rating"] = "3"

    elif rating == "Four":
        infos["review_rating"] = "4"

    elif rating == "Five":
        infos["review_rating"] = "5"

    else:
        infos["review_rating"] = "Pas d'informations disponibles"

    infos["product_page_url"] = url
    infos["universal_product_code_(upc)"] = informations[0].string
    infos["title"] = soup.find_all("h1")[0].string
    infos["price_including_tax"] = informations[3].string
    infos["price_excluding_tax"] = informations[2].string
    infos["number_available"] = informations[5].string
    infos["product_description"] = descriptions[3].string
    infos["category"] = category
    infos["image_url"] = "http://books.toscrape.com/"+"m"+image[1]

    return infos

