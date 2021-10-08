<h1>BookstoScrape</h1>
<p><h3>Pour créer l'environnment virtuel il faut utiliser</h3>
les commandes suivantes:</p>
<ul>
  <li>python -m venv nomEnvironnement</li>
  <li>source env/bin/activate</li>
</ul>
<p>Vérifier les packages:</p>
<ul>
  <li>pip freeze</li>
</ul>
<p>Vérifier le fichier requirements.txt et installer les packages</p>
</p>
<br>

<p><h3>Description de l'application</h3>
BookstoScrpe est un programme qui permet de récolter les informations des livres
du site <a href="https://books.toscrape.com/index.html"><br>https://books.toscrape.com/index.html</a>
 comme le:<br><br>
<ul>
  <li>product_page_url</li>
  <li>universal_ product_code (upc)</li>
  <li>title</li>
  <li>price_including_tax</li>
  <li>price_excluding_tax</li>
  <li>number_available</li>
  <li>product_description</li>
  <li>category</li>
  <li>review_rating</li>
  <li>image_url</li>
</ul>
<p>Pour chaque catégorie nous avons toutes les informations des livres ainsi que les images téléchargées pour chaque livre.</p>
</p><br>



<p><h3>Utilisation de l'application:</h3>
<p>Pour démarrer notre fichier principal tapez la commande:<p>
<ul>
  <li>python main.py</Li><br>
  <li>Un message comme ceci va apparaître: <br>"Choisissez le mode automatique 'A' pour avoir toutes les catégories.<br>
Choisissez le mode manuel pour 'm' avoir une categorie précise. (A/m)"<br></li><br>
 <li>Si vous choissisez "m" le programme vous demande le nom d'une catégorie. Soyez précis lorsque vous la mettez.<br>
 Le programme étant sensible à la case.</li><br>
 <li>Attendez quelques instants et mettez le nom du fichier. Pas besoin de mettre csv à la fin le programme s'en charge pour vous.</li><br>
 <li> Si le dossier n'est pas déjà crée un répertoire Category se crée avec à l'intérieur un dossier csv avec le nom du fichier csv correspondant
 et un dossier image avec toutes les images téléchargées.</li><br>
 <li>Le programme vous demandera alors si vous voulez continuer ou pas: "Voulez vous continuer:(Y/n)"<br> Si vous continuez la boucle repart</li><br>
 <li>Si vous choissisez le mode automatique le processus est le même mais par contre vous pouvez pas choisir ni la catégorie ni le nom du fichier.</li><br>
</ul>
</p>
