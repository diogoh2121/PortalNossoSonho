from flask import Flask, render_template, url_for, session, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conectar o Banco de Dados
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0252'
app.config['MYSQL_HOST'] = '3306'
app.config['MYSQL_DB'] = 'pi1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE Example (id INTEGER, nome VARCHAR(20))''')
    return "Done!"

# Criar a primeira página do site (toda página tem um route, uma função e um template)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/materias")
def materias():
    return render_template("materias.html")

@app.route("/hrcircular")
def hrcircular():
    return render_template("hrcircular.html")

@app.route("/teluteis")
def teluteis():
    return render_template("teluteis.html")

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
