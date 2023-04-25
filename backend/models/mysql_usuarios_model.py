from backend.models.mysql_connection_pool import MySQLPool

class UsuariosModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_usuario(self, usuario_id):    
        params = {'usuario_id' : usuario_id}      
        rv = self.mysql_pool.execute("""SELECT U.id, U.nombre, U.DNI from usuarios U
                                        where U.id = %(usuario_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'usuario_id': result[0], 'nombre_usuario': result[1], 'dni_usuario': result[2]}
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):  
        rv = self.mysql_pool.execute("""SELECT U.id, U.nombre, U.DNI from usuarios U""")  
        data = []
        content = {}
        for result in rv:
            content = {'usuario_id': result[0], 'nombre_usuario': result[1], 'dni_usuario': result[2]}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, nombre, dni, password):    
        data = {
            'nombre' : nombre,
            'dni' : dni,
            'password' : password,
        }  
        query = """insert into usuarios (nombre, DNI, password) 
            values (%(nombre)s, %(dni)s, %(password)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_usuario(self, usuario_id):    
        params = {'usuario_id' : usuario_id}      
        query = """delete from usuarios where id = %(usuario_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = UsuariosModel()