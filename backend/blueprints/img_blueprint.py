from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask import send_file
from flask_cors import CORS, cross_origin 
import io
import numpy as np
from matplotlib import pylab as plt


img_blueprint = Blueprint('img_blueprint', __name__)
@img_blueprint.route('/img/<string:nombre_imagen>', methods=['GET'])
@cross_origin()
def imagen(nombre_imagen):
    ruta = "img/"+ nombre_imagen
    return send_file(ruta,  mimetype='text/plain')

 