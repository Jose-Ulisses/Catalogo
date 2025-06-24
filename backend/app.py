from flask import Flask, render_template
import os
from config import Config
from models import db, bcrypt
from database import init_db
from routes import routes, init_jwt


app = Flask(__name__, static_folder='static', template_folder='templates')

app.config.from_object(Config)

@app.route('/')
def index():
    caminho_pasta = os.path.join('static\catalogo\masculino\camisas e regatas')
    imagens = os.listdir(caminho_pasta)
    imagens = [f'imagens/{img}' for img in imagens if img.lower().endswitch(('.png','.jpg','.jpeg','.gif'))]
    return render_template('index.html', imagens=imagens)

db.init_app(app)
bcrypt.init_app(app)
init_db(app)
init_jwt(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
