import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import conexionDB as db
from tkinter import scrolledtext as st
import datetime
from datetime import date


class Biblioteca:
# En el init incluimos los menues
    def __init__(self):
        self.conexion = db.conexionDb ()
        self.ventana = tk.Tk ()
        self.ventana.title("SISTEMA DE ADMINISTRACION BIBLIOTECA")
        self.ventana.geometry ("800x800")
        menu1 = tk.Menu(self.ventana)
        self.ventana.config (menu = menu1)
        opciones1 = tk.Menu ( menu1, tearoff = 0 )
        opciones1.add_command (label= "Alta de Libros", command = self.formularioaltalibros)
        opciones1.add_command (label= "Modificar Datos de Libros", command = self.formulariomodificalibros)
        opciones1.add_command (label= "Baja de libros", command = self.formulariobajalibros)
        opciones1.add_separator()
        opciones1.add_command (label = "Consulta de Libros por Codigo", command = self.formularioconsultalibros1)# falta command
        opciones1.add_command (label= "Consulta de Libros por Titulo", command = self.formularioconsultalibros)
        opciones1.add_separator()
        opciones1.add_command (label= "Listado de libros", command = self.formulariolistado)
        opciones1.add_separator()
        opciones1.add_command (label = "Salir", command = self.salir)
        menu1.add_cascade (label ="Administracion de libros", menu = opciones1)
        opciones2 = tk.Menu (menu1, tearoff = 0)
        opciones2.add_command (label= "Alta de Usuarios", command = self.formularioaltausuarios)
        opciones2.add_separator()
        opciones2.add_command (label= "Modificar Datos Usuarios", command = self.formulariomodificausuarios)
        opciones2.add_command (label= "Baja de Usuarios", command = self.formulariobajausuarios)
        opciones2.add_separator()
        opciones2.add_command (label = "Salir", command = self.salir)
        menu1.add_cascade (label ="Administracion de Usuarios", menu = opciones2)
        opciones3 = tk.Menu (menu1, tearoff = 0)
        opciones3.add_command (label= "Prestamos", command = self.formularioaltamovimientos)
        opciones3.add_separator()
        opciones3.add_command (label= "Devoluciones", command = self.formulariobajamovimientos)
        opciones3.add_separator()
        opciones3.add_command (label = "Salir", command = self.salir)
        menu1.add_cascade (label ="Administracion de Movimientos", menu = opciones3)
        opciones4 = tk.Menu (menu1, tearoff = 0)
        opciones4.add_command (label= "Listado de Retrasos", command = self.formularioretraso)
        opciones4.add_separator()
        opciones4.add_command (label = "Salir", command = self.salir)
        menu1.add_cascade (label ="Administracion de Reclamos", menu = opciones4)
        
        
        
        self.ventana.mainloop()
    
 # formulario para dar de alta libros   
    
    def formularioaltalibros (self):
        self.ventana1 = tk.Toplevel(self.ventana)
        self.ventana1.title("Alta de Libros")
        self.ventana1.geometry ("600x600")
        self.label1 = tk.Label(self.ventana1, text = "Titulo" )
        self.label1.grid (column = 0, row = 0, padx=10, pady =10)
        self.titulo = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, textvariable = self.titulo, width = 40 )
        self.entry1.grid(column = 1, row = 0, padx=10, pady =10,)
        self.label2 = tk.Label(self.ventana1, text = "Autor")
        self.label2.grid (column = 0, row = 1, padx=10, pady = 10)
        self.autor = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, textvariable = self.autor, width = 30 )
        self.entry2.grid(column = 1, row = 1, padx=10, pady = 10)
        self.label3 = tk.Label(self.ventana1, text = "Edicion")
        self.label3.grid (column = 0, row = 2, padx=10, pady = 10)
        self.edicion = tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, textvariable = self.edicion )
        self.entry3.grid(column = 1, row = 2, padx=10, pady = 10)
        self.label4 = tk.Label(self.ventana1, text = "Lugar de Impresion")
        self.label4.grid (column = 0, row = 3, padx=10, pady = 10)
        self.lugar = tk.StringVar()
        self.entry4 = tk.Entry(self.ventana1, textvariable = self.lugar )
        self.entry4.grid(column = 1, row = 3, padx=10, pady = 10)
        self.label5 = tk.Label(self.ventana1, text = "Editorial")
        self.label5.grid (column = 0, row = 4, padx=10, pady = 10)
        self.editorial = tk.StringVar()
        self.entry5 = tk.Entry(self.ventana1, textvariable = self.editorial )
        self.entry5.grid(column = 1, row = 4, padx=10, pady = 10)
        self.label6 = tk.Label(self.ventana1, text = "Traducion (Si/No)")
        self.label6.grid (column = 0, row = 5, padx=10, pady = 10)
        self.traduccion = tk.StringVar()
        self.combo1 = ttk.Combobox(self.ventana1, textvariable = self.traduccion )
        self.combo1.grid(column = 1, row = 5, padx=10, pady = 10)
        self.combo1 ["values"] = ("Si", "No")
        self.label7 = tk.Label(self.ventana1, text = "Cantidad de Páginas")
        self.label7.grid (column = 0, row = 6, padx=10, pady = 10)
        self.cantidad = tk.StringVar()
        self.entry7 = tk.Entry(self.ventana1, textvariable = self.cantidad )
        self.entry7.grid(column = 1, row = 6, padx=10, pady = 10)
        self.label8 = tk.Label(self.ventana1, text = "Condición")
        self.label8.grid (column = 0, row = 7, padx=10, pady = 10)
        self.condicion = tk.StringVar()
        self.combo2 = ttk.Combobox(self.ventana1, textvariable = self.condicion )
        self.combo2.grid(column = 1, row = 7, padx=10, pady = 10)
        self.combo2 ["values"] = ("Prestado", "Disponible", "Retraso", "En restauración")
        self.label9 = tk.Label(self.ventana1, text = "Fecha de Devolución")
        self.label9.grid (column = 0, row = 8, padx=10, pady = 10)
        self.devolucion = tk.StringVar()
        self.entry9 = tk.Entry(self.ventana1, textvariable = self.devolucion )
        self.entry9.grid(column = 1, row = 8, padx=10, pady = 10)
        self.boton1 = tk.Button(self.ventana1, text = "Confirmar", command = self.altalibrosdb )# falta command
        self.boton1.grid (column = 1, row = 9, padx = 15, pady =15 )


# Operacion para dar de alta a los libros
    def altalibrosdb (self):
        aux = self.titulo.get()
        aux1 = aux.upper()
        self.titulo.set(aux1)         
        datos = (self.titulo.get(), self.autor.get(), self.edicion.get(), self.lugar.get(), self.editorial.get(), self.traduccion.get(),self.cantidad.get(), self.condicion.get(), self.devolucion.get())
        self.conexion.altalibros (datos)
        mb.showinfo ("INFORMACION!", "LOS DATOS FUERON CARGADOS!!!")
        self.titulo.set("")
        self.autor.set("")
        self.edicion.set("")
        self.lugar.set("")
        self.editorial.set("")
        self.traduccion.set("")
        self.cantidad.set("")
        self.condicion.set("")
        self.devolucion.set("")



