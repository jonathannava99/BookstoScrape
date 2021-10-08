import os


def make_directory(category, type):
    parent_dir = os.getcwd()
    directory = "Categories" + "/" + category + "/" + type + "/"
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print('Dossier déjà crée')

    return path
