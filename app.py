# coding: utf-8

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask("projeto")
app.secret_key = "amksdkasd"

@app.route("/")
def inicio():

    produtos = [
        {"nome": "Playstation", "preco": 1000.50},
        {"nome": "Xbox", "preco": 1020.0},
    ]

    return render_template("alo.html", produtos = produtos), 200

# Nova rota teste

@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):

    return f"nova rota teste<br>Variável: {variavel}", 200

# Rota comentário
@app.route("/form")
def form():
    return render_template("form.html"), 200

# Rota tratamento formulário
@app.route("/form_recebe", methods = ["GET", "POST"])
def form_recebe():
    if request.method == "POST":
        nome = request.form["nome"]
    
    return "Nome: {}".format(nome), 200

# Rota para login
@app.route("/login")
def login():
    return render_template("login.html"), 200 

# Rota para validar o formulário
@app.route("/login_validar", methods = ["POST"])
def login_validar():
    if request.form["usuario"] == "nicholas" and request.form["senha"] == "12345":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))
    else:
        return "Usuário ou senha inválidos, digite novamente.", 200

# Rota para a área restrita
@app.route("/restrito")
def acesso_restrito():
    if session["codigo"] == 1:
        return "Bem-vindo à área restrita!", 200
    else:
        return "Acesso inválido!"

app.run()