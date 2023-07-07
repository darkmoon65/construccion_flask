from backend.models.mysql_connection_pool import MySQLPool
from datetime import timedelta
import datetime
import time

class AsistenciasModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_asistencia(self, asistencia_id):    
        params = {'asistencia_id' : asistencia_id}      
        rv = self.mysql_pool.execute("""SELECT A.id, A.estado, A.sesion_id from asistencias A
                                        where A.id = %(asistencia_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'asistencia_id': result[0], 'estado': result[1], 'sesion_id': result[2]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.mysql_pool.execute("""SELECT A.id, A.estado, A.sesion_id from asistencias A""")  
        data = []
        content = {}
        for result in rv:
            content = {'asistencia_id': result[0], 'estado': result[1], 'sesion_id': result[2]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, estado, sesion_id):    

        data = {
            'estado' : estado,
            'sesion_id' : sesion_id
        }
        query = """insert into asistencias (estado, sesion_id) 
            values (%(estado)s, %(sesion_id)s) """    
        cursor = self.mysql_pool.execute(query, data, commit=True)

        data['id'] = cursor.lastrowid
        return data

    def delete_asistencia(self, asistencia_id):    
        params = {'asistencia_id' : asistencia_id}      
        query = """delete from asistencias where id = %(asistencia_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def update_asistencia(self, asistencia_id,estado,sesion_id ):    
        data = {
            'asistencia_id': asistencia_id,
            'estado' : estado,
            'sesion_id' : dni
        }  
        query = """update asistencias set 
                    estado = %(estado)s,
                    sesion_id = %(sesion_id)s 
                    where id = %(asistencia_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def check_curso_horario(self, usuario_id):
        params = {
            'usuario_id': usuario_id,
        }  
        rv = self.mysql_pool.execute ("""select H.hora_inicio , H.hora_fin from usuarios U 
                    inner join alumnos A on A.usuario_id = U.id
                    inner join matriculas M on M.alumno_id = A.id
                    inner join profesores_cursos PC on PC.id = M.profesores_cursos_id
                    inner join cursos C on C.id = PC.curso_id
                    inner join grupos G on G.curso_id = C.id
                    inner join sesiones S on S.id = G.sesion_id
                    inner join horarios H on H.id = S.horario_id
                    where U.id = %(usuario_id)s """, params ) 
        data = []
        content = {}
        if(len(rv) == 0):
            return False
        for result in rv:
            content = {'hora_inicio': result[0], 'hora_fin': result[1]}
            data.append(content)
            content = {}

        segundos_inicio = data[0]['hora_inicio'].total_seconds() 
        segundos_fin = data[0]['hora_fin'].total_seconds()
        now = datetime.datetime.now()
        segundos_actual = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        print(segundos_actual)
        if(segundos_actual < segundos_fin and segundos_actual > segundos_inicio):
            return True
        else:
            return False
if __name__ == "__main__":    
    tm = AsistenciasModel()