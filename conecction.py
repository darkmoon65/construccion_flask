from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Pass.123$@127.0.0.1/flaskmysql'

#posgresql
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3307/construccion"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # para q no de warnings

#db = SQLAlchemy(app)
#ma = Marshmallow(app)

# tabla task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=False)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

#with app.app_context():
   # db.create_all() # crea todas las tablas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


#task_schema = TaskSchema()
#tasks_schema = TaskSchema(many=True)

if __name__ == "__main__":
    app.run(debug=True, port=5002)