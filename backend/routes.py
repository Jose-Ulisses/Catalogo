from flask import Blueprint, request, jsonify
from models import db, User, ClothingItem
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import JWTManager

routes = Blueprint('routes', __name__)

def init_jwt(app):
    JWTManager(app)

@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user and user.check_password(data.get('password')):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Login inválido"}), 401

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
