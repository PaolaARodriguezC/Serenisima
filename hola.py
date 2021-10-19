from flask import Flask
from flask import render_template as render

listado_usuario=["empleado1","empleado2","empleado3","empleado3"]
listado_roles=["Superadministrador","administrador","empleado"]
app = Flask(__name__)
@app.route('/')
def login():
    return render('login.html', methods=["GET", "POST"])

@app.route('/listado/<id_rol>', methods=["GET"])
def listado(id_rol):
    if id_rol == "empleado":
        return "no tiene acceso"
    else:
        return render('listado.html')

@app.route('/visualizar/<id_usuario>' , methods=["GET", "POST"])
def visualizar(id_usuario):
    return render('visualizar.html')

@app.route('/editar', methods=["GET", "POST"])
def editar():
    return render('editar.html')

@app.route('/main')
def estilo():
    return render('css/main.css')

if __name__=="__main__":
    app.run(debug=True)