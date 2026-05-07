from flask import Flask, render_template, abort

from app.lib import biblioteca_header as header
from app.lib.biblioteca_tari import TARI, BIBLIOTECI



print('Proiect SCC - Tari')
app = Flask(__name__)


'''NU SE MAI MODIIFICA NIMIC '''


@app.route("/", methods=['GET'])
def pagina_home():
    return render_template('home.html', tari=TARI)


@app.route("/<tara>", methods=['GET'])
def pagina_tara(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    descriere = bib.descriere_tara()
    return render_template('tara.html', descriere=descriere, tara=tara, tara_nume=TARI[tara]['nume'])


@app.route("/<tara>/capitala", methods=['GET'])
def pagina_capitala(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    return render_template('pagina.html',
                         titlu='Capitala',
                         header=header.header_capitala(),
                         continut=bib.descriere_capitala(),
                         tara_url=f'/{tara}')


@app.route("/<tara>/populatie", methods=['GET'])
def pagina_populatie(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    return render_template('pagina.html',
                         titlu='Populație',
                         header=header.header_populatie(),
                         continut=bib.descriere_populatie(),
                         tara_url=f'/{tara}')


@app.route("/<tara>/steag", methods=['GET'])
def pagina_steag(tara):
    if tara not in TARI:
        abort(404)
    bib = BIBLIOTECI[tara]
    return render_template('steag.html',
                         header=header.header_steag(),
                         continut=bib.descriere_steag(),
                         tara_url=f'/{tara}')


if __name__ == '__main__':
    app.run(debug=True)
