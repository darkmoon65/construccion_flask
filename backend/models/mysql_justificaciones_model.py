from backend.models.mysql_connection_pool import MySQLPool

class justificacionesModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_justificacion(self, justificacion_id):    
        params = {'justificacion_id' : justificacion_id}      
        rv = self.mysql_pool.execute("""SELECT J.id, J.descripcion, J.estado, J.fecha_creacion
                                        from justificaciones J
                                        where J.id = %(justificacion_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'justificacion_id': result[0],
            'descripcion': result[1],
            'estado': result[1], 
            'fecha_creacion': result[2]}
            data.append(content)
            content = {}
        return data

    def get_justificacions(self):  
        rv = self.mysql_pool.execute("""SELECT U.id, U.nombre, U.DNI, 
                                        U.path_foto, U.vector from justificacions U""")  
        data = []
        content = {}
        for result in rv:
            content = {'justificacion_id': result[0], 
                       'nombre_justificacion': result[1], 
                       'dni_justificacion': result[2],
                       'ruta_foto': result[3],
                       'vector': result[4]
                       }
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, nombre, dni, password):    
        data = {
            'nombre' : nombre,
            'dni' : dni,
            'password' : password,
        }  
        query = """insert into justificacions (nombre, DNI, password) 
            values (%(nombre)s, %(dni)s, %(password)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_justificacion(self, justificacion_id):    
        params = {'justificacion_id' : justificacion_id}      
        query = """delete from justificacions where id = %(justificacion_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



    def update_justificacion(self, justificacion_id, dni, nombre, password, path_foto, vector ):    
        params = {'justificacion_id' : justificacion_id,
                'nombre' : nombre,
                'DNI' : dni,
                'password' : password,
                'path_foto' : path_foto,
                'vector' : vector,
        }      
        query = """update justificacions set 
                    nombre = %(nombre)s,
                    DNI = %(DNI)s,
                    password = %(password)s,
                    path_foto = %(path_foto)s,
                    vector =%(vector)s
                    where id = %(justificacion_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
 
if __name__ == "__main__":    
    tm = justificacionsModel()