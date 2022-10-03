
from classes.LecturaCoordenadas import LecturaCoordenadas
from classes.Cache import *
from classes.Request import *
from tkinter import messagebox, ttk
import tkinter as tk

class Interfaz(ttk.Frame):
    
    def __init__(self, ventana, clavesCiudad):
        super().__init__(ventana)
        self.estiloVentana(ventana)
        self.place(width=350, height=250)
        
        self.etiquetaInformacion = ttk.Label(ventana, text="Bienvenido. Selecciona la clave de la ciudad\nde destino:")
        self.estiloMensaje()

        self.combo = ttk.Combobox(self,state= "readonly",values= clavesCiudad)
        self.combo.place(x=100, y=90)
        
        self.button = ttk.Button(text="Mostrar clima",command=self.muestraOpcion)
        self.button.place(x=130, y=140)
    
    def estiloVentana(self,ventana):    
        ventana.title("Consultor del clima")
        ventana.iconbitmap('assets/icono.ico')
        ventana.eval('tk::PlaceWindow . center')
        ventana.resizable(0,0)
        ventana.config(width=350, height=250)
    
    def estiloMensaje(self):
        self.etiquetaInformacion.place(x=30, y=30) 
        self.etiquetaInformacion.configure(font=('Arial', 12))
        self.etiquetaInformacion.configure(anchor="center")
    
    def muestraOpcion(self):
        opcionElegida = self.combo.get()
        if opcionElegida == '':
            messagebox.showerror(message= "¡Selecciona una opción!",title="Error")
        else:
            solicitud = Request()
            cache = {}
            mensaje  = ''
            if(cache == {}):
                solicitud.conectarApi(opcionElegida)
                datos = solicitud.generaDatos()
                Cache.agregaDatos(cache,datos,opcionElegida)
                mensaje = Cache.muestraDatos(cache, opcionElegida)
            elif(Cache.infoActualizada(cache, opcionElegida) == True):
                mensaje = Cache.muestraDatos(cache, opcionElegida)
            elif():
                solicitud.conectarApi(opcionElegida)
                datos = solicitud.generaDatos()
                Cache.agregaDatos(cache,datos,opcionElegida)
                mensaje = Cache.muestraDatos(cache, opcionElegida)
            messagebox.showinfo(message= mensaje,title="Información del clima")

ventana = tk.Tk()
lectura = LecturaCoordenadas()
dicAeropuertos = lectura.getCiudades()
clavesAeropuertos = list(dicAeropuertos)
clavesAeropuertos.pop(0)
gestorClima = Interfaz(ventana, clavesAeropuertos)
gestorClima.mainloop()