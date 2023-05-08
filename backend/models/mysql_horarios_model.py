from backend.models.mysql_connection_pool import MySQLPool

class HorariosModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_horario(self, horario_id):    
        params = {'horario_id' : horario_id}      
        rv = self.mysql_pool.execute("""SELECT H.id, H.dia, H.hora_inicio, H.hora_fin 
                                        from horarios H
                                        where H.id = %(horario_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'horario_id': result[0], 
                       'dia': result[1], 
                       'hora_inicio': result[2],
                       'hora_fin': result[3]}
            data.append(content)
            content = {}
        return data

    def get_horarios(self):  
        rv = self.mysql_pool.execute("""SELECT H.id, H.dia, H.hora_inicio, H.hora_fin 
                                        from horarios H""")  
        data = []
        content = {}
        for result in rv:
            content = {'horario_id': result[0], 
                       'dia': result[1], 
                       'hora_inicio': result[2],
                       'hora_fin': result[3]
                       }
            data.append(content)
            content = {}
        return data

    def create_horario(self, dia, hora_inicio, hora_fin):    
        data = {
            'dia' : dia,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
        }  
        query = """insert into horarios (dia, hora_inicio, hora_fin) 
            values (%(dia)s, %(hora_inicio)s, %(hora_fin)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_horario(self, horario_id):    
        params = {'horario_id' : horario_id}      
        query = """delete from horarios where id = %(horario_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



    def update_horario(self, horario_id, dia, hora_inicio,hora_fin ):    
        params = {'horario_id' : horario_id,
                'dia' : dia,
                'hora_inicio' : hora_inicio,
                'hora_fin' : hora_fin,
        }      
        query = """update horarios set 
                    dia = %(dia)s,
                    hora_inicio = %(hora_inicio)s,
                    hora_fin = %(hora_fin)s 
                    where id = %(horario_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
 
if __name__ == "__main__":    
    tm = UsuariosModel()