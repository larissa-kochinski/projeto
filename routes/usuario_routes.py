from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/login')
def login():
    return render_template('login.html', error=None)

@main_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', error=None)