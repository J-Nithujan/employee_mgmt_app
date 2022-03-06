# Pré-TPI

---

## 1. Tâches globales

- [x] clarification CdC
- [ ] modélisation bdd
  - [x] script création
  - [ ] ajouter DROP

- [x] choix langages (et logiciels) => python + flask + flask-sqlalchemy + 
- [x] choix implémentation c# et /ou web+PHP ou python => python + web
- [ ] maquettes
- [x] use cases
- [ ] ~~TDD quand c'est possible (?)~~
- [ ] Implémentation du programme
- [ ] Documentation

### TO DO  (actuel):

- Emails: librairie ou service intégré à python
- librairie flask-login à checker
- Laisser le département IT entrer les mots de passe dans la base de données ou valeur par défaut

## 2. Choix

- Logiciels et langage: Python, PyCharm
- Techno BDD: MySQL

### 	librairies python:

- Flask: 
  - plus rapide à apprendre et mettre en place que Django
  - met à disposition le minimum => possible de personnaliser comme on veut
- Flask-SQLAlchemy: 
  - fork de SQLAlchemy destiné à Flask
  - supported dbs: SQLite, Postgresql, MySQL, Oracle, MS-SQL, Firebird, Sybase and others
- fpdf2: 
  - fork de fpdf1 () qui est lui-même un portage de FPDF (PHP)
  - simple et versatile (?) et màj régulière
  - alternative rejetée: ReportLab, freemium
- planification d'events ?

### Conception

Le programme sera destiné à une entreprise informatique ()

## 4. Versions:

- Python: 3.9.10, non compatible si OS <= Windows 7
- Import:
  - Flask:
  - Flask-SQLAlchemy:
  - fpdf2:
  - planif ?

## n. Réflexions:

- ~~appli en c# pour les 2 côtés (RH et employés)~~

- ~~appli RH et page web pour employés ==> code de test en moins car web ?~~

  ==> Le tout en python
  
- planification pour les fiches de salaires:

  - https://www.geeksforgeeks.org/python-schedule-library/
  
- extensions possible

  - page de contact (support, entreprise, etc)
  - backup de la base de données
  - crypté les mots de passe