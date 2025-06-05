from flask import Blueprint, render_template, request, redirect, url_for
import logging
usuario_bp = Blueprint('usuario', __name__)

USERS = {
    "larissa": "1234"
}

@usuario_bp.route('/login')
def login():
    return render_template('login.html', error=None)

@usuario_bp.route('/servicos')
def servicos():
    return render_template(url_for('usuario.servicos'))

@usuario_bp.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']

    if username in USERS and USERS[username] == password:
        return redirect(url_for('usuario.servicos'))
    else:
        logging.warning(f'Tentativa de login inválido: {username}')
        return render_template('login.html', error="Usuário ou senha incorretos")

@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', error=None)

@usuario_bp.route('/add_cadastro', methods=['POST'])
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

    if username in USERS:
        error = "Usuário já cadastrado."
        return render_template('cadastro.html', error=error)

    USERS[username] = password
    logging.info(f'Novo usuário cadastrado: {username}')
    return redirect(url_for('usuario.servicos'))
