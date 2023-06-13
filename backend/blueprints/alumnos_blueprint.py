from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_alumnos_model import AlumnosModel
model = AlumnosModel()

alumno_blueprint = Blueprint('alumno_blueprint', __name__)

@alumno_blueprint.route('/alumno_create', methods=['POST'])
@cross_origin()
def create_alumno():
    content = model.create_alumno(request.json['usuario_id'])    
    return jsonify(content)

@alumno_blueprint.route('/alumno', methods=['DELETE'])
@cross_origin()
def delete_alumno():
    return jsonify(model.delete_alumno(int(request.json['alumno_id'])))

@alumno_blueprint.route('/alumno', methods=['POST'])
@cross_origin()
def alumno():
    return jsonify(model.get_alumno(int(request.json['alumno_id'])))

@alumno_blueprint.route('/alumnos', methods=['GET'])
@cross_origin()
def alumnos():
    return jsonify(model.get_alumnos())

@alumno_blueprint.route('/alumno_update', methods=['POST'])
@cross_origin()
def alumno_update():
    content = model.alumno_update(request.json['usuario_id'])    
    return jsonify(content)