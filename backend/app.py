from flask import Flask
from config import Config
from models import db, bcrypt
from database import init_db
from routes import routes, init_jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
init_db(app)
init_jwt(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
