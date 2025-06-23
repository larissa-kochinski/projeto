from flask import Blueprint, render_template, request, redirect, session, url_for
import logging
import json
import os
import secrets
usuario_bp = Blueprint('usuario', __name__)

USER_FILE = 'usuarios.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

USERS = load_users()

@usuario_bp.route('/login')
def login():
    return render_template('login.html', error=None)

@usuario_bp.route('/servicos')
def servicos():
    return render_template('servicos.html', nomeuser= "Larissa")

@usuario_bp.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']

    users = load_users()
    if username in users and users[username] == password:
        session['usuario'] = username
        token = '1472'
        session['token'] = token
        return redirect(url_for('usuario.servicos'))
    else:
        logging.warning(f'Tentativa de login inválido: {username}')
        error = "Usuário ou senha incorreto"
        return render_template('login.html', error=error)
        

@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', error=None)

@usuario_bp.route('/cadastro', methods=['POST'])
def add_cadastro_post():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if not username or not password:
        error = "Preencha todos os campos."
        return render_template('cadastro.html', error=error)

    if password != confirm_password:
        error = "As senhas não conferem."
        return render_template('cadastro.html', error=error)

    users = load_users()  # sempre pega a versão atual
    if username in users:
        error = "Usuário já cadastrado."
        return render_template('cadastro.html', error=error)

    users[username] = password
    save_users(users)
    logging.info(f'Novo usuário cadastrado: {username}')
    return redirect(url_for('usuario.servicos'))

@usuario_bp.route('/inicio')
def inicio():
    return render_template('inicio.html')

@usuario_bp.route('/contato')
def contato():
    return render_template('contato.html')


@usuario_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('usuario.login'))

@usuario_bp.before_request
def check_auth():
    rotas_livres = [
        'usuario.login',
        'usuario.logout',
        'usuario.acesso',
        'usuario.cadastro',
        'usuario.inicio'
    ]

    print("Endpoint acessado:", request.endpoint)  # Ajuda no debug

    if request.endpoint in rotas_livres:
        return

    token = session.get('token')
    if token:
        return  # Está autenticado

    return redirect(url_for('usuario.login'))