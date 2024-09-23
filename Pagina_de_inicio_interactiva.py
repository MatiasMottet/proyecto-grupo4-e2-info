import tkinter as tk
from tkinter import ttk
import time

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página de Inicio interactiva")
        self.geometry("800x600")

        # Crear menú desplegable
        # Constructor
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.menu_inicio = tk.Menu(self.menubar, tearoff=0)
        self.menu_inicio.add_command(label="Pestaña 1", command=self.pestaña1)
        self.menu_inicio.add_command(label="Pestaña 2", command=self.pestaña2)
        self.menu_inicio.add_command(label="Pestaña 3", command=self.pestaña3)
        self.menu_inicio.add_separator()
        self.menu_inicio.add_command(label="Salir", command=self.logout)
        self.menubar.add_cascade(label="Inicio", menu=self.menu_inicio)

        # Crear reloj en la zona superior derecha
        self.reloj = tk.Label(self, text="", font=("Arial", 12))
        self.reloj.pack(side=tk.TOP, anchor=tk.E)
        self.actualizar_reloj()

        # Crear pestañas
        self.pestañas = ttk.Notebook(self)
        self.pestañas.pack(fill=tk.BOTH, expand=True)

        self.pestaña1_frame = tk.Frame(self.pestañas)
        self.pestaña2_frame = tk.Frame(self.pestañas)
        self.pestaña3_frame = tk.Frame(self.pestañas)

        self.pestañas.add(self.pestaña1_frame, text="Pestaña 1")
        self.pestañas.add(self.pestaña2_frame, text="Pestaña 2")
        self.pestañas.add(self.pestaña3_frame, text="Pestaña 3")

        #Crear estilo
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="lightblue")
        style.configure("TNotebook.Tab", font=("Arial", 12, "bold"), padding=[10, 5])
        style.configure("TLabel", font=("Arial", 12))
        

    def pestaña1(self):
        # Contenido de la pestaña 1
        label = tk.Label(self.pestaña1_frame, text="Contenido de la pestaña 1")
        label.pack()

    def pestaña2(self):
        # Contenido de la pestaña 2
        label = tk.Label(self.pestaña2_frame, text="Contenido de la pestaña 2")
        label.pack()

    def pestaña3(self):
        # Contenido de la pestaña 3
        label = tk.Label(self.pestaña3_frame, text="Contenido de la pestaña 3")
        label.pack()

    def actualizar_reloj(self):
        hora_actual = time.strftime("%H:%M:%S")
        self.reloj.config(text=hora_actual)
        self.after(1000, self.actualizar_reloj)

    def logout(self):
        self.quit()



# Llamada a la clase y a mainloop para inciar la app
app = Aplicacion()
app.mainloop()

'''
Explicación

En el código, se crea una clase Aplicacion.

En el constructor, creamos un menú desplegable con tres opciones que llaman
a las funciones pestaña1, pestaña2 y pestaña3, respectivamente.

Se creamos un reloj en la zona superior derecha que se actualiza cada segundo.

Se crea tres pestañas utilizando ttk.Notebook* y se agrega contenido a cada pestaña
en las funciones: pestaña1, pestaña2 y pestaña3.

*ttk.Notebook: Administra una colección de ventanas y muestra una sola uno a la vez.
Cada ventana secundaria está asociada a una pestaña, que el usuario puede seleccionar
cambiar la ventana que se muestra actualmente.
'''

