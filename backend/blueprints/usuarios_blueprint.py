from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
import requests
import copy
import sys
import numpy as np
import os
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models.mysql_usuarios_model import UsuariosModel
model = UsuariosModel()

usuario_blueprint = Blueprint('usuario_blueprint', __name__)

@usuario_blueprint.route('/usuario_create', methods=['POST'])
@cross_origin()
def create_usuario():

    copia = request.files['foto']
    nombreImg = copia.filename
    copia.save("img/"+ nombreImg)

    img = open("img/"+ nombreImg, 'rb').read()
    ## Consumiendo API openFace
    url = "http://localhost:81/openfaceAPI"
    response = requests.post(url, files=dict(file = img))
    data = response.text
    vector = json.loads(data)

    content = model.create_usuario(request.form['nombre'],request.form['dni'], 
              request.form['password'],copia, str(vector['result']), nombreImg)
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
@jwt_required()
def usuarios():
    return jsonify(model.get_usuarios())

@usuario_blueprint.route('/update_usuario', methods=['POST'])
@cross_origin()
def update_usuario():
    if( 'foto' in request.files ):
        copia = request.files['foto']
        nombreImg = copia.filename
        copia.save("img/"+ nombreImg)

        img = open("img/"+ nombreImg, 'rb').read()
    else:    
        url = "http://localhost:5000/usuario"
        us = requests.post(url, json={'usuario_id' : request.form['usuario_id']})
        user_found = us.json()

        img = open(user_found[0]['ruta_foto'], 'rb').read()
        nombreImg = user_found[0]['ruta_foto'].split('/')[1]
    
    ## Consumiendo API openFace 
    url = "http://localhost:81/openfaceAPI"
    response = requests.post(url, files=dict(file = img))
    data = response.text
    vector = json.loads(data)

    content = model.update_usuario(request.form['usuario_id'], request.form['dni'],
                request.form['nombre'],request.form['password'],nombreImg, 
                str(vector['result']))
    return jsonify(content)

@usuario_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    dni = request.json.get("dni", None)
    password = request.json.get("password", None)
    
    user = model.check_usuario_login(dni, password)
    if len(user) < 1:
        return jsonify({"status": "false", "msg": "Dni o contraseña incorrecta"}), 401

    access_token = create_access_token(identity = user[0]['usuario_id'])
    return jsonify({ "token": access_token, "user_id": user[0]['usuario_id'] })