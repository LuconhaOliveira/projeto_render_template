from flask import Flask, render_template
import random

app = Flask(__name__)

#arrays
cores = ["red","blue","green","#BABACA","#666666"]
imagens = ["img1.jpg","img2.jpg","img3.jpg","img4.jpg","img5.jpg"]
curiosidades = ["não existe falantes de latim vivos atualmente",
                "latim é usado até hoje nas ciências",
                "lorem ipsum é um texto em latim",
                "lorem ipsum não tem significado completo pois o texto foi alterado",
                "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias iusto pariatur sed, quos voluptatem maiores eaque facere deleniti voluptatum aliquid fugiat commodi alias cum, culpa animi explicabo tempore unde consectetur."]

#ROTAS
@app.route("/")
def pagina_principal():
    cor_fundo = random.choice(cores)
    imagem = random.choice(imagens)
    texto_curioso = random.choice(curiosidades)
    return render_template("index.html", cor_fundo=cor_fundo, imagem=imagem, texto_curioso=texto_curioso)

#@app.route("/sobre")
# def pagina_sobre():
#     cor_fundo = random.choice(cores)
#     return render_template("sobre.html", cor_fundo=cor_fundo)

app.run(debug=True)

