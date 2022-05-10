from flask import Flask, render_template, abort, redirect
import os

from functions import checkmsx
app = Flask(__name__)

games = checkmsx()	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def biblioteca():
    return render_template("juegos.html", games=games)

@app.route('/error')
def error():
    return abort(404)
















@app.route('/libro/<isbn>')
def libro(isbn):
    try:
        return render_template("libro.html",isbn=isbn,games=games)
    except:
        return abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    return render_template("categoria.html", categoria=categoria, games=games)

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")


app.run("0.0.0.0",5000,debug=True)
#port=os.environ["PORT"]
#app.run('0.0.0.0',int(port), debug=True)