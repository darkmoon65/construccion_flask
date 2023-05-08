from backend.models.mysql_connection_pool import MySQLPool

class GruposModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_grupo(self, grupo_id):    
        params = {'grupo_id' : grupo_id}      
        rv = self.mysql_pool.execute("""SELECT G.categoria, C.nombre from grupos G 
                                        inner join cursos C on C.id = G.curso_id
                                        where G.id = %(grupo_id)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'categoria': result[0], 'nombre_curso': result[1]}
            data.append(content)
            content = {}
        return data

    def get_grupos(self):  
        rv = self.mysql_pool.execute("""SELECT G.categoria, C.nombre from grupos G 
                                        inner join cursos C on C.id = G.curso_id""")  
        data = []
        content = {}
        for result in rv:
            content = {'categoria': result[0], 'nombre_curso': result[1]}
            data.append(content)
            content = {}
        return data

    def create_grupo(self, curso_id, horario_id, categoria):    
        data = {
            'curso_id' : curso_id,
            'horario_id' : horario_id,
            'categoria' : categoria,
        }  
        query = """insert into grupos (curso_id, horario_id, categoria) 
            values (%(curso_id)s,%(horario_id)s,%(categoria)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data

    def delete_grupo(self, grupo_id):    
        params = {'grupo_id' : grupo_id}      
        query = """delete from grupos where id = %(grupo_id)s """    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


    def update_grupo(self, grupo_id, curso_id, horario_id, categoria):    
        data = {
            'grupo_id' : grupo_id,
            'curso_id' : curso_id,
            'horario_id' : horario_id,
            'categoria' : categoria,
        }  
        query = """update grupos set 
            curso_id = %(curso_id)s,
            horario_id = %(horario_id)s, 
            categoria = %(categoria)s 
            where id = %(grupo_id)s """    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id'] = cursor.lastrowid
        return data



if __name__ == "__main__":    
    tm = GruposModel()