from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from model.endereco import Endereco_db
from model.pessoa import Pessoa_db
from model.aluno import Aluno_db
from model.funcionario import Funcionario_db
from model.gestorApp import GestorApp_db
from model.instituicaoDeEnsino import InstituicaoDeEnsino_db
from model.motorista import Motorista_db
from model.passageiro import Passageiro_db
from model.pessoa import Pessoa_db
from model.prefeito import Prefeito_db
from model.prefeitura import Prefeitura_db
from model.rota import Rota_db
from model.cidade import Cidade_db
from model.uf import Uf_db
from model.veiculo import Veiculo_db

from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aemotor:aemotor@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)
api = Api(app)
