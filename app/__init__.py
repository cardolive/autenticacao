from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'auth753$%ZZ'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
    db.init_app(app)

    """ Iniciando o flask login 
    especificando uma visualização de login
    por causa do blueprint. 
    Será auth.login 
    Quando alguem não estiver autenticado
    será redirecionado para o login"""
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    """ a importação do usuario esta aqui pq
    o usuario usa o db que foi declarado logo acima"""
    from .models import User

    """ criando o carregador de usuário para passar entre
    a navegação de páginas da app.
    Logado, o flask cria um cookie e dentro dele
    existe o id do usuário. 
    Este cookie é enviado a cada request 
    Aqui é carregado o usuario pegando o id do cookie"""
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app