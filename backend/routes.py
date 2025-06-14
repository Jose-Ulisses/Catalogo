from flask import Blueprint, request, jsonify, render_template
from models import db, User, ClothingItem
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import JWTManager

routes = Blueprint('routes', __name__)

def init_jwt(app):
    JWTManager(app)

# Autenticação
@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user and user.check_password(data.get('password')):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Login inválido"}), 401

# API - Roupas
@routes.route('/clothes', methods=['GET'])
@jwt_required()
def all_clothes():
    clothes = ClothingItem.query.all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'gender': item.gender,
        'size': item.size,
        'color': item.color,
        'type': item.type,
        'season': item.season,
        'price': item.price
    } for item in clothes])

@routes.route('/clothes/masculino', methods=['GET'])
@jwt_required()
def masculine_clothes():
    clothes = ClothingItem.query.filter_by(gender='masculino').all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'gender': item.gender,
        'size': item.size,
        'color': item.color,
        'type': item.type,
        'season': item.season,
        'price': item.price
    } for item in clothes])

@routes.route('/clothes/feminino', methods=['GET'])
@jwt_required()
def feminine_clothes():
    clothes = ClothingItem.query.filter_by(gender='feminino').all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'gender': item.gender,
        'size': item.size,
        'color': item.color,
        'type': item.type,
        'season': item.season,
        'price': item.price
    } for item in clothes])

# Páginas do site
@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/contato')
def contato():
    return render_template('contato.html')

@routes.route('/sobre')
def sobre():
    return render_template('sobre.html')

@routes.route('/relatorio')
def relatorio():
    return render_template('relatorio.html')

# Página de Produto (genérica)
@routes.route('/produto')
def produto():
    return render_template('produto/produto.html')

# Feminino
@routes.route('/feminino')
def feminino():
    return render_template('categorias/feminino/feminino.html')

@routes.route('/feminino/camisetas-regatas')
def camisetas_regatas_fem():
    return render_template('categorias/feminino/camisetas_regatas_fem.html')

@routes.route('/feminino/casacos-jaquetas')
def casacos_jaquetas_fem():
    return render_template('categorias/feminino/casacos_jaquetas_fem.html')

@routes.route('/feminino/jeans-sarja')
def jeans_sarja_fem():
    return render_template('categorias/feminino/jeans_sarja_fem.html')

@routes.route('/feminino/camisas')
def camisas_fem():
    return render_template('categorias/feminino/camisas_fem.html')

# Masculino
@routes.route('/masculino')
def masculino():
    return render_template('categorias/masculino/masculino.html')

@routes.route('/masculino/camisas')
def camisas_masc():
    return render_template('categorias/masculino/camisasMasc.html')

@routes.route('/masculino/calcas')
def calcas_masc():
    return render_template('categorias/masculino/calcasMasc.html')

@routes.route('/masculino/casacos-jaquetas')
def casaco_jaqueta_masc():
    return render_template('categorias/masculino/casaco-jaqueta.html')

@routes.route('/masculino/polo')
def polo_masc():
    return render_template('categorias/masculino/polo.html')