#formulario para modificar datos de libros:

    def formulariomodificalibros (self):
        self.ventana2 = tk.Toplevel(self.ventana)
        self.ventana2.title("Modificacion Datos de Libros")
        self.ventana2.geometry ("600x600")
        self.labelcod = tk.Label (self.ventana2, text = "Codigo")
        self.labelcod.grid (column = 0, row = 0, padx=10, pady =10)
        self.codigomod = tk.StringVar()
        self.entrymod = tk.Entry(self.ventana2, textvariable = self.codigomod )
        self.entrymod.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelmod1 = tk.Label(self.ventana2, text = "Titulo" )
        self.labelmod1.grid (column = 0, row = 1, padx=10, pady =10)
        self.titulomod = tk.StringVar()
        self.entrymod1 = tk.Entry(self.ventana2, textvariable = self.titulomod, width = 40 )
        self.entrymod1.grid(column = 1, row = 1, padx=10, pady =10,)
        self.labelmod2 = tk.Label(self.ventana2, text = "Autor")
        self.labelmod2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.autormod = tk.StringVar()
        self.entrymod2 = tk.Entry(self.ventana2, textvariable = self.autormod, width = 30 )
        self.entrymod2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelmod3 = tk.Label(self.ventana2, text = "Edicion")
        self.labelmod3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.edicionmod = tk.StringVar()
        self.entrymod3 = tk.Entry(self.ventana2, textvariable = self.edicionmod )
        self.entrymod3.grid (column = 1, row = 3, padx=10, pady = 10)
        self.labelmod4 = tk.Label(self.ventana2, text = "Lugar de Impresion")
        self.labelmod4.grid (column = 0, row = 4, padx=10, pady = 10)
        self.lugarmod = tk.StringVar()
        self.entrymod4 = tk.Entry(self.ventana2, textvariable = self.lugarmod )
        self.entrymod4.grid(column = 1, row = 4, padx=10, pady = 10)
        self.labelmod5 = tk.Label(self.ventana2, text = "Editorial")
        self.labelmod5.grid (column = 0, row = 5, padx=10, pady = 10)
        self.editorialmod = tk.StringVar()
        self.entrymod5 = tk.Entry(self.ventana2, textvariable = self.editorialmod )
        self.entrymod5.grid(column = 1, row = 5, padx=10, pady = 10)
        self.labelmod6 = tk.Label(self.ventana2, text = "Traducion (Si/No)")
        self.labelmod6.grid (column = 0, row = 6, padx=10, pady = 10)
        self.traduccionmod = tk.StringVar()
        self.combomod1 = ttk.Combobox(self.ventana2, textvariable = self.traduccionmod )
        self.combomod1.grid(column = 1, row = 6, padx=10, pady = 10)
        self.combomod1 ["values"] = ("Si", "No")
        self.labelmod7 = tk.Label(self.ventana2, text = "Cantidad de Páginas")
        self.labelmod7.grid (column = 0, row = 7, padx=10, pady = 10)
        self.cantidadmod = tk.StringVar()
        self.entrymod7 = tk.Entry(self.ventana2, textvariable = self.cantidadmod )
        self.entrymod7.grid(column = 1, row = 7, padx=10, pady = 10)
        self.labelmod8 = tk.Label(self.ventana2, text = "Condición")
        self.labelmod8.grid (column = 0, row = 8, padx=10, pady = 10)
        self.condicionmod = tk.StringVar()
        self.combomod2 = ttk.Combobox(self.ventana2, textvariable = self.condicionmod )
        self.combomod2.grid(column = 1, row = 8, padx=10, pady = 10)
        self.combomod2 ["values"] = ("Prestado", "Disponible", "Retraso", "En restauración")
        self.labelmod9 = tk.Label(self.ventana2, text = "Fecha de Devolución")
        self.labelmod9.grid (column = 0, row = 9, padx=10, pady = 10)
        self.devolucionmod = tk.StringVar()
        self.entrymod9 = tk.Entry(self.ventana2, textvariable = self.devolucionmod )
        self.entrymod9.grid(column = 1, row = 9, padx=10, pady = 10)
        self.botonmod1 = tk.Button(self.ventana2, text = "Consultar", command = self.consulta_mod )
        self.botonmod1.grid (column = 1, row = 10, padx = 15, pady =15 )
        self.botonmod2 = tk.Button(self.ventana2, text = "Modificar", command = self.modificadb )
        self.botonmod2.grid (column = 1, row = 11, padx = 15, pady =15 )

# metodo para consultar y luego modificar

    def consulta_mod (self):
        datos = (self.codigomod.get(), )
        respuesta = self.conexion.consultalibros (datos)
        if len (respuesta)>0:
            self.titulomod.set(respuesta [0][0])
            self.autormod.set(respuesta[0][1])
            self.edicionmod.set(respuesta[0][2])
            self.lugarmod.set(respuesta [0][3])
            self.editorialmod.set(respuesta[0][4])
            self.traduccionmod.set(respuesta[0][5])
            self.cantidadmod.set(respuesta[0][6])
            self.condicionmod.set(respuesta[0][7])
            self.devolucionmod.set(respuesta[0][8])
        else:
            self.titulomod.set("")
            self.autormod.set("")
            self.edicionmod.set("")
            self.lugarmod.set("")
            self.editorialmod.set("")
            self.traduccionmod.set("")
            self.cantidadmod.set("")
            self.condicionmod.set("")
            self.devolucionmod.set("")
            mb.showinfo("Informacion!", "No existe un Libro con ese Codigo")
# Metodo para hacer modificaciones

    def modificadb (self):
        datos = (self.titulomod.get(), self.autormod.get(), self.edicionmod.get(), self.lugarmod.get(), self.editorialmod.get(), self.traduccionmod.get(),self.cantidadmod.get(), self.condicionmod.get(), self.devolucionmod.get(),self.codigomod.get())
        cantidad = self.conexion.modificalibros(datos)
        if cantidad == 1:
            mb.showinfo ("INFORMACION !!", "EL LIBRO FUE MODIFICADO")
        else:
            mb.showinfo("Informacion!!","No existe un Libro con ese Codigo")
