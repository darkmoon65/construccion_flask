from backend.models.mysql_connection_pool import MySQLPool

class AsistenciasModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_asistencia(self, asistencia_id):    
        params = {'asistencia_id' : asistencia_id}      
        rv = self.mysql_pool.execute("""SELECT A.id, A.estado, A.sesion_id from asistencias A
                                        where A.id = %(asistencia_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'asistencia_id': result[0], 'estado': result[1], 'sesion_id': result[2]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.mysql_pool.execute("""SELECT A.id, A.estado, A.sesion_id from asistencias A""")  
        data = []
        content = {}
        for result in rv:
            content = {'asistencia_id': result[0], 'estado': result[1], 'sesion_id': result[2]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, estado, sesion_id):    

        data = {
            'estado' : estado,
            'sesion_id' : sesion_id
        }
        query = """insert into asistencias (estado, sesion_id) 
            values (%(estado)s, %(sesion_id)s) """    
        cursor = self.mysql_pool.execute(query, data, commit=True)

        data['id'] = cursor.lastrowid
        return data

    def delete_asistencia(self, asistencia_id):    
        params = {'asistencia_id' : asistencia_id}      
        query = """delete from asistencias where id = %(asistencia_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def update_asistencia(self, asistencia_id,estado,sesion_id ):    
        data = {
            'asistencia_id': asistencia_id,
            'estado' : estado,
            'sesion_id' : dni
        }  
        query = """update asistencias set 
                    estado = %(estado)s,
                    sesion_id = %(sesion_id)s 
                    where id = %(asistencia_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
 
if __name__ == "__main__":    
    tm = AsistenciasModel()