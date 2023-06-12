from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
import requests

from backend.models.mysql_usuarios_model import UsuariosModel
model = UsuariosModel()

usuario_blueprint = Blueprint('usuario_blueprint', __name__)

@usuario_blueprint.route('/usuario_create', methods=['POST'])
@cross_origin()
def create_usuario():

    ## Consumiendo API openFace 
    url = "http://localhost:81/openfaceAPI"
    response = requests.post(url, files=dict(file = request.files['foto']))
    data = response.text
    vector = json.loads(data)

    content = model.create_usuario(request.form['nombre'],request.form['dni'], 
              request.form['password'],request.files['foto'], str(vector['result']))
    return jsonify(content)

@usuario_blueprint.route('/usuario_delete', methods=['POST'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['usuario_id'])))

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def usuario():
    return jsonify(model.get_usuario(int(request.json['usuario_id'])))

@usuario_blueprint.route('/usuarios', methods=['GET'])
@cross_origin()
def usuarios():
    return jsonify(model.get_usuarios())

@usuario_blueprint.route('/update_usuario', methods=['POST'])
@cross_origin()
def update_usuario():

    ## Consumiendo API openFace 
    url = "http://localhost:81/openfaceAPI"
    response = requests.post(url, files=dict(file = request.files['foto']))
    data = response.text
    vector = json.loads(data)

    content = model.update_usuario(request.form['usuario_id'], request.form['dni'],
                request.form['nombre'],request.form['password'],request.files['foto'], 
                str(vector['result']))
    return jsonify(content)

 