# Metodo para hacer el formulario de Bajas

    def formulariobajalibros (self):
        self.ventana3 = tk.Toplevel(self.ventana)
        self.ventana3.title("Baja de Libros")
        self.ventana3.geometry ("600x600")
        self.labelcodbaja = tk.Label (self.ventana3, text = "Codigo")
        self.labelcodbaja.grid (column = 0, row = 0, padx=10, pady =10)
        self.codigobaja = tk.StringVar()
        self.entrybaja = tk.Entry(self.ventana3, textvariable = self.codigobaja )
        self.entrybaja.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelbaja1 = tk.Label(self.ventana3, text = "Titulo" )
        self.labelbaja1.grid (column = 0, row = 1, padx=10, pady =10)
        self.titulobaja = tk.StringVar()
        self.entrybaja1 = tk.Entry(self.ventana3, textvariable = self.titulobaja, width = 40, state= "readonly" )
        self.entrybaja1.grid(column = 1, row = 1, padx=10, pady =10,)
        self.labelbaja2 = tk.Label(self.ventana3, text = "Autor")
        self.labelbaja2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.autorbaja = tk.StringVar()
        self.entrybaja2 = tk.Entry(self.ventana3, textvariable = self.autorbaja, width = 30, state = "readonly" )
        self.entrybaja2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelbaja3 = tk.Label(self.ventana3, text = "Edicion")
        self.labelbaja3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.edicionbaja = tk.StringVar()
        self.entrybaja3 = tk.Entry(self.ventana3, textvariable = self.edicionbaja, state= "readonly" )
        self.entrybaja3.grid (column = 1, row = 3, padx=10, pady = 10)
        self.labelbaja4 = tk.Label(self.ventana3, text = "Lugar de Impresion")
        self.labelbaja4.grid (column = 0, row = 4, padx=10, pady = 10)
        self.lugarbaja = tk.StringVar()
        self.entrybaja4 = tk.Entry(self.ventana3, textvariable = self.lugarbaja, state = "readonly" )
        self.entrybaja4.grid(column = 1, row = 4, padx=10, pady = 10)
        self.labelbaja5 = tk.Label(self.ventana3, text = "Editorial")
        self.labelbaja5.grid (column = 0, row = 5, padx=10, pady = 10)
        self.editorialbaja = tk.StringVar()
        self.entrybaja5 = tk.Entry(self.ventana3, textvariable = self.editorialbaja,  state = "readonly")
        self.entrybaja5.grid(column = 1, row = 5, padx=10, pady = 10)
        self.labelbaja6 = tk.Label(self.ventana3, text = "Traducion (Si/No)")
        self.labelbaja6.grid (column = 0, row = 6, padx=10, pady = 10)
        self.traduccionbaja = tk.StringVar()
        self.entrybaja6= tk.Entry(self.ventana3, textvariable = self.traduccionbaja, state = "readonly" )
        self.entrybaja6.grid(column = 1, row = 6, padx=10, pady = 10)
        self.labelbaja7 = tk.Label(self.ventana3, text = "Cantidad de Páginas")
        self.labelbaja7.grid (column = 0, row = 7, padx=10, pady = 10)
        self.cantidadbaja = tk.StringVar()
        self.entrybaja7 = tk.Entry(self.ventana3, textvariable = self.cantidadbaja, state = "readonly" )
        self.entrybaja7.grid(column = 1, row = 7, padx=10, pady = 10)
        self.labelbaja8 = tk.Label(self.ventana3, text = "Condición")
        self.labelbaja8.grid (column = 0, row = 8, padx=10, pady = 10)
        self.condicionbaja = tk.StringVar()
        self.entrybaja8 = tk.Entry(self.ventana3, textvariable = self.condicionbaja, state = "readonly" )
        self.entrybaja8.grid(column = 1, row = 8, padx=10, pady = 10)
        self.labelbaja9 = tk.Label(self.ventana3, text = "Fecha de Devolución")
        self.labelbaja9.grid (column = 0, row = 9, padx=10, pady = 10)
        self.devolucionbaja = tk.StringVar()
        self.entrybaja9 = tk.Entry(self.ventana3, textvariable = self.devolucionbaja, state = "readonly"  )
        self.entrybaja9.grid(column = 1, row = 9, padx=10, pady = 10)
        self.botonbaja1 = tk.Button(self.ventana3, text = "Consultar Baja", command = self.consulta_baja )
        self.botonbaja1.grid (column = 1, row = 10, padx = 15, pady =15 )
        self.botonbaja2 = tk.Button(self.ventana3, text = "Eliminar", command = self.bajadb)
        self.botonbaja2.grid (column = 1, row = 11, padx = 15, pady =15 )

# metodos para dar de baja a un libro

    def consulta_baja (self):
        datos = (self.codigobaja.get(), )
        respuesta = self.conexion.consultalibros (datos)
        if len (respuesta)>0:
            self.titulobaja.set(respuesta [0][0])
            self.autorbaja.set(respuesta[0][1])
            self.edicionbaja.set(respuesta[0][2])
            self.lugarbaja.set(respuesta [0][3])
            self.editorialbaja.set(respuesta[0][4])
            self.traduccionbaja.set(respuesta[0][5])
            self.cantidadbaja.set(respuesta[0][6])
            self.condicionbaja.set(respuesta[0][7])
            self.devolucionbaja.set(respuesta[0][8])
        else:
            self.titulobaja.set("")
            self.autorbaja.set("")
            self.edicionbaja.set("")
            self.lugarbaja.set("")
            self.editorialbaja.set("")
            self.traduccionbaja.set("")
            self.cantidadbaja.set("")
            self.condicionbaja.set("")
            self.devolucionbaja.set("")
            mb.showinfo("Informacion!!","No existe un Libro con ese Codigo")

    def bajadb (self):
        pregunta = mb.askyesno("Confirma la Baja del Libro?")
        if pregunta == False:
            pregunta = self.formulariobajalibros()
        else:
            datos = (self.codigobaja.get(), )
            cantidad = self.conexion.bajalibros(datos)  
            if cantidad == 1:
                mb.showinfo ("Informacion!!","El libro fue eliminado")  
            else:
                mb.showinfo("Informacion!!","No existe un Libro con ese Codigo")

