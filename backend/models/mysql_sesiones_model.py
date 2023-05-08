from backend.models.mysql_connection_pool import MySQLPool

class SesionesModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_sesion(self, sesion_id):    
        params = {'sesion_id' : sesion_id}      
        rv = self.mysql_pool.execute("""SELECT S.id, S.fecha, S.hora, S.tema from sesiones S
                                        where S.id = %(sesion_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'sesion_id': result[0], 'fecha': result[1], 'hora': result[2], 'tema': result[2]}
            data.append(content)
            content = {}
        return data

    def get_sesiones(self):  
        rv = self.mysql_pool.execute("""SELECT S.id, S.fecha, S.hora, S.tema from sesiones S""")  
        data = []
        content = {}
        for result in rv:
            content = {'sesion_id': result[0], 'fecha': result[1], 'hora': result[2], 'tema': result[2]}
            data.append(content)
            content = {}
        return data

    def create_sesion(self, fecha, hora, tema, horario_id , justificacion_id):    

        data = {
            'fecha' : fecha,
            'hora' : hora,
            'tema' : tema,
            'horario_id' : horario_id,
            'justificacion_id' : justificacion_id
        }
        query = """insert into sesiones (fecha, hora, tema, horario_id, justificacion_id) 
            values (%(fecha)s, %(hora)s, %(tema)s, %(horario_id)s, %(justificacion_id)s) """    
        cursor = self.mysql_pool.execute(query, data, commit=True)

        data['id'] = cursor.lastrowid
        return data

    def delete_sesion(self, sesion_id):    
        params = {'sesion_id' : sesion_id}      
        query = """delete from sesiones where id = %(sesion_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def update_sesion(self,sesion_id, fecha, hora, tema, horario_id , justificacion_id):    
        data = {
            'sesion_id': sesion_id,
            'fecha' : fecha,
            'hora' : hora,
            'tema' : tema,
            'horario_id' : horario_id,
            'justificacion_id' : justificacion_id
        }  
        query = """update sesiones set 
                    fecha = %(fecha)s,
                    hora = %(hora)s,
                    fecha = %(fecha)s,
                    hora = %(hora)s,
                    fecha = %(fecha)s
                    where id = %(sesion_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
 
if __name__ == "__main__":    
    tm = SesionesModel()