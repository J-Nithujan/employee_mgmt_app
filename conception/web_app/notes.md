# Notes de conception

## flask- / sqlalchemy:

- Possible d'exécuter des query de 2 manières différentes:
  1. db.Model.query() - retourne des objets ORM
  2. db.session.execute(query) - retourne des lignes sous forme de tuple
  
  ==> Le second sert lors de sélection de certaines colonnes précises