from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_justificaciones_model import justificacionesModel
model = justificacionesModel()

justificacion_blueprint = Blueprint('justificacion_blueprint', __name__)

@justificacion_blueprint.route('/justificacion_create', methods=['POST'])
@cross_origin()
def create_justificacion():
    content = model.create_justificacion(
              request.json['descripcion'], 
              request.json['estado'], 
              request.json['fecha_creacion'] )    
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['DELETE'])
@cross_origin()
def delete_justificacion():
    return jsonify(model.delete_justificacion(int(request.json['justificacion_id'])))

@justificacion_blueprint.route('/justificacion', methods=['POST'])
@cross_origin()
def justificacion():
    return jsonify(model.get_justificacion(int(request.json['justificacion_id'])))

@justificacion_blueprint.route('/justificaciones', methods=['GET'])
@cross_origin()
def justificaciones():
    return jsonify(model.get_justificaciones())

@justificacion_blueprint.route('/update_justificacion', methods=['PATCH'])
@cross_origin()
def update_justificacion():
    content = model.update_justificacion(request.json['justificacion_id'],
              request.json['descripcion'], request.json['estado'], 
              request.json['fecha_creacion'])    

    return jsonify(content)

 