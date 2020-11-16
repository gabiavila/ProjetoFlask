from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost/ac5'
db=SQLAlchemy(app)


class clube(db.Model):
    _tablename_ = 'tbclube'
    idclube = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dia=db.Column(db.String(10)) 
    horario = db.Column(db.String(225))
    time1clube = db.Column(db.String(25))
    time2clube = db.Column(db.String(25))
    def _init_(self, nome,email ,senha, time):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.time = time


db.create_all()


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/partidas")   
def partidas():
    return render_template("partidas.html")

@app.route("/times")
def times():
    return render_template("times.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/historia")
def cadastro():
    return render_template("historia.html")


@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome=(request.form.get("nome"))
        email= (request.form.get("email"))
        senha = (request.form.get("senha"))
        time= (request.form.get("time"))
        if email:
             a = clube(nome,senha,time)
             db.session.add(a)
             db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


#"http://127.0.0.1:5000/home" #enderco URL

#localhost:5000/home  # outro caminho q da pra por de URL