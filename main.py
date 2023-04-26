from flask import Flask, render_template

app = Flask(__name__)

# Criar a primeira página do site (toda página tem um route, uma função e um template)
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
