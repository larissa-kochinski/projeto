from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']
   
    if username == 'gabriel@' and password == '123':
        return redirect('/servico')
    else:
        print('Usuário não encontrado')
        return "Usuário ou senha incorretos", 401


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


if __name__ == '_main_':
    print('Iniciando o servidor Flask...')
    app.run(host='0.0.0.0', port=5000, debug=True)