# Formulario para hacer consultas

    def formularioconsultalibros (self):
        self.ventana4 = tk.Toplevel(self.ventana)
        self.ventana4.title("Consulta de Libros")
        self.ventana4.geometry ("600x600")
        self.labelcodconsulta = tk.Label (self.ventana4, text = "Codigo")
        self.labelcodconsulta.grid (column = 0, row = 0, padx=10, pady =10)
        self.codigoconsulta = tk.StringVar()
        self.entryconsulta = tk.Entry(self.ventana4, textvariable = self.codigoconsulta, state = "readonly" )
        self.entryconsulta.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelconsulta1 = tk.Label(self.ventana4, text = "Titulo" )
        self.labelconsulta1.grid (column = 0, row = 1, padx=10, pady =10)
        self.tituloconsulta = tk.StringVar()
        self.entryconsulta1 = tk.Entry(self.ventana4, textvariable = self.tituloconsulta, width = 40 )
        self.entryconsulta1.grid(column = 1, row = 1, padx=10, pady =10,)
        self.labelconsulta2 = tk.Label(self.ventana4, text = "Autor")
        self.labelconsulta2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.autorconsulta = tk.StringVar()
        self.entryconsulta2 = tk.Entry(self.ventana4, textvariable = self.autorconsulta, width = 30, state = "readonly" )
        self.entryconsulta2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelconsulta3 = tk.Label(self.ventana4, text = "Edicion")
        self.labelconsulta3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.edicionconsulta = tk.StringVar()
        self.entryconsulta3 = tk.Entry(self.ventana4, textvariable = self.edicionconsulta, state= "readonly" )
        self.entryconsulta3.grid (column = 1, row = 3, padx=10, pady = 10)
        self.labelconsulta4 = tk.Label(self.ventana4, text = "Lugar de Impresion")
        self.labelconsulta4.grid (column = 0, row = 4, padx=10, pady = 10)
        self.lugarconsulta = tk.StringVar()
        self.entryconsulta4 = tk.Entry(self.ventana4, textvariable = self.lugarconsulta, state = "readonly" )
        self.entryconsulta4.grid(column = 1, row = 4, padx=10, pady = 10)
        self.labelconsulta5 = tk.Label(self.ventana4, text = "Editorial")
        self.labelconsulta5.grid (column = 0, row = 5, padx=10, pady = 10)
        self.editorialconsulta = tk.StringVar()
        self.entryconsulta5 = tk.Entry(self.ventana4, textvariable = self.editorialconsulta,  state = "readonly")
        self.entryconsulta5.grid(column = 1, row = 5, padx=10, pady = 10)
        self.labelconsulta6 = tk.Label(self.ventana4, text = "Traducion (Si/No)")
        self.labelconsulta6.grid (column = 0, row = 6, padx=10, pady = 10)
        self.traduccionconsulta = tk.StringVar()
        self.entryconsulta6= tk.Entry(self.ventana4, textvariable = self.traduccionconsulta, state = "readonly" )
        self.entryconsulta6.grid(column = 1, row = 6, padx=10, pady = 10)
        self.labelconsulta7 = tk.Label(self.ventana4, text = "Cantidad de Páginas")
        self.labelconsulta7.grid (column = 0, row = 7, padx=10, pady = 10)
        self.cantidadconsulta = tk.StringVar()
        self.entryconsulta7 = tk.Entry(self.ventana4, textvariable = self.cantidadconsulta, state = "readonly" )
        self.entryconsulta7.grid(column = 1, row = 7, padx=10, pady = 10)
        self.labelconsulta8 = tk.Label(self.ventana4, text = "Condición")
        self.labelconsulta8.grid (column = 0, row = 8, padx=10, pady = 10)
        self.condicionconsulta = tk.StringVar()
        self.entryconsulta8 = tk.Entry(self.ventana4, textvariable = self.condicionconsulta, state = "readonly" )
        self.entryconsulta8.grid(column = 1, row = 8, padx=10, pady = 10)
        self.labelconsulta9 = tk.Label(self.ventana4, text = "Fecha de Devolución")
        self.labelconsulta9.grid (column = 0, row = 9, padx=10, pady = 10)
        self.devolucionconsulta = tk.StringVar()
        self.entryconsulta9 = tk.Entry(self.ventana4, textvariable = self.devolucionconsulta, state = "readonly"  )
        self.entryconsulta9.grid(column = 1, row = 9, padx=10, pady = 10)
        self.botonconsulta = tk.Button(self.ventana4, text = "Consultar", command = self.consultadb )
        self.botonconsulta.grid (column = 1, row =10, padx = 20, pady = 20)
        
# Metodo para hacer operativa la consulta

    def consultadb (self):
        aux = self.tituloconsulta.get()
        aux1 = aux.upper()
        self.tituloconsulta.set (aux1)
        datos = (self.tituloconsulta.get(), )
        respuesta = self.conexion.consulta_por_titulo (datos)
        if len (respuesta)>0:
            self.codigoconsulta.set(respuesta [0][0])
            self.autorconsulta.set(respuesta[0][1])
            self.edicionconsulta.set(respuesta[0][2])
            self.lugarconsulta.set(respuesta [0][3])
            self.editorialconsulta.set(respuesta[0][4])
            self.traduccionconsulta.set(respuesta[0][5])
            self.cantidadconsulta.set(respuesta[0][6])
            self.condicionconsulta.set(respuesta[0][7])
            self.devolucionconsulta.set(respuesta[0][8])
        else:
            self.codigoconsulta.set("")
            self.autorconsulta.set("")
            self.edicionconsulta.set("")
            self.lugarconsulta.set("")
            self.editorialconsulta.set("")
            self.traduccionconsulta.set("")
            self.cantidadconsulta.set("")
            self.condicionconsulta.set("")
            self.devolucionconsulta.set("")
            mb.showinfo("Informacion!!","No existe un Libro con ese Codigo")

# formulario para listado

    def formulariolistado (self):
        self.ventana5 = tk.Toplevel(self.ventana)
        self.ventana5.title("Listado completo de Libros")
        self.ventana5.geometry ("800x800")
        self.botonlistado = tk.Button(self.ventana5, text = "Listado de Libros", command = self.listadodb )
        self.botonlistado.grid (column = 0, row =0, padx = 20, pady = 20)
        self.scroll = st.ScrolledText(self.ventana5, width =80, height = 60)
        self.scroll.grid (column = 0 , row = 1, padx= 10, pady = 10)

# Metodo para hacer el listado

    def listadodb (self):
        respuesta = self.conexion.listarlibros()
        self.scroll.delete("1.0", tk.END)
        for fila in respuesta:
            self.scroll.insert (tk.END, "Codigo:  " + str (fila [0])+ "\nTitulo: " + str (fila [1]) +"\nAutor:  " + str (fila [ 2])+"\nEdicion:  " + str (fila [3])+ "\nLugar de Impresion:  " + str (fila [4])+ "\nEditorial:  " + str (fila [5])+"\nTraduccion:  " + str (fila [6])+ "\nPaginas:  " + str (fila [7])+"\nCondicion:  " + str (fila [8])+  "\nDevolucion:  " + str (fila [9])+ "\n\n\n")

# Metodo para salir
    def salir (self):
        ventana= quit()

# metodo grafico para dar de alta un usuario

    def formularioaltausuarios (self):
        self.ventana6 = tk.Toplevel(self.ventana)
        self.ventana6.title("Alta de Usuarios")
        self.ventana6.geometry ("400x400")
        self.labelusuario = tk.Label(self.ventana6, text = "DNI" )
        self.labelusuario.grid (column = 0, row = 0, padx=10, pady =10)
        self.documento = tk.StringVar()
        self.entryusuario = tk.Entry(self.ventana6, textvariable = self.documento )
        self.entryusuario.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelusuario1 = tk.Label(self.ventana6, text = "Nombre Completo")
        self.labelusuario1.grid (column = 0, row = 1, padx=10, pady = 10)
        self.nombre = tk.StringVar()
        self.entryusuario1 = tk.Entry(self.ventana6, textvariable = self.nombre, width = 40 )
        self.entryusuario1.grid(column = 1, row = 1, padx=10, pady = 10)
        self.labelusuario2 = tk.Label(self.ventana6, text = "Telefono")
        self.labelusuario2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.telefono = tk.StringVar()
        self.entryusuario2 = tk.Entry(self.ventana6, textvariable = self.telefono )
        self.entryusuario2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelusuario3 = tk.Label(self.ventana6, text = "Correo Electronico")
        self.labelusuario3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.mail = tk.StringVar()
        self.entryusuario3 = tk.Entry(self.ventana6, textvariable = self.mail )
        self.entryusuario3.grid(column = 1, row = 3, padx=10, pady = 10)
        self.botonusuario = tk.Button(self.ventana6, text = "Agregar usuario", command= self.altausuariosdb )
        self.botonusuario.grid (column = 1, row =10, padx = 20, pady = 20)


