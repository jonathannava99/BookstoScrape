import requests
from make_directory import make_directory


def save_image(infos,category,type):
    path2  = make_directory(category,type)

    for info in infos:
        response = requests.get(info['image_url'])
        file = open(path2+info['title'].replace(" ","").replace("/","")+".jpg", "wb")
        file.write(response.content)
        file.close()