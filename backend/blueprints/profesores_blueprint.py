from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_profesores_model import ProfesoresModel
model = ProfesoresModel()

profesor_blueprint = Blueprint('profesor_blueprint', __name__)

@profesor_blueprint.route('/profesor_create', methods=['POST'])
@cross_origin()
def create_profesor():
    content = model.create_profesor(request.json['usuario_id'])    
    return jsonify(content)

@profesor_blueprint.route('/profesor', methods=['DELETE'])
@cross_origin()
def delete_profesor():
    return jsonify(model.delete_profesor(int(request.json['profesor_id'])))

@profesor_blueprint.route('/profesor', methods=['POST'])
@cross_origin()
def profesor():
    return jsonify(model.get_profesor(int(request.json['profesor_id'])))

@profesor_blueprint.route('/profesores', methods=['GET'])
@cross_origin()
def profesors():
    return jsonify(model.get_profesores())


@profesor_blueprint.route('/update_profesor', methods=['PATCH'])
@cross_origin()
def update_profesor():
    content = model.update_profesor(request.json['usuario_id'], request.json['profesor_id'])    

    return jsonify(content)