# metodo para dar de alta un usuario

    def altausuariosdb (self):
        datos = (self.documento.get(), self.nombre.get(), self.telefono.get(), self.mail.get() )
        self.conexion.altausuarios (datos)
        mb.showinfo ( "Informacion!!","LOS DATOS FUERON CARGADOS!!!")
        self.documento.set("")
        self.nombre.set("")
        self.telefono.set("")
        self.mail.set("")
        
# Metodo para Interfaz Grafica Modificacion de datos de usuario

    def formulariomodificausuarios (self):
        self.ventana7 = tk.Toplevel(self.ventana)
        self.ventana7.title("Modificacion de datos de Usuarios")
        self.ventana7.geometry ("400x400")
        self.labelusuariomod = tk.Label(self.ventana7, text = "DNI" )
        self.labelusuariomod.grid (column = 0, row = 0, padx=10, pady =10)
        self.documentomod = tk.StringVar()
        self.entryusuariomod = tk.Entry(self.ventana7, textvariable = self.documentomod )
        self.entryusuariomod.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelusuariomod1 = tk.Label(self.ventana7, text = "Nombre Completo")
        self.labelusuariomod1.grid (column = 0, row = 1, padx=10, pady = 10)
        self.nombremod = tk.StringVar()
        self.entryusuariomod1 = tk.Entry(self.ventana7, textvariable = self.nombremod, width = 30 )
        self.entryusuariomod1.grid(column = 1, row = 1, padx=10, pady = 10)
        self.labelusuariomod2 = tk.Label(self.ventana7, text = "Telefono")
        self.labelusuariomod2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.telefonomod = tk.StringVar()
        self.entryusuariomod2 = tk.Entry(self.ventana7, textvariable = self.telefonomod )
        self.entryusuariomod2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelusuariomod3 = tk.Label(self.ventana7, text = "Correo Electronico")
        self.labelusuariomod3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.mailmod = tk.StringVar()
        self.entryusuariomod3 = tk.Entry(self.ventana7, textvariable = self.mailmod )
        self.entryusuariomod3.grid(column = 1, row = 3, padx=10, pady = 10)
        self.botonusuariomod = tk.Button(self.ventana7, text = "Consultar usuario", command = self.consulta_usuarios_mod )
        self.botonusuariomod.grid (column = 1, row =4, padx = 20, pady = 20)
        self.botonusuariomod1 = tk.Button(self.ventana7, text = "Modificar usuario", command= self.modifica_usuarios_db )
        self.botonusuariomod1.grid (column = 1, row =5, padx = 20, pady = 20)

# Metodos operativos para hacer modificaciones de usuario:

    def consulta_usuarios_mod (self):
        datos = (self.documentomod.get(), )
        respuesta = self.conexion.consultausuarios (datos)
        if len (respuesta)>0:
            self.nombremod.set(respuesta [0][0])
            self.telefonomod.set(respuesta[0][1])
            self.mailmod.set(respuesta[0][2])
            
        else:
            self.documentomod.set("")
            self.nombremod.set("")
            self.telefonomod.set("")
            self.mailmod.set("")
            mb.showinfo("Informacion!!","El Usuario no existe!!!")
# Metodo para hacer modificaciones

    def modifica_usuarios_db (self):
        datos = (self.nombremod.get(), self.telefonomod.get(), self.mailmod.get(), self.documentomod.get())
        cantidad = self.conexion.modificausuarios(datos)
        if cantidad == 1:
            mb.showinfo ("INFORMACION !!", "EL USUARIO FUE MODIFICADO")
        else:
            mb.showinfo("Informacion!!","El usuario no existe!!")

# Metodo para interfaz Grafica Baja de usuario

    def formulariobajausuarios (self):
        self.ventana8 = tk.Toplevel(self.ventana)
        self.ventana8.title("Baja de Usuarios")
        self.ventana8.geometry ("400x400")
        self.labelusuariobaja = tk.Label(self.ventana8, text = "DNI" )
        self.labelusuariobaja.grid (column = 0, row = 0, padx=10, pady =10)
        self.documentobaja = tk.StringVar()
        self.entryusuariobaja = tk.Entry(self.ventana8, textvariable = self.documentobaja )
        self.entryusuariobaja.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelusuariobaja1 = tk.Label(self.ventana8, text = "Nombre Completo")
        self.labelusuariobaja1.grid (column = 0, row = 1, padx=10, pady = 10)
        self.nombrebaja = tk.StringVar()
        self.entryusuariobaja1 = tk.Entry(self.ventana8, textvariable = self.nombrebaja, width = 30, state ="readonly" )
        self.entryusuariobaja1.grid(column = 1, row = 1, padx=10, pady = 10)
        self.labelusuariobaja2 = tk.Label(self.ventana8, text = "Telefono")
        self.labelusuariobaja2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.telefonobaja = tk.StringVar()
        self.entryusuariobaja2 = tk.Entry(self.ventana8, textvariable = self.telefonobaja, state="readonly" )
        self.entryusuariobaja2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelusuariobaja3 = tk.Label(self.ventana8, text = "Correo Electronico")
        self.labelusuariobaja3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.mailbaja = tk.StringVar()
        self.entryusuariobaja3 = tk.Entry(self.ventana8, textvariable = self.mailbaja, state = "readonly" )
        self.entryusuariobaja3.grid(column = 1, row = 3, padx=10, pady = 10)
        self.botonusuariobaja = tk.Button(self.ventana8, text = "Consultar usuario", command = self.consulta_baja_usuarios ) 
        self.botonusuariobaja.grid (column = 1, row =4, padx = 20, pady = 20)
        self.botonusuariobaja1 = tk.Button(self.ventana8, text = "Eliminar usuario", command = self.bajausuariosdb )
        self.botonusuariobaja1.grid (column = 1, row =5, padx = 20, pady = 20)

