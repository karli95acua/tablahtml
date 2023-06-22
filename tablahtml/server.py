#ACTIVIDAD TABLA DE HTML
from flask import Flask, render_template
app = Flask(__name__)

#Personajes de serie
usuarios = [
    {'Nombre': 'Bojack', 'Apellido': 'Horseman'},
    {'Nombre': 'Todd', 'Apellido': 'Chávez'},
    {'Nombre': 'Princess', 'Apellido': 'Carolyn'},
    {'Nombre': 'Diane', 'Apellido': 'Nguyen'},
    {'Nombre': 'Mr.', 'Apellido': 'Peanutbutter'},
    {'Nombre': 'Vincent', 'Apellido': 'Adultman'}, 
    {'Nombre': 'Sarah', 'Apellido': 'Lynn'}
]

@app.route("/", methods=['GET'])
def tabla_html():
    return render_template("index.html", usuarios=usuarios)


if __name__ == "__main__":
    app.run(debug=True, port=5005)
