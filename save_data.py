import csv
from make_directory import make_directory

write = []


def save(infos,file,category,type):
    en_tete = ['product_page_url', 'universal_product_code_(upc)', 'title',
               'price_including_tax', 'price_excluding_tax', 'number_available',
               'product_description', 'category', 'review_rating', 'image_url']

    path2 = make_directory(category, type)

    with open(path2+file.replace(" ","").replace("/","")+'.csv', 'w', newline='') as csv_file:
        # delimiter nous permet de séparer titre et description en deux colonnes
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(en_tete)

        for info in infos:
            writer.writerow(
                [info['product_page_url'], info['universal_product_code_(upc)'], info['title'],
                 info['price_including_tax'], info['price_excluding_tax'], info['number_available'],
                 info['product_description'], info['category'], info['review_rating'], info['image_url']]
            )


