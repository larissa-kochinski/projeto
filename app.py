from flask import Flask
from routes.main_routes import main_bp
from routes.usuario_routes import usuario_bp
from routes.compra_routes import compra_bp

app = Flask(__name__)
app.secret_key = 'tassie'

app.register_blueprint(main_bp)
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(compra_bp, url_prefix='/compra')

if __name__ == '__main__':
    app.run(debug=True)