# METODO PARA HACER OPERATIVO LA baja de usuarios
    def consulta_baja_usuarios (self):
        datos = (self.documentobaja.get(), )
        respuesta = self.conexion.consultausuarios (datos)
        if len (respuesta)>0:
            self.nombrebaja.set(respuesta [0][0])
            self.telefonobaja.set(respuesta[0][1])
            self.mailbaja.set(respuesta[0][2])
            
        else:
            self.documentobaja.set("")
            self.nombrebaja.set("")
            self.telefonobaja.set("")
            self.mailbaja.set("")
            mb.showinfo("Informacion!!","El Usuario no existe!!!")
            

    def bajausuariosdb (self):
        pregunta = mb.askyesno("Confirma la Baja del Usuario?")
        if pregunta == False:
            pregunta = self.formulariobajausuarios()
        else:
            datos = (self.documentobaja.get(), )
            cantidad = self.conexion.bajausuarios(datos)  
            if cantidad == 1:
                mb.showinfo ("Informacion","El Usuario fue eliminado")  
            else:
                mb.showinfo("Informacion","No existe un Usuario con ese Documento")

# Metodo para la interfaz grafica de ingreso de prestamos

    def formularioaltamovimientos (self):
        self.ventana9 = tk.Toplevel(self.ventana)
        self.ventana9.title("Registro de Prestamos")
        self.ventana9.geometry ("600x600")
        self.labelprestamo = tk.Label (self.ventana9, text = "Codigo Libro")
        self.labelprestamo.grid (column = 0, row = 0, padx=10, pady =10)
        self.codigoprestamo = tk.StringVar()
        self.entryprestamo = tk.Entry(self.ventana9, textvariable = self.codigoprestamo )
        self.entryprestamo.grid(column = 1, row = 0, padx=10, pady =10)
        self.botonprestamo = tk.Button (self.ventana9, text = "Verificar Libros", command = self.consultaprestamolibro)#Falta command
        self.botonprestamo.grid (column = 2, row = 0, padx = 10, pady=10)
        self.labelprestamo1 = tk.Label(self.ventana9, text = "Titulo" )
        self.labelprestamo1.grid (column = 0, row = 1, padx=10, pady =10)
        self.tituloprestamo = tk.StringVar()
        self.entryprestamo1 = tk.Entry(self.ventana9, textvariable = self.tituloprestamo, width = 40, state = "readonly" )
        self.entryprestamo1.grid(column = 1, row = 1, padx=10, pady =10,)
        self.labelprestamo2 = tk.Label(self.ventana9, text = "Condicion")
        self.labelprestamo2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.condicionprestamo = tk.StringVar()
        self.entryprestamo2 = tk.Entry(self.ventana9, textvariable = self.condicionprestamo, state = "readonly" )
        self.entryprestamo2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelprestamo3 = tk.Label(self.ventana9, text = "Documento")
        self.labelprestamo3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.documentoprestamo = tk.StringVar()
        self.entryprestamo3 = tk.Entry(self.ventana9, textvariable = self.documentoprestamo )
        self.entryprestamo3.grid (column = 1, row = 3, padx=10, pady = 10)
        self.botonprestamo1 = tk.Button (self.ventana9, text = "Verificar Usuario", command = self.consultaprestamousuario)
        self.botonprestamo1.grid (column = 2, row = 3, padx = 10, pady=10)
        self.labelprestamo4 = tk.Label(self.ventana9, text = "Nombre")
        self.labelprestamo4.grid (column = 0, row = 4, padx=10, pady = 10)
        self.nombreprestamo = tk.StringVar()
        self.entryprestamo4 = tk.Entry(self.ventana9, textvariable = self.nombreprestamo, state = "readonly", width = 30 )
        self.entryprestamo4.grid(column = 1, row = 4, padx=10, pady = 10)
        self.labelprestamo5 = tk.Label(self.ventana9, text = "Telefono")
        self.labelprestamo5.grid (column = 0, row = 5, padx=10, pady = 10)
        self.telefonoprestamo = tk.StringVar()
        self.entryprestamo5 = tk.Entry(self.ventana9, textvariable = self.telefonoprestamo,  state = "readonly")
        self.entryprestamo5.grid(column = 1, row = 5, padx=10, pady = 10)
        self.labelprestamo6 = tk.Label(self.ventana9, text = "Correo Electronico")
        self.labelprestamo6.grid (column = 0, row = 6, padx=10, pady = 10)
        self.mailprestamo = tk.StringVar()
        self.entryprestamo6= tk.Entry(self.ventana9, textvariable = self.mailprestamo, state = "readonly", width = 30 )
        self.entryprestamo6.grid(column = 1, row = 6, padx=10, pady = 10)
        self.labelprestamo7 = tk.Label(self.ventana9, text = "Fecha de Inicio (dd-mm-yyyy)")
        self.labelprestamo7.grid (column = 0, row = 7, padx=10, pady = 10)
        self.inicioprestamo = tk.StringVar()
        self.entryprestamo7 = tk.Entry(self.ventana9, textvariable = self.inicioprestamo )
        self.entryprestamo7.grid(column = 1, row = 7, padx=10, pady = 10)
        self.labelprestamo8 = tk.Label(self.ventana9, text = "Fecha de Finalizacion (dd-mm-yyyy)")
        self.labelprestamo8.grid (column = 0, row = 8, padx=10, pady = 10)
        self.finalprestamo = tk.StringVar()
        self.entryprestamo8 = tk.Entry(self.ventana9, textvariable = self.finalprestamo )
        self.entryprestamo8.grid(column = 1, row = 8, padx=10, pady = 10)
        self.botonprestamo2 = tk.Button(self.ventana9, text = "Registrar Prestamo", command= self.altaprestamodb ) # Falta Command
        self.botonprestamo2.grid (column = 1, row =10, padx = 20, pady = 20)

 # Metodos para registrar un prestamo   
    
    
    def consultaprestamolibro (self):
        datos = (self.codigoprestamo.get(), )
        respuesta = self.conexion.consultaprestamo1 (datos)
        if len (respuesta)>0:
            self.tituloprestamo.set(respuesta [0][0])
            self.condicionprestamo.set(respuesta[0][1])
        else:
            mb.showinfo("Informacion","El libro no existe")
        condicion = self.condicionprestamo.get()
        if condicion != "Disponible":
            mb.showinfo ("Informacion","El libro no está Disponible")

    def consultaprestamousuario (self):
        datos = (self.documentoprestamo.get(), )
        respuesta = self.conexion.consultausuarios (datos)
        if len (respuesta)>0:
            self.nombreprestamo.set(respuesta [0][0])
            self.telefonoprestamo.set(respuesta[0][1])
            self.mailprestamo.set(respuesta[0][2])

    def altaprestamodb (self):
        self.condicionprestamo.set("En Curso")
        datos = (self.codigoprestamo.get(), self.tituloprestamo.get(), self.condicionprestamo.get(), self.documentoprestamo.get(), self.nombreprestamo.get(), self.telefonoprestamo.get(), self.mailprestamo.get(), self.inicioprestamo.get(), self.finalprestamo.get())
        self.conexion.altamovimientos (datos)
        mb.showinfo ( "Informacion", "Prestamo registrado!!")
            
        self.condicionprestamo.set("Prestado")
        datos1=(self.condicionprestamo.get(), self.finalprestamo.get(), self.codigoprestamo.get())
        self.conexion.modifica_condicion_libros(datos1)
  
  
  #Formulario para registrar devoluciones
       
    def formulariobajamovimientos (self):
        self.ventana10 = tk.Toplevel(self.ventana)
        self.ventana10.title("Devoluciones")
        self.ventana10.geometry ("600x600")
        self.labeldevolucion = tk.Label (self.ventana10, text = "Codigo Libro")
        self.labeldevolucion.grid (column = 0, row = 0, padx=10, pady =10)
        self.codigodevolucion = tk.StringVar()
        self.entrydevolucion = tk.Entry(self.ventana10, textvariable = self.codigodevolucion )
        self.entrydevolucion.grid(column = 1, row = 0, padx=10, pady =10)
        self.labeldevolucion1 = tk.Label(self.ventana10, text = "Titulo" )
        self.labeldevolucion1.grid (column = 0, row = 1, padx=10, pady =10)
        self.titulodevolucion = tk.StringVar()
        self.entrydevolucion1 = tk.Entry(self.ventana10, textvariable = self.titulodevolucion, width = 40, state = "readonly" )
        self.entrydevolucion1.grid(column = 1, row = 1, padx=10, pady =10,)
        self.labeldevolucion2 = tk.Label(self.ventana10, text = "Condicion")
        self.labeldevolucion2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.condiciondevolucion = tk.StringVar()
        self.entrydevolucion2 = tk.Entry(self.ventana10, textvariable = self.condiciondevolucion, state = "readonly" )
        self.entrydevolucion2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labeldevolucion3 = tk.Label(self.ventana10, text = "Documento")
        self.labeldevolucion3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.documentodevolucion = tk.StringVar()
        self.entrydevolucion3 = tk.Entry(self.ventana10, textvariable = self.documentodevolucion, state="readonly" )
        self.entrydevolucion3.grid (column = 1, row = 3, padx=10, pady = 10)
        self.labeldevolucion4 = tk.Label(self.ventana10, text = "Nombre")
        self.labeldevolucion4.grid (column = 0, row = 4, padx=10, pady = 10)
        self.nombredevolucion = tk.StringVar()
        self.entrydevolucion4 = tk.Entry(self.ventana10, textvariable = self.nombredevolucion, state = "readonly", width = 30 )
        self.entrydevolucion4.grid(column = 1, row = 4, padx=10, pady = 10)
        self.labeldevolucion5 = tk.Label(self.ventana10, text = "Telefono")
        self.labeldevolucion5.grid (column = 0, row = 5, padx=10, pady = 10)
        self.telefonodevolucion = tk.StringVar()
        self.entrydevolucion5 = tk.Entry(self.ventana10, textvariable = self.telefonodevolucion,  state = "readonly")
        self.entrydevolucion5.grid(column = 1, row = 5, padx=10, pady = 10)
        self.labeldevolucion6 = tk.Label(self.ventana10, text = "Correo Electronico")
        self.labeldevolucion6.grid (column = 0, row = 6, padx=10, pady = 10)
        self.maildevolucion = tk.StringVar()
        self.entrydevolucion6= tk.Entry(self.ventana10, textvariable = self.maildevolucion, state = "readonly", width = 30 )
        self.entrydevolucion6.grid(column = 1, row = 6, padx=10, pady = 10)
        self.labeldevolucion7 = tk.Label(self.ventana10, text = "Fecha de Inicio")
        self.labeldevolucion7.grid (column = 0, row = 7, padx=10, pady = 10)
        self.iniciodevolucion = tk.StringVar()
        self.entrydevolucion7 = tk.Entry(self.ventana10, textvariable = self.iniciodevolucion, state= "readonly" )
        self.entrydevolucion7.grid(column = 1, row = 7, padx=10, pady = 10)
        self.labeldevolucion8 = tk.Label(self.ventana10, text = "Fecha de Finalizacion")
        self.labeldevolucion8.grid (column = 0, row = 8, padx=10, pady = 10)
        self.finaldevolucion = tk.StringVar()
        self.entrydevolucion8 = tk.Entry(self.ventana10, textvariable = self.finaldevolucion, state = "readonly" )
        self.entrydevolucion8.grid(column = 1, row = 8, padx=10, pady = 10)
        self.botondevolucion = tk.Button(self.ventana10, text = "Controlar Prestamo",command=self.consultamovimientodb ) 
        self.botondevolucion.grid (column = 1, row =10, padx = 20, pady = 20)
        self.botondevolucion1 = tk.Button(self.ventana10, text = "Registrar Devolucion", command= self.devoluciondb ) 
        self.botondevolucion1.grid (column = 1, row =11, padx = 20, pady = 20)

    def consultamovimientodb (self):
        datos = (self.codigodevolucion.get(), )
        respuesta = self.conexion.consultamovimientos (datos)
        if len (respuesta)>0:
            self.titulodevolucion.set(respuesta [0][0])
            self.condiciondevolucion.set(respuesta[0][1])
            self.documentodevolucion.set (respuesta[0][2])
            self.nombredevolucion.set (respuesta[0][3])
            self.telefonodevolucion.set (respuesta[0][4])
            self.maildevolucion.set (respuesta [0][5])
            self.iniciodevolucion.set(respuesta[0][6])
            self.finaldevolucion.set(respuesta[0][7])
        else:
            mb.showinfo("Informacion","Movimiento Inexistente!!")
            self.titulodevolucion.set("")
            self.condiciondevolucion.set("")
            self.documentodevolucion.set ("")
            self.nombredevolucion.set ("")
            self.telefonodevolucion.set ("")
            self.maildevolucion.set ("")
            self.iniciodevolucion.set("")
            self.finaldevolucion.set("")
        
    def devoluciondb (self):
        self.condiciondevolucion.set("Disponible")
        self.finaldevolucion.set("")
        datos1=(self.condiciondevolucion.get(), self.finaldevolucion.get(), self.codigodevolucion.get())
        self.conexion.modifica_libros_devolucion(datos1)        
        datos = (self.codigodevolucion.get(), )
        cantidad = self.conexion.bajamovimiento(datos)  
        mb.showinfo ("Informacion", "Devolucion Registrada")



