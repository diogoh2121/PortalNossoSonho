from flask import Flask, render_template

app = Flask(__name__, template_folder= "templates_folder")

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
