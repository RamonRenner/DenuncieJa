from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DenunciaForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    sobrenome = StringField("Sobrenome", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired()])
    bairro = StringField("Bairro", validators=[DataRequired()])
    rua = StringField("Rua", validators=[DataRequired()])
    cidade = StringField("Cidade", validators=[DataRequired()])
    estado = StringField("Estado", validators=[DataRequired()])
    pais = StringField("País", validators=[DataRequired()])
    idade = StringField("Idade", validators=[DataRequired()])
    telefone = StringField("Telefone", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    pergunta1 = StringField("O que você sofreu?", validators=[DataRequired()])
    pergunta2 = StringField("Quem fez isso com você?", validators=[DataRequired()])
    botao = SubmitField("Denunciar")