# Formulario para el lstado de prestamos con retraso


    def formularioretraso (self):
        self.ventana11 = tk.Toplevel(self.ventana)
        self.ventana11.title("Listado de Movimiento con retraso")
        self.ventana11.geometry ("800x800")
        self.botonretraso = tk.Button(self.ventana11, text = "Listado de Prestamos Retrasados", command = self.retrasodb )
        self.botonretraso.grid (column = 0, row =0, padx = 20, pady = 20)
        self.scrollretraso = st.ScrolledText(self.ventana11, width =80, height = 60)
        self.scrollretraso.grid (column = 0 , row = 1, padx= 10, pady = 10)

# Metodos para emitir listado de prestamos con Retraso

    def retrasodb (self):
        respuesta = self.conexion.listaretrasos()
        self.scrollretraso.delete("1.0", tk.END)
        hoy = datetime.datetime.today()
        for fila in respuesta:
            devo = datetime.datetime.strptime((fila[8]), "%d-%m-%Y")
            if hoy>devo: 
                self.scrollretraso.insert (tk.END, "Codigo:  " + str (fila [0])+ "\nTitulo: " + str (fila [1]) +"\nCondicion:  " + str (fila [ 2])+"\nDocumento:  " + str (fila [3])+ "\nNombre de usuario:  " + str (fila [4])+ "\nTelefono:  " + str (fila [5])+"\nCorreo Electronico:  " + str (fila [6])+ "\nFecha Inicio:  " + str (fila [7])+"\nFecha devolucion:  " + str (fila [8])+ "\n\n\n")
        
        for fila in respuesta:
            devo1= datetime.datetime.strptime((fila[8]), "%d-%m-%Y")
            if hoy > devo1:
                codigoretraso = (fila[0])
                condicionretraso = "Retraso"
                datos = ( condicionretraso, codigoretraso)
                self.conexion.modifica_retraso (datos)


