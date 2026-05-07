# PROIECT SCC - TEMPLATE WEB PENTRU PROIECT DE GRUPA

Acest branch este template-ul de proiect pentru grupa. Scopul este ca fiecare student sa foloseasca aceeasi structura si sa modifice doar ce este necesar pentru tara proprie.

## Ce se modifica

In acest proiect, trebuie modificat:

- `app/lib/biblioteca_tari.py`

Trebuie adaugat importul bibliotecii tarii la inceputul fisierului, dupa modelul prezentat.

Apoi trebuie adaugata:

1. o pereche in `TARI` pentru tara ta
2. o intrare in `BIBLIOTECI` care sa includa fișierul `biblioteca_<tara_mea>.py`

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

- Creeaza un fisier nou `app/lib/biblioteca_<tara_mea>.py` (de exemplu `biblioteca_romania.py`) similar cu `biblioteca_belgia.py`.
- In fisierul personal, adauga functiile tarii tale, de exemplu:
  - `descriere_tara()`
  - `descriere_capitala()`
  - `descriere_populatie()`
  - `descriere_steag()`

## Ce se adauga in `static/`

- Adauga poza cu steagul tarii tale in format `png` in directorul `static/`.
- Adauga locatia pozei in `biblioteca_<tara_mea>.py`, sub formatul '/static/<steag_tara>.png'.

## Ce NU se modifica

- `tari.py` - NU SE MODIFICA
- `app/lib/biblioteca_header.py` - NU SE MODIFICA
- `templates/base.html` - NU SE MODIFICA
- `templates/pagina.html` - NU SE MODIFICA
- `templates/steag.html` - NU SE MODIFICA
- `templates/tara.html` - NU SE MODIFICA (este template generic pentru pagina de tara)


## Structura de baza

`app/lib/`
- `biblioteca_tari.py` - singurul fisier de configurare personalizata pentru tara ta
- `biblioteca_<tara_mea>.py` - fisierul tau personal cu functiile pentru tara aleasa
- `biblioteca_header.py` - header comun, nu se modifica

`static/`
- aici se pune poza steagului in format `png`

`templates/`
- `base.html` - sablonul principal
- `home.html` - pagina de start cu lista de tari
- `tara.html` - template generic pentru pagina fiecarei tari
- `pagina.html` - pagina generica folosita pentru capitala/populatie
- `steag.html` - pagina generica pentru steag

## Scripturi de activare si rulare

### `activeaza_venv`

Acest script activeaza mediul virtual Python din `.venv`.

- Incarca ` . .venv/bin/activate`
- Daca activarea esueaza, incearca varianta `activeaza_venv_jenkins`
- Este folosit pentru a asigura ca python si dependintele sunt executate in mediul corect

### `ruleaza_aplicatia`

Acest script porneste aplicatia Flask local.

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

1. `git clone ...`
2. `git checkout dev-template`
3. `git checkout -b dev-nume-prenume`
4. modifica doar `app/lib/biblioteca_tari.py`
5. adauga `app/lib/biblioteca_<tara_mea>.py`
6. adauga steagul in `static/` si referinteaza-l in biblioteca personala
7. ruleaza cu `./activeaza_venv` si `./ruleaza_aplicatia`

## Observatie finala

Scripturile din aceasta aplicatie sunt introduse dupa modelul aplicatiei `chrchende/sysinfo:simplu_main`.
