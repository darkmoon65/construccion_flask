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
            'estado': result[2], 
            'fecha_creacion': result[3]}
            data.append(content)
            content = {}
        return data

    def get_justificaciones(self):  
        rv = self.mysql_pool.execute("""SELECT J.id, J.descripcion, J.estado, 
                                        J.fecha_creacion from justificaciones J""")  
        data = []
        content = {}
        for result in rv:
            content = {'justificacion_id': result[0], 
                       'descripcion': result[1], 
                       'estado': result[2],
                       'fecha_creacion': result[3]
                       }
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, descripcion, estado, fecha_creacion):    
        data = {
            'descripcion' :descripcion,
            'estado' : estado,
            'fecha_creacion' : fecha_creacion,
        }  
        query = """insert into justificaciones (descripcion, estado, fecha_creacion) 
            values (%(descripcion)s, %(estado)s, %(fecha_creacion)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_justificacion(self, justificacion_id):    
        params = {'justificacion_id' : justificacion_id}      
        query = """delete from justificaciones where id = %(justificacion_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



    def update_justificacion(self, justificacion_id, descripcion, estado, fecha_creacion ):    
        params = {'justificacion_id' : justificacion_id,
                'descripcion' : descripcion,
                'estado' : estado,
                'fecha_creacion' : fecha_creacion,
        }      
        query = """update justificaciones set 
                    descripcion = %(descripcion)s,
                    estado = %(estado)s,
                    fecha_creacion =%(fecha_creacion)s
                    where id = %(justificacion_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
 
if __name__ == "__main__":    
    tm = justificacionsModel()