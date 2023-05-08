from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
import requests
import numpy as np
import ast, re
np.set_printoptions(precision=2)

from backend.models.mysql_sesiones_model import SesionesModel
sesionModel = SesionesModel()

sesion_blueprint = Blueprint('sesion_blueprint', __name__)

@sesion_blueprint.route('/sesion_create', methods=['POST'])
@cross_origin()
def create_sesion():

    content = sesionModel.create_sesion(request.json['fecha'],request.json['hora'], 
               request.json['tema'],request.json['horario_id'], request.json['justificacion_id'])
    return jsonify(content)

@sesion_blueprint.route('/sesion', methods=['DELETE'])
@cross_origin()
def delete_sesion():
    return jsonify(model.delete_sesion(int(request.json['sesion_id'])))

@sesion_blueprint.route('/sesion', methods=['POST'])
@cross_origin()
def sesion():
    return jsonify(model.get_sesion(int(request.json['sesion_id'])))

@sesion_blueprint.route('/sesions', methods=['GET'])
@cross_origin()
def sesions():
    return jsonify(model.get_sesions())

@sesion_blueprint.route('/update_sesion', methods=['PATCH'])
@cross_origin()
def update_sesion():
    content = sesionModel.update_sesion(request.json['sesion_id'], request.json['fecha'],request.json['hora'], 
                request.json['tema'],request.json['horario_id'], request.json['horario_id'])   
    return jsonify(content)

 