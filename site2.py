from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.cadastro import CadastroForm
from app.login import LoginForm
from app.denuncia import DenunciaForm
from app.perfil import PerfilForm

#from bancodados import Usuario

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///meusite.db'
app.config['SECRET_KEY'] = 'SDFRGHTNJYMUK,IL.'
db = SQLAlchemy(app)



#temporario

class Usuario(db.Model):
	__tablename__="usuario"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(8), unique=True, nullable=False) 
	email = db.Column(db.String(200), unique=True, nullable=False)


	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		
	def __repr__(self):
		return "<Usuario %r>" % self.username

class Perfil(db.Model):
	__tablename___="perfil"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(80), unique=True, nullable=False)
	sobrenome = db.Column(db.String(80), unique=True, nullable=False)
	cpf = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)

	def __init__(self, nome, sobrenome, cpf, email):
		self.nome = nome
		self.sobrenome = sobrenome
		self.cpf = cpf
		self.email = email
		
	def __repr__(self):
		return "<Perfil %r>" % self.nome

class Login(db.Model):
	__tablename___="logins"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), unique=True, nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password
		
	def __repr__(self):
		return "<Login %r>" % self.username

class Denuncia(db.Model):
	__tablename__="denuncias"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(80), unique=False, nullable=False)
	sobrenome = db.Column(db.String(80), unique=False, nullable=False)
	cpf = db.Column(db.String(80), unique=True, nullable=False)
	bairro = db.Column(db.String(80), unique=False, nullable=False)
	rua = db.Column(db.String(80), unique=False, nullable=False)
	cidade = db.Column(db.String(80), unique=False, nullable=False)
	estado = db.Column(db.String(80), unique=False, nullable=False)
	pais = db.Column(db.String(80), unique=False, nullable=False)
	idade = db.Column(db.String(80), unique=False, nullable=False)
	telefone = db.Column(db.String(80), unique=False, nullable=False)
	email = db.Column(db.String(80), unique=False, nullable=False)
	pergunta1 = db.Column(db.String(80), unique=False, nullable=False)
	pergunta2 = db.Column(db.String(80), unique=False, nullable=False)

	def __init__(self, nome, sobrenome, cpf, bairro, rua, cidade, estado, pais, idade, telefone, email, pergunta1, pergunta2):
		self.nome = nome
		self.sobrenome = sobrenome
		self.cpf = cpf
		self.bairro = bairro
		self.rua = rua
		self.cidade = cidade
		self.estado = estado
		self.pais = pais
		self.idade = idade
		self.telefone = telefone
		self.email = email
		self.pergunta1 = pergunta1
		self.pergunta2 = pergunta2
		
	def __repr__(self):
		return "<Denuncia %r>" % self.nome

   











@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
	form = CadastroForm()
	if form.validate_on_submit():
		u1=Usuario(username=form.username.data, password=form.password.data, email=form.email.data)
		db.session.add(u1)
		db.session.commit()
		
	return render_template('Cadastro.html', form = form)

@app.route('/perfil', methods=['GET','POST'])
def perfil():
	form = PerfilForm()
	if form.validate_on_submit():
		u4=Perfil(nome=form.nome.data, sobrenome=form.sobrenome.data, cpf=form.cpf.data, email=form.email.data)
		db.session.add(u4)
		db.session.commit()
	return render_template('Perfil.html', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		u2=Login(username=form.username.data, password=form.password.data)
		db.session.add(u2)
		db.session.commit()
		
	return render_template('Login.html', form = form)

@app.route('/denuncia', methods=['GET','POST'])
def denuncia():
	form = DenunciaForm()
	if form.validate_on_submit():
		u3=Denuncia(
			nome=form.nome.data, 
			sobrenome=form.sobrenome.data, 
			cpf=form.cpf.data, 
			bairro=form.bairro.data,
			rua=form.rua.data, 
			cidade=form.cidade.data, 
			estado=form.estado.data, 
			pais=form.pais.data, 
			idade=form.idade.data, 
			telefone=form.telefone.data, 
			email=form.email.data, 
			pergunta1=form.pergunta1.data, 
			pergunta2=form.pergunta2.data
		)
		db.session.add(u3)
		db.session.commit()

	return render_template('Denuncia.html', form = form)
	
if __name__ == '__main__': 
	app.run(debug=True)