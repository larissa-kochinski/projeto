from flask import Blueprint, render_template, request, session, redirect, url_for

compra_bp = Blueprint('compra', __name__)

@compra_bp.route('/aluguel')
def aluguel():
    return render_template('aluguel.html')

@compra_bp.route('/adicionar', methods=['POST'])
def adicionar_compra():
    item = {
        'nome': request.form['nome'],
        'preco': float(request.form['preco']),
        'tipo': request.form['tipo']
    }
    if 'aluguel' not in session:
        session['aluguel'] = []
    session['aluguel'].append(item)
    session.modified = True
    return redirect(url_for('compra.ver_compra'))

@compra_bp.route('/')
def ver_compra():
    return render_template('compra.html', compra=session.get('compra', []))

@compra_bp.route('/remover_item/<int:item_index>')
def remover_item(item_index):
    if 'compra' in session and 0 <= item_index < len(session['compra']):
        session['compra'].pop(item_index)
        session.modified = True
    return redirect(url_for('compra.ver_compra'))

@compra_bp.route('/finalizar')
def finalizar_compra():
    if 'aluguel' in session:
        total = sum(item['preco'] for item in session['aluguel'])
        session.pop('aluguel', None)
        return render_template('finalizar_compra.html', total=total)
    else:
        return redirect(url_for('compra.ver_compra'))