import sqlite3

class conexionDb:
    def conectar (self):
        conexion= sqlite3.connect("Biblioteca.db")
        return conexion

    def altalibros (self,datos):
        cone = self.conectar()
        cursor = cone.cursor ()
        sql = "insert into Libros (Titulo, Autor, Edicion, Lugar_impresion, Editorial, Traduccion, Cantidad_paginas, Condicion, Fecha_devolucion) values (?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def modificalibros (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor ()
            sql = "update Libros set Titulo = ?, Autor = ?, Edicion = ? , Lugar_impresion = ?, Editorial = ?, Traduccion =?, Cantidad_paginas = ? , Condicion = ?, Fecha_devolucion = ? where codigo = ?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
    
    def consultalibros (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Titulo, Autor, Edicion , Lugar_impresion, Editorial, Traduccion, Cantidad_paginas, Condicion, Fecha_devolucion from Libros where codigo = ?" 
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def bajalibros (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "delete from Libros where codigo = ?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

            
    def consulta_por_titulo (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Codigo, Autor, Edicion , Lugar_impresion, Editorial, Traduccion, Cantidad_paginas, Condicion, Fecha_devolucion from Libros where Titulo = ?" 
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()
    
    
    def listarlibros (self,):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Codigo, Titulo,  Autor, Edicion , Lugar_impresion, Editorial, Traduccion, Cantidad_paginas, Condicion, Fecha_devolucion from Libros" 
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def altausuarios (self,datos):
        cone = self.conectar()
        cursor = cone.cursor ()
        sql = "insert into Usuarios (DNI, Nombre, Telefono, Mail) values (?,?,?,?)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def consultausuarios (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Nombre, Telefono, Mail from Usuarios where DNI = ?" 
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def modificausuarios (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor ()
            sql = "update Usuarios set Nombre = ?, Telefono = ?, Mail = ?  where DNI = ?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

    def bajausuarios (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "delete from Usuarios where DNI = ?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
    
    
    # metodos para conectar con las distintas bases para registrar el movimiento

    def consultaprestamo1 (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Titulo, Condicion from Libros  where codigo = ?" 
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def altamovimientos (self,datos):
        cone = self.conectar()
        cursor = cone.cursor ()
        sql = "insert into Movimientos  (Codigo_libro, Titulo, Condicion, DNI, Nombre, Telefono, Mail, Fecha_inicio, Fecha_devolucion) values (?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,datos)
        cone.commit()
 # Metodo para cambiar la condicion y fecha de devolucion en la tabla Libros       
    
    
    def modifica_condicion_libros (self,datos1):
        try:
            cone = self.conectar()
            cursor = cone.cursor ()
            sql = "update Libros set Condicion = ?, Fecha_devolucion = ? where Codigo = ?"
            cursor.execute(sql,datos1)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()    

# Metodo para consulta de devoluciones

    def consultamovimientos (self, datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Titulo, Condicion, DNI, Nombre, Telefono, Mail, fecha_inicio, fecha_devolucion from Movimientos  where Codigo_libro = ?" 
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()

# Metodos para registrar una devolucion y actualizar las tablas
    def modifica_libros_devolucion (self,datos1):
        cone = self.conectar()
        cursor = cone.cursor ()
        sql = "update Libros set Condicion = ?, Fecha_devolucion = ? where Codigo = ?"
        cursor.execute(sql,datos1)
        cone.commit()
        return cursor.rowcount
           
    def bajamovimiento (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "delete from Movimientos where Codigo_libro = ?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

    def listaretrasos (self,):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Codigo_libro, Titulo,  Condicion, DNI , Nombre, Telefono, Mail, Fecha_Inicio,  Fecha_Devolucion from Movimientos" 
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
    
    def modifica_retraso (self,datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor ()
            sql = "update Libros set Condicion = ? where Codigo = ?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()    