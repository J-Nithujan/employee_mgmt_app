# Concevez un site avec Flask

[Lien du cours](https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask)

## Installez Flask

voir screenshots



## Ajouter une db

> pip install flask_sqlalchemy

Pour initialiser la commande change:

> set FLASK_APP=run.py
>
> flask init.db

ORM = Object-Relational Mapping

​	EX: SQLAlchemy

table.query.get(1) ==> renvoie l'élément dont la clé primaire est égale à 1



## Afficher le contenu d'un template

Flask utilise un modèle MVT

Vue = toutes fonctions décorée par @app.route



## Découper votre projet en template

Flask utilise le moteur de template Jinja2

- {{ }}: pour afficher qqch
- {% %}: pour du code Python
- {# #}: pour des commentaires

Flask permet de créer un fichier de base qui contient tous les éléments qui se répètent sur plusieurs pages

Il est possible d'imbriquer des templates afin d'éviter de répéter du code :

> { % include 'seconde_template.html' % }



## Créez une page de résultat grâce aux URL dynamiques

GET - request.args.get(<key>)

POST - request.form.get(<key>) (???)

fichier 'utils.py' pour les objets pas directement liés à Flask

Il est possible d'accéder aux variables dans l'URL quand une architecture REST est utilisée: 

```python
@app.route('/contents/<content_id>/')
def content(content_id):
    return content_id
```



## Tests fonctionnels

```powershell
pip install pytest
...
pip install Flask-Testing
...
pip install selenium

```

Pour Selenium, il faut installer un [driver](https://selenium-python.readthedocs.io/installation.html) car il permet de simuler un utilisateur qui navigue sur le site

Créer un fichier config.py dans le dossier 'test'

Port à utiliser doit être différent de celui du serveur web !

Les fichers de tests doivent avoir un nom qui finissent avec "test" pour être interprété par pytest.



