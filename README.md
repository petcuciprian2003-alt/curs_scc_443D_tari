# Proiect SCC - Țări

## Dezvoltator
- **Nume:** Petcu Ștefan-Ciprian
- **Grupa:** 443D
- **Țară alocată:** Serbia

## Cuprins
- [Descriere generală](#descriere-generală)
- [Funcționalitate implementată](#funcționalitate-implementată)
- [Stadiu dezvoltare](#stadiu-dezvoltare)
- [Testare manuală în browser](#testare-manuală-în-browser)
- [Testare automată cu pytest](#testare-automată-cu-pytest)
- [Testare cu Docker](#testare-cu-docker)
- [DevOps CI - Jenkins](#devops-ci---jenkins)
- [Concluzii](#concluzii)

## Descriere generală

Acest proiect se înscrie în tema comună a grupei 443D, „Țări”, scopul fiind dezvoltarea și integrarea unui set de funcționalități dedicate țării **Serbia**.

Aplicația este implementată utilizând framework-ul web Flask, fiind proiectată pentru a furniza date esențiale despre țara accesată. Soluția a fost supusă testării automate (Pytest), containerizată prin Docker și orchestrată într-un pipeline de integrare continuă (CI/CD) folosind Jenkins.

## Funcționalitate implementată

În acest branch am adăugat și personalizat:

- Fișierul `app/lib/biblioteca_serbia.py` cu funcțiile:
  - `descriere_tara()` – oferă o descriere generală a țării.
  - `descriere_capitala()` – returnează capitala Serbiei (Belgrad).
  - `descriere_limbi()` – afișează limba oficială (sârba).
  - `descriere_populatie()` – afișează numărul de locuitori.
  - `descriere_steag()` – returnează codul HTML pentru afișarea steagului Serbiei.

- Integrarea în fișierul `app/lib/biblioteca_tari.py`:
  - Declararea țării în dicționarul global `TARI`.
  - Maparea modulului aferent în dicționarul `BIBLIOTECI`.

- Fișierul `app/tests/test_lib_serbia.py` cu testele automate.

- `Dockerfile` pentru containerizare.

- `Jenkinsfile` pentru pipeline-ul CI/CD.

## Stadiu dezvoltare

- Funcționalitate complet implementată.
- Cod adăugat în branch-ul `dev_petcu_stefan`.
- Dockerfile și Jenkinsfile funcționale.
- Testare locală, automată și containerizată realizată cu succes.

## Testare manuală în browser

**Rulare locală:**

```bash
cd curs_scc_443D_tari
. ./activeaza_venv
./ruleaza_aplicatia
Aplicația poate fi accesată la: http://127.0.0.1:5011/serbia

![](screenshots/Screenshot from 2026-05-10 15-51-26.png)

Rute disponibile:

    /serbia - pagina principală

    /serbia/capitala - capitala

    /serbia/populatie - populația

    /serbia/steag - steagul

![](screenshots/Screenshot from 2026-05-10 14-40-38.png)
Testare automată cu pytest
bash

. ./activeaza_venv
pytest app/tests/test_lib_serbia.py -v

Rezultat: 4/4 teste trecute cu succes ✅

![](screenshots/Screenshot from 2026-05-10 14-12-21.png)
Testare cu Docker
bash

docker build -t tari:v01 .

![](screenshots/Screenshot from 2026-05-10 15-35-45.png)
bash

docker run -d --name tari_serbia -p 8020:5000 tari:v01

![](screenshots/Screenshot from 2026-05-10 15-37-46.png)

Accesare: http://localhost:8020/serbia

![](screenshots/Screenshot from 2026-05-10 15-50-31.png)
DevOps CI - Jenkins

Pipeline-ul Jenkins include:

    Setup - instalare dependințe

    Test - rulare pytest (4/4 PASSED)

    Build Docker - construire imagine

![](screenshots/Screenshot from 2026-05-10 18-54-56.png)
Concluzii

Proiectul a atins cu succes obiectivele propuse:

    Dezvoltare modulară cu Flask

    Testare automată cu pytest

    Containerizare cu Docker

    Integrare continuă cu Jenkins

Bibliografie

https://github.com/crchende/sysinfo
https://github.com/raduionutgavrila/curs_scc_443D_tari
