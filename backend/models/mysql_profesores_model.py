from backend.models.mysql_connection_pool import MySQLPool

class ProfesoresModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_profesor(self, profesor_id):    
        params = {'profesor_id' : profesor_id}      
        rv = self.mysql_pool.execute("""SELECT P.id, U.nombre, U.dni from profesores P 
                                        inner join usuarios U on P.usuario_id = U.id
                                        where P.id = %(profesor_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'profesor_id': result[0], 'nombre_profesor': result[1], 'dni_profesor': result[2]}
            data.append(content)
            content = {}
        return data

    def get_profesores(self):  
        rv = self.mysql_pool.execute("""SELECT P.id, U.nombre, U.dni from profesores P 
                                        inner join usuarios U on P.id_usuario = U.id""")  
        data = []
        content = {}
        for result in rv:
            content = {'profesor_id': result[0], 'nombre_profesor': result[1], 'dni_profesor': result[2]}
            data.append(content)
            content = {}
        return data

    def create_profesor(self, usuario_id):    
        data = {
            'usuario_id' : usuario_id,
        }  
        query = """insert into profesores (id_usuario) 
            values (%(usuario_id)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_profesor(self, profesor_id):    
        params = {'profesor_id' : profesor_id}      
        query = """delete from profesores where id = %(profesor_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = ProfesoresModel()