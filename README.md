# PROIECT SCC - TEMPLATE WEB PENTRU PROIECT DE GRUPA

Acest branch este template-ul de proiect pentru grupa. Scopul este ca fiecare student sa foloseasca aceeasi structura a site-ului si sa modifice ce este necesar pentru tara proprie. 

## Ce se modifica

In acest proiect, trebuie modificat:

- `app/lib/biblioteca_belgia.py`
- `app/lib/biblioteca_tari.py`



Modifica fisierul `app/lib/biblioteca_belgia.py` cu numele tarii alese `app/lib/biblioteca_<tara_mea>.py` (de exemplu `biblioteca_romania.py`).
  
- In `biblioteca_<tara_mea>.py`, adauga continut corespuzator tarii alease in functiile:
  - `descriere_tara()`
  - `descriere_limbi()`
  - `descriere_populatie()`
  - `descriere_capitala()`
  - `descriere_steag()`
    
Trebuie adaugat importul bibliotecii tarii la inceputul fisierului 'biblioteca_tari.py', dupa modelul prezentat.

Apoi trebuie adaugata:

1. o pereche in `TARI` pentru numele tarii
2. o intrare in `BIBLIOTECI` pentru biblioteca tarii alese 

Obs: Eliminati intrarile cu Belgia; sunt doar de model !

### Exemplu de actualizare in `app/lib/biblioteca_tari.py`

```python
from app.lib import biblioteca_tara_mea as prescurtare_biblioteca_tara_mea

TARI = {
    'tara_mea': {
        'nume': 'Numele complet al tarii mele',
    },
}

BIBLIOTECI = {
    'tara_mea': prescurtare_biblioteca_tara_mea,
}
```


## Ce se adauga in `static/`

- Adauga poza cu steagul tarii tale in format `png` in directorul `static/` ( sterge apoi poza steag_belgia.png).
- Adauga locatia pozei in functia desriere_steag() din  `biblioteca_<tara_mea>.py`, sub formatul '/static/<steag_tara>.png'.

## Ce NU se modifica

- `tari.py` - NU SE MODIFICA
- `app/lib/biblioteca_header.py` - NU SE MODIFICA
- `templates/base.html` - NU SE MODIFICA
- `templates/pagina.html` - NU SE MODIFICA
- `templates/steag.html` - NU SE MODIFICA
- `templates/tara.html` - NU SE MODIFICA (este template generic pentru pagina de tara)


## Structura de baza

`app/lib/`
- `biblioteca_tari.py` - fisier in care vor fi agregate numele si bibliotecile de la toate tarile din proiect ( agregarea se va face la final, cand se va face Pull Request in branch-ul main)
- `biblioteca_<tara_mea>.py` - fisierul individual cu functiile pentru tara aleasa
- `biblioteca_header.py` - header comun, nu se modifica

`static/`
- aici se pune poza steagului in format `png`

`templates/`
- `base.html` - scheletul proiectului - contine structura html + css statica
- `home.html` - pagina de pornire unde sunt listate tarile
- `tara.html` - template generic pentru pagina fiecarei tari, unde este afisat rezultatul functiei descriere_tara()
- `pagina.html` - pagina folosita pentru a afisa rezultatul funtiilor descriere_capitala() / descriere_populatie() / descriere_limbi()
- `steag.html` - pagina folosita pentru a afisa rezultatul functiei descriere_steag()

## Scripturi de activare si rulare

### `activeaza_venv`

Acest script activeaza mediul virtual Python din `.venv`. Comanda:  `. ./activeaza_venv`

- Incarca ` . .venv/bin/activate`
- Daca activarea esueaza, incearca varianta `activeaza_venv_jenkins`
- Este folosit pentru a asigura ca python si dependintele sunt executate in mediul corect

### `ruleaza_aplicatia`

Acest script porneste aplicatia Flask local. Comanda: `./ruleaza_aplicatia`

- seteaza `FLASK_APP=tari`
- ruleaza `flask run -p 5011 --reload`
- `--reload` face serverul sa se reporneasca automat cand faci modificari in cod

### `dockerstart.sh`

Acest script face acelasi lucru, dar cu optiuni suplimentare:

- activeaza environment-ul virtual
- seteaza `FLASK_APP=tari`
- afiseaza directorul curent si continutul fisierelor
- porneste serverul Flask pe `0.0.0.0:5011` cu `--reload`

### Permisiuni de executie

Pentru a rula scripturile, trebuie sa le dai permisiuni de executie:

```bash
chmod 764 activeaza_venv ruleaza_aplicatia dockerstart.sh
```

## Pasi recomandati pentru proiect

1. `git clone https://github.com/raduionutgavrila/curs_scc_443D_tari.git` - pentru a copia local repository-ul
2. `git checkout dev-template` - pentru a selecta ramura de dezvolatare cu template-ul
3. `git checkout -b dev-nume-prenume` - pentru a crea o noua ramura de dezvoltare pornind de la template
4. modifica `app/lib/biblioteca_tari.py`
5. redenumeste `app/lib/biblioteca_belgia.py` in `app/lib/biblioteca_<tara_mea>.py` si modifica continutul functiilor
6. adauga poza cu steagul in `static/` si adauga link catre acesta in functia din 'biblioteca_<tara_mea>.py'
7. ruleaza cu `. ./activeaza_venv` si `./ruleaza_aplicatia`

# Ce mai trebuie adaugat

- Modificare fisier de test in 'app/tests' cu denumirea 'test_<tara_mea>.py'
- Creare Dockerfile
- Creare Jenkinsfile

## Observatie finala

Scripturile din aceasta aplicatie sunt introduse dupa modelul aplicatiei `chrchende/sysinfo:simplu_main`.


  