# Formulario para consulta de libros por Codigo

    def formularioconsultalibros1 (self):
        self.ventana12 = tk.Toplevel(self.ventana)
        self.ventana12.title("Consulta de Libros por Codigo")
        self.ventana12.geometry ("600x600")
        self.labelcodconsulta = tk.Label (self.ventana12, text = "Codigo")
        self.labelcodconsulta.grid (column = 0, row = 0, padx=10, pady =10)
        self.codigoconsulta = tk.StringVar()
        self.entryconsulta = tk.Entry(self.ventana12, textvariable = self.codigoconsulta )
        self.entryconsulta.grid(column = 1, row = 0, padx=10, pady =10,)
        self.labelconsulta1 = tk.Label(self.ventana12, text = "Titulo" )
        self.labelconsulta1.grid (column = 0, row = 1, padx=10, pady =10)
        self.tituloconsulta = tk.StringVar()
        self.entryconsulta1 = tk.Entry(self.ventana12, textvariable = self.tituloconsulta, width = 40, state = "readonly" )
        self.entryconsulta1.grid(column = 1, row = 1, padx=10, pady =10,)
        self.labelconsulta2 = tk.Label(self.ventana12, text = "Autor")
        self.labelconsulta2.grid (column = 0, row = 2, padx=10, pady = 10)
        self.autorconsulta = tk.StringVar()
        self.entryconsulta2 = tk.Entry(self.ventana12, textvariable = self.autorconsulta, width = 30, state = "readonly" )
        self.entryconsulta2.grid(column = 1, row = 2, padx=10, pady = 10)
        self.labelconsulta3 = tk.Label(self.ventana12, text = "Edicion")
        self.labelconsulta3.grid (column = 0, row = 3, padx=10, pady = 10)
        self.edicionconsulta = tk.StringVar()
        self.entryconsulta3 = tk.Entry(self.ventana12, textvariable = self.edicionconsulta, state= "readonly" )
        self.entryconsulta3.grid (column = 1, row = 3, padx=10, pady = 10)
        self.labelconsulta4 = tk.Label(self.ventana12, text = "Lugar de Impresion")
        self.labelconsulta4.grid (column = 0, row = 4, padx=10, pady = 10)
        self.lugarconsulta = tk.StringVar()
        self.entryconsulta4 = tk.Entry(self.ventana12, textvariable = self.lugarconsulta, state = "readonly" )
        self.entryconsulta4.grid(column = 1, row = 4, padx=10, pady = 10)
        self.labelconsulta5 = tk.Label(self.ventana12, text = "Editorial")
        self.labelconsulta5.grid (column = 0, row = 5, padx=10, pady = 10)
        self.editorialconsulta = tk.StringVar()
        self.entryconsulta5 = tk.Entry(self.ventana12, textvariable = self.editorialconsulta,  state = "readonly")
        self.entryconsulta5.grid(column = 1, row = 5, padx=10, pady = 10)
        self.labelconsulta6 = tk.Label(self.ventana12, text = "Traducion (Si/No)")
        self.labelconsulta6.grid (column = 0, row = 6, padx=10, pady = 10)
        self.traduccionconsulta = tk.StringVar()
        self.entryconsulta6= tk.Entry(self.ventana12, textvariable = self.traduccionconsulta, state = "readonly" )
        self.entryconsulta6.grid(column = 1, row = 6, padx=10, pady = 10)
        self.labelconsulta7 = tk.Label(self.ventana12, text = "Cantidad de Páginas")
        self.labelconsulta7.grid (column = 0, row = 7, padx=10, pady = 10)
        self.cantidadconsulta = tk.StringVar()
        self.entryconsulta7 = tk.Entry(self.ventana12, textvariable = self.cantidadconsulta, state = "readonly" )
        self.entryconsulta7.grid(column = 1, row = 7, padx=10, pady = 10)
        self.labelconsulta8 = tk.Label(self.ventana12, text = "Condición")
        self.labelconsulta8.grid (column = 0, row = 8, padx=10, pady = 10)
        self.condicionconsulta = tk.StringVar()
        self.entryconsulta8 = tk.Entry(self.ventana12, textvariable = self.condicionconsulta, state = "readonly" )
        self.entryconsulta8.grid(column = 1, row = 8, padx=10, pady = 10)
        self.labelconsulta9 = tk.Label(self.ventana12, text = "Fecha de Devolución")
        self.labelconsulta9.grid (column = 0, row = 9, padx=10, pady = 10)
        self.devolucionconsulta = tk.StringVar()
        self.entryconsulta9 = tk.Entry(self.ventana12, textvariable = self.devolucionconsulta, state = "readonly"  )
        self.entryconsulta9.grid(column = 1, row = 9, padx=10, pady = 10)
        self.botonconsulta = tk.Button(self.ventana12, text = "Consultar", command= self.consultadb1 ) 
        self.botonconsulta.grid (column = 1, row =10, padx = 20, pady = 20)

# Metodo para consultar libros por Codigo

    def consultadb1 (self):
        datos = (self.codigoconsulta.get(), )
        respuesta = self.conexion.consultalibros (datos)
        if len (respuesta)>0:
            self.tituloconsulta.set(respuesta [0][0])
            self.autorconsulta.set(respuesta[0][1])
            self.edicionconsulta.set(respuesta[0][2])
            self.lugarconsulta.set(respuesta [0][3])
            self.editorialconsulta.set(respuesta[0][4])
            self.traduccionconsulta.set(respuesta[0][5])
            self.cantidadconsulta.set(respuesta[0][6])
            self.condicionconsulta.set(respuesta[0][7])
            self.devolucionconsulta.set(respuesta[0][8])
        else:
            self.codigoconsulta.set("")
            self.autorconsulta.set("")
            self.edicionconsulta.set("")
            self.lugarconsulta.set("")
            self.editorialconsulta.set("")
            self.traduccionconsulta.set("")
            self.cantidadconsulta.set("")
            self.condicionconsulta.set("")
            self.devolucionconsulta.set("")
            mb.showinfo("Informacion!!","No existe un Libro con ese Codigo")









app = Biblioteca()