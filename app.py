from flask import Flask, render_template, abort, request


from functions import checkmsx
app = Flask(__name__)

infoGames = checkmsx()	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")

@app.route('/listajuegos', methods=["POST"])
def listajuegos():
    datos=request.form
    juegos=datos["nombre"]
    lista=[]
    for info in infoGames:
        for info in info:
            if info.startswith(juegos) == info:
                lista.append(info.nombre)

    return render_template("listajuegos.html", infoGames=infoGames, juegos=juegos, lista=lista)

@app.route('/error')
def error():
    return abort(404)



app.run("0.0.0.0",5000,debug=True)
#port=os.environ["PORT"]
#app.run('0.0.0.0',int(port), debug=True)