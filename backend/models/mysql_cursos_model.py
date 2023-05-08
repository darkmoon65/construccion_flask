from backend.models.mysql_connection_pool import MySQLPool

class CursosModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_curso(self, curso_id):    
        params = {'curso_id' : curso_id}      
        rv = self.mysql_pool.execute("""SELECT C.id, C.nombre, C.descripcion, P.nombre from cursos C 
                                        inner join profesores P on C.profesor_id = P.id
                                        where C.id = %(curso_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'curso_id': result[0], 'nombre_curso': result[1], 'curso_descripcion': result[2], 'profesor_nombre': result[3]}
            data.append(content)
            content = {}
        return data

    def get_cursos(self):  
        rv = self.mysql_pool.execute("""SELECT C.id, C.nombre, C.descripcion, U.nombre from cursos C 
                                        inner join profesores P on C.profesor_id = P.id
                                        inner join usuarios U on P.id_usuario = U.id""")  
        data = []
        content = {}
        for result in rv:
            content = {'curso_id': result[0], 'nombre_curso': result[1], 'curso_descripcion': result[2], 'profesor_nombre': result[3]}
            data.append(content)
            content = {}
        return data

    def create_curso(self, nombre, descripcion, profesor_id):    
        data = {
            'nombre' : nombre,
            'descripcion' : descripcion,
            'profesor_id' : profesor_id,
        }  
        query = """insert into cursos (nombre, descripcion, profesor_id) 
            values (%(nombre)s, %(descripcion)s, %(profesor_id)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_curso(self, curso_id):    
        params = {'curso_id' : curso_id}      
        query = """delete from cursos where id = %(curso_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def update_curso(self, nombre, descripcion):    
        data = {
            'curso_id' : curso_id,
            'nombre' : nombre,
            'descripcion' : descripcion,
        }  
        query = """update cursos set (
            nombre = %(nombre)s,
            descripcion = %(desripcion)s) where id = %(curso_id)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

if __name__ == "__main__":    
    tm = CursosModel()