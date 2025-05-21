from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'larissa@' and password == '2007':
        return redirect('/servicos')
    else:
        print('Usuário não encontrado')
        return "Usuário ou senha incorretos", 401


@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


if __name__ == '__main__':
    app.run(debug=True)
