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
from flask_jwt_extended import jwt_required, get_jwt_identity

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
    usuario = usuarioModel.get_usuario_by_dni(int(request.form['dni']))
    if(len(usuario) == 0):
        return jsonify({"result": "No existe usuario con ese DNI" , "estado": "0"})
    else:
        vector_imagen_guardada = usuario[0]['vector']

    if(vector_imagen_enviada[1] == " "):
        vector_imagen_enviada = '[' + vector_imagen_enviada[2:]
    if(vector_imagen_guardada[1] == " "):
        vector_imagen_guardada = '[' + vector_imagen_guardada[2:]

    arr1 = re.sub('\s+', ',', vector_imagen_guardada)
    arr2 = re.sub('\s+', ',', vector_imagen_enviada)
    vector1_numerico = np.array(ast.literal_eval(arr1))
    vector2_numerico = np.array(ast.literal_eval(arr2))

    dist = np.linalg.norm(vector1_numerico - vector2_numerico)
    print(dist)
    if(dist > 0.80):
        return jsonify({"result": "No es el alumno"})
    else:
        print(usuario[0]['usuario_id'])
        result_check = asistenciaModel.check_curso_horario(usuario[0]['usuario_id'])
        if(result_check):
            return jsonify({"result": "Marcado de asistencia exitoso", "estado": "1"})
        else:
            return jsonify({"result": "No tiene ningun curso en dicho horario" , "estado": "0"})

@asistencia_blueprint.route('/asistencia', methods=['DELETE'])
@cross_origin()
def delete_asistencia():
    return jsonify(asistenciaModel.delete_asistencia(int(request.json['usuario_id'])))

@asistencia_blueprint.route('/asistencia', methods=['POST'])
@cross_origin()
def asistencia():
    return jsonify(asistenciaModel.get_asistencia(int(request.json['usuario_id'])))

@asistencia_blueprint.route('/asistencias', methods=['GET'])
@cross_origin()
@jwt_required()
def asistencias():
    return jsonify(asistenciaModel.get_asistencias())

@asistencia_blueprint.route('/update_asistencia', methods=['PATCH'])
@cross_origin()
def update_asistencia():
    content = asistenciaModel.update_asistencia(request.json['usuario_id'],request.json['dni'],
              request.json['nombre'], request.json['password'] , request.json['path_foto'], 
              request.json['vector'])    

    return jsonify(content)

 