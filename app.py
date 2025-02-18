from flask import Flask, render_template, request, redirect
import random
from data.listas_configuracao import *
import mysql.connection

app = Flask(__name__)

#ROTAS
@app.route("/", methods=["GET"])
def pagina_principal():
    cor_fundo = random.choice(cores)
    imagem = random.choice(imagens)
    texto_curioso = random.choice(curiosidades)
    return render_template("index.html", cor_fundo=cor_fundo, imagem=imagem, texto_curioso=texto_curioso)

@app.route("/frases", methods=["GET"])
def pagina_frases():
    return render_template("cadastro-frases.html", frases=curiosidades)

@app.route("/cores", methods=["GET"])
def pagina_cores():
    return render_template("cadastro-cores.html", cores=cores)

@app.route("/post/cadastrarcor", methods=["POST"])
def post_cadastrarcor():
    cor_cadastrada = request.form.get("cor")
    cores.append(cor_cadastrada)
    return redirect("/cores")

@app.route("/post/cadastrarfrase", methods=["POST"])
def post_cadastrarfrase():
    frase_cadastrada = request.form.get("frase")
    curiosidades.append(frase_cadastrada)
    return redirect("/frases")

@app.route("/cores/delete/<indice_cor>")
def delete_cores(indice_cor):
    indice_cor=int(indice_cor)
    cores.pop(indice_cor)
    return redirect("/cores")

#@app.route("/sobre", methods=["GET"])
# def pagina_sobre():
#     cor_fundo = random.choice(cores)
#     return render_template("sobre.html", cor_fundo=cor_fundo)

app.run(debug=True)

