from backend.models.mysql_connection_pool import MySQLPool

class UsuariosModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_usuario(self, usuario_id):    
        params = {'usuario_id' : usuario_id}      
        rv = self.mysql_pool.execute("""SELECT U.id, U.nombre, U.DNI, 
                                        U.path_foto, U.vector from usuarios U
                                        where U.id = %(usuario_id)s""", params)                
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

    def get_usuarios(self):  
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

    def create_usuario(self, nombre, dni, password, foto, vector, nombreimg):    

        ## Guardando imagen server
        route = "img/" + nombreimg
        #foto.save(route)

        data = {
            'nombre_usuario' : nombre,
            'dni_usuario' : dni,
            'password' : password,
            'ruta_foto' : route,
            'vector': vector
        }
        query = """insert into usuarios (nombre, DNI, password, path_foto, vector) 
            values (%(nombre_usuario)s, %(dni_usuario)s, %(password)s, %(ruta_foto)s, %(vector)s) """    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_usuario(self, usuario_id):    
        params = {'usuario_id' : usuario_id}      
        query = """delete from usuarios where id = %(usuario_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



    def update_usuario(self, usuario_id, dni, nombre, password, path_foto, vector ):    
        route = "img/" + path_foto
        ##path_foto.save(route)

        params = {'usuario_id' : usuario_id,
                'nombre' : nombre,
                'DNI' : dni,
                'password' : password,
                'path_foto' : route,
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
    tm = UsuariosModel()