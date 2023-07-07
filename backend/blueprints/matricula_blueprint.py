from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_matriculas_model import MatriculasModel
model = MatriculasModel()

matricula_blueprint = Blueprint('matricula_blueprint', __name__)

@grupo_blueprint.route('/matricula_create', methods=['POST'])
@cross_origin()
def create_matricula():
    content = model.create_matricula(request.json['alumno_id'],request.json['profesores_cursos_id'], request.json['estado'] )    
    return jsonify(content)

@grupo_blueprint.route('/grupo_delete', methods=['POST'])
@cross_origin()
def delete_matricula():
    return jsonify(model.delete_matricula(int(request.json['matricula_id'])))

@grupo_blueprint.route('/matricula', methods=['POST'])
@cross_origin()
def matricula():
    return jsonify(model.get_matricula(int(request.json['matricula_id'])))

@grupo_blueprint.route('/matriculas', methods=['POST'])
@cross_origin()
def matriculas():
    return jsonify(model.get_matriculas())

@grupo_blueprint.route('/update_matricula', methods=['POST'])
@cross_origin()
def update_matricula():
    content = model.update_matricula(request.json['alumno_id'],request.json['profesores_cursos_id'], request.json['estado'] )    
    return jsonify(content.update_matricula(int(request.json['matricula_id'])))
