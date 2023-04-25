from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_grupos_model import GruposModel
model = GruposModel()

grupo_blueprint = Blueprint('grupo_blueprint', __name__)

@grupo_blueprint.route('/grupo_create', methods=['POST'])
@cross_origin()
def create_grupo():
    content = model.create_grupo(request.json['curso_id'],request.json['horario_id'], request.json['categoria'] )    
    return jsonify(content)

@grupo_blueprint.route('/grupo', methods=['DELETE'])
@cross_origin()
def delete_grupo():
    return jsonify(model.delete_grupo(int(request.json['grupo_id'])))

@grupo_blueprint.route('/grupo', methods=['POST'])
@cross_origin()
def grupo():
    return jsonify(model.get_grupo(int(request.json['grupo_id'])))

@grupo_blueprint.route('/grupos', methods=['POST'])
@cross_origin()
def grupos():
    return jsonify(model.get_grupos())