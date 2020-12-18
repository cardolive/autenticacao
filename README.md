Criando enviroment
==================
>python -m venv venv # ou py -m venv venv
>venv\Scripts\activate (windows)
>. venv/bin/activate (linux)
>python -m pip install --upgrade pip

Instalando dependencias
=======================

>pip install flask
>pip install flask-SQLAlchemy
>pip install flask-Login

Para rodar a app: (set - windows / export linux)
================
> set FLASK_APP=app
#obedecendo a estrutura da aplicação indicando que o main esta na pasta app (poderia ter outro nome, o importante é que ao montar a variavel FLASK_APP, ligue ao nome da pasta principal do projeto, aqui nomeada de 'app')
> set FLASK_ENV=development
> flask run

Criando o DB
============
no terminal
> python
> from app import db, create_app
> db.create_all(app=create_app())
> exit()
    para evitar avisos de modificação do db, pode-se usar a seguinte configuração:
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS = False']


