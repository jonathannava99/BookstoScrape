import requests


def pages_check(link):
    url = link
    # nous renvoie 200 si la requete fonctionne
    response = requests.get(url)
    pages = []
    books_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

    i = 2
    while True:

        if response.status_code == 200:
            pages.append(url)

            url = url.replace("index.html", ("page-" + str(i) + ".html"))
            url = url.replace("page-"+str(i-1)+".html","page-" +str(i) +".html")
            response = requests.get(url)
            i += 1

        else:
            break

    return pages
