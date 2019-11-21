from add.site2 import db

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
	CPF = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)

	def __init__(self, nome, sobrenome, CPF, email):
		self.nome = nome
		self.sobrenome = sobrenome
		self.CPF = CPF
		self.email = email
		
	def __repr__(self):
		return "<Perfil %r>" % self.nome

class Login(db.Model):
	__tablename___="perfil"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), unique=True, nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password
		
	def __repr__(self):
		return "<Login %r>" % self.username


class Denuncia(db.Model):
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


   