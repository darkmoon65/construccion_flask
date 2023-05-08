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

from backend.models.mysql_asistencias_model import AsistenciasModel
from backend.models.mysql_usuarios_model import UsuariosModel
usuarioModel = UsuariosModel()
asistenciaModel = AsistenciasModel()

asistencia_blueprint = Blueprint('asistencia_blueprint', __name__)

@asistencia_blueprint.route('/asistencia_create', methods=['POST'])
@cross_origin()
def create_usuario():

    ## Consumiendo API openFace 
    url = "http://localhost:81/openfaceAPI"
    response = requests.post(url, files=dict(file = request.files['foto']))
    data = response.text
    vector_imagen_enviada = json.loads(data)['result']

    ##Consultando imagen guardada
    usuario = usuarioModel.get_usuario(int(request.form['usuario_id']))
    vector_imagen_guardada = usuario[0]['vector']

    arr1 = re.sub('\s+', ',', vector_imagen_guardada)

    if(vector_imagen_enviada[1] == " "):
        vector_imagen_enviada = '[' + vector_imagen_enviada[2:]
        
    arr2 = re.sub('\s+', ',', vector_imagen_enviada)
    vector1_numerico = np.array(ast.literal_eval(arr1))
    vector2_numerico = np.array(ast.literal_eval(arr2))

    dist = np.linalg.norm(vector1_numerico - vector2_numerico)
    return(str(dist))
    ##content = asistenciaModel.create_usuario(request.form['nombre'],request.form['dni'], 
    ##          request.form['password'],request.files['foto'], str(vector['result']))
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['usuario_id'])))

@asistencia_blueprint.route('/asistencia', methods=['POST'])
@cross_origin()
def usuario():
    return jsonify(model.get_usuario(int(request.json['usuario_id'])))

@asistencia_blueprint.route('/asistencias', methods=['GET'])
@cross_origin()
def asistencias():
    return jsonify(model.get_asistencias())

@asistencia_blueprint.route('/update_asistencia', methods=['PATCH'])
@cross_origin()
def update_usuario():
    content = asistenciaModel.update_usuario(request.json['usuario_id'],request.json['dni'],
              request.json['nombre'], request.json['password'] , request.json['path_foto'], 
              request.json['vector'])    

    return jsonify(content)

 