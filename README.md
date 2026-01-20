# Esame - 20/01/2026

---
> **❗ ATTENZIONE:** 
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale** 
> (https://github.com/my-github-username/Esame_20-01-2026) e non quello principale.

---
**DURATA DELLA PROVA**: 2 h

---

Si consideri il database `iTunes.sql`, tratto dalla piattaforma iTunes di Apple. Il database è stato estratto a partire 
dai dati di un utente reale ed ha la seguente struttura.
![database.png](img/database.png)

-----
## LINK ACCESSIBILI DURANTE L'ESAME
- `Python`: https://docs.python.org/
- `PyCharm`: https://www.jetbrains.com/help/pycharm/getting-started.html
- `DBeaver`: https://dbeaver.com/docs/dbeaver/
- `Flet`: https://docs.flet.dev/api-reference/
- `mysql-connector-python`: https://pypi.org/project/mysql-connector-python/ & https://dev.mysql.com/doc/connector-python/en/
- `NetworkX`: https://networkx.org/documentation/stable/reference/index.html
-----

## Materiale Fornito
Il repository Esame_20-01-2026 è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario 
per svolgere l'esame:

```code
Esame_20-01-2026/
├── database/
│   ├── __init__.py
|   ├── connector.cnf 
|   ├── DB_connect.py 
│   └── dao.py (DA MODIFICARE) 
│
├── model/ (AGGIUNGERE ULTERIORI CLASSI SE NECESSARIE) 
│   ├── __init__.py
│   └── model.py (DA MODIFICARE) 
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py (DA MODIFICARE)
│   └── view.py (DA MODIFICARE)
│
├── requirements.txt
├── plot.png
├── iTunes.sql (DA IMPORTARE)
└── main.py (DA ESEGUIRE)
 ```
