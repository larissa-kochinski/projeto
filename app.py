from flask import Flask, request, render_template, redirect, flash, session

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('/index')
@app.route('/login', methods = ['POST'])
def login():
        login = request.form['username']
        senha = request.form['password']

        print(f'nome: {login}')
        print(f'senha: {senha}')
        return redirect('/login')

if __name__== '__main__':
      app.run(debug=True)
      