from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 
from flask_jwt_extended import JWTManager
from datetime import timedelta
from backend.blueprints.alumnos_blueprint import alumno_blueprint
from backend.blueprints.cursos_blueprint import curso_blueprint
from backend.blueprints.profesores_blueprint import profesor_blueprint
from backend.blueprints.usuarios_blueprint import usuario_blueprint
from backend.blueprints.grupos_blueprint import grupo_blueprint
from backend.blueprints.asistencias_blueprint import asistencia_blueprint
from backend.blueprints.horarios_blueprint import horario_blueprint
from backend.blueprints.justificaciones_blueprint import justificacion_blueprint
from backend.blueprints.sesiones_blueprint import sesion_blueprint
from backend.blueprints.img_blueprint import img_blueprint


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "pass"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

jwt = JWTManager(app)

app.register_blueprint(alumno_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(profesor_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(grupo_blueprint)
app.register_blueprint(asistencia_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(justificacion_blueprint)
app.register_blueprint(sesion_blueprint)
app.register_blueprint(img_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)