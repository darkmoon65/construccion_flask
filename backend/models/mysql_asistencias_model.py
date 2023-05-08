from backend.models.mysql_connection_pool import MySQLPool

class AsistenciasModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_asistencia(self, usuario_id):    
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

    def get_asistencias(self):  
        rv = self.mysql_pool.execute("""SELECT U.id, U.nombre, U.DNI, 
                                        U.path_foto, U.vector from usuarios U""")  
        data = []
        content = {}
        for result in rv:
            content = {'usuario_id': result[0], 
                       'nombre_usuario': result[1], 
                       'dni_usuario': result[2],
                       'ruta_foto': result[3],
                       'vector': result[4]
                       }
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, nombre, dni, password, file, vector):    

        data = {
            'nombre' : nombre,
            'dni' : dni,
            'password' : password,
            'path_foto' : route,
            'vector': vector
        }
        query = """insert into usuarios (nombre, DNI, password, path_foto, vector) 
            values (%(nombre)s, %(dni)s, %(password)s, %(path_foto)s, %(vector)s) """    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_asistencia(self, usuario_id):    
        params = {'usuario_id' : usuario_id}      
        query = """delete from usuarios where id = %(usuario_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



    def update_asistencia(self, usuario_id, dni, nombre, password, path_foto, vector ):    
        params = {'usuario_id' : usuario_id,
                'nombre' : nombre,
                'DNI' : dni,
                'password' : password,
                'path_foto' : path_foto,
                'vector' : vector,
        }      
        query = """update usuarios set 
                    nombre = %(nombre)s,
                    DNI = %(DNI)s,
                    password = %(password)s,
                    path_foto = %(path_foto)s,
                    vector =%(vector)s
                    where id = %(usuario_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
 
if __name__ == "__main__":    
    tm = AsistenciasModel()