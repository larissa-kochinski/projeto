from flask import Flask, render_template, request, redirect
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

USERS = {
    "": ""
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html', error=None)

@app.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']

    if username in USERS and USERS[username] == password:
        return redirect('/servicos')
    else:
        logging.warning(f'Tentativa de login inválido: {username}')
        return render_template('login.html', error="Usuário ou senha incorretos")

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', error=None)

@app.route('/cadastro', methods=['POST'])
def cadastro_post():
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
    return redirect('/servicos')

if __name__ == '__main__':
    app.run(debug=True)
