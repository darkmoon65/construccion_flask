from backend.models.mysql_connection_pool import MySQLPool

class GruposModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_matricula(self, matricula_id):    
        params = {'matricula_id' : matricula_id}      
        rv = self.mysql_pool.execute("""SELECT M.estado, A.nombre from matriculas M 
                                        inner join alumnos A on A.id = M.alumno_id
                                        where G.id = %(matricula_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'estado': result[0], 'nombre_alumno': result[1]}
            data.append(content)
            content = {}
        return data

    def get_matriculas(self):  
        rv = self.mysql_pool.execute("""SELECT M.estado, A.nombre from matriculas M 
                                        inner join alumnos A on A.id = M.alumno_id""")  
        data = []
        content = {}
        for result in rv:
            content = {'estado': result[0], 'nombre_alumno': result[1]}
            data.append(content)
            content = {}
        return data

    def create_matricula(self, estado, alumno_id, profesores_cursos_id ):    
        data = {
            'estado' : estado,
            'alumno_id' : alumno_id,
            'profesores_cursos_id' : profesores_cursos_id,
        }
        query = """insert into matriculas (estado, alumno_id, profesores_cursos_id) 
            values (%(estado)s,%(alumno_id)s,%(profesores_cursos_id)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_grupo(self, matricula_id):    
        params = {'matricula_id' : matricula_id}      
        query = """delete from matriculas where id = %(matricula_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


    def update_grupo(self, estado, matricula_id, alumno_id, profesores_cursos_id ):    
        data = {
            'matricula_id' : matricula_id,
            'estado' :estado,
            'alumno_id' : alumno_id,
            'profesores_cursos_id' : profesores_cursos_id,
        }  
        query = """update grupos set 
            estado = %(estado)s,
            alumno_id = %(alumno_id)s,
            profesores_cursos_id = %(profesores_cursos_id)s, 
            where id = %(matricula_id)s """    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data



if __name__ == "__main__":    
    tm = MatriculasModel()