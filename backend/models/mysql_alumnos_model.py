from backend.models.mysql_connection_pool import MySQLPool

class AlumnosModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_alumno(self, alumno_id):    
        params = {'alumno_id' : alumno_id}      
        rv = self.mysql_pool.execute("""SELECT A.id_alumno, U.nombre, U.DNI from alumnos A 
                                        inner join usuarios U on A.usuario_id = U.id
                                        where A.id = %(alumno_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'alumno_id': result[0], 'nombre_alumno': result[1], 'alumno_dni': result[2]}
            data.append(content)
            content = {}
        return data

    def get_alumnos(self):  
        rv = self.mysql_pool.execute("""SELECT A.id_alumno, U.nombre, U.DNI from alumnos A 
                                        inner join usuarios U on A.id_usuario = U.id""")  
        data = []
        content = {}
        for result in rv:
            content = {'alumno_id': result[0], 'nombre_alumno': result[1], 'alumno_dni': result[2]}
            data.append(content)
            content = {}
        return data

    def create_alumno(self, usuario_id):    
        data = {
            'usuario_id' : usuario_id,
        }  
        query = """insert into alumnos (id_usuario) 
            values (%(usuario_id)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_alumno(self, alumno_id):    
        params = {'alumno_id' : alumno_id}      
        query = """delete from alumnos where id_alumno = %(alumno_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = AlumnosModel()