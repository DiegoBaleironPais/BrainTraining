import tkinter as tk
from tkinter import ttk
from LecturaBD import LecturaBD
from TTS import TTS

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Fortalecer Memoria")
        self.master.geometry("800x600")  # Tamaño de la ventana ajustado

        self.bd = LecturaBD()
        self.tts = TTS()

        # Frame contenedor
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=True)

        # Encabezado
        self.encabezado = tk.Label(self.frame, text="Bases de Datos Disponibles", font=("Arial", 16))
        self.encabezado.pack(side="top", pady=40)

        # Lista de bases de datos disponibles
        self.lista_bds = ttk.Combobox(self.frame, font=("Arial", 12))
        self.lista_bds['values'] = self.bd.obtener_bases_de_datos_disponibles()
        self.lista_bds.pack(side="top", pady=20)

        # Selectores para el número de palabras y el tiempo entre ellas
        self.num_palabras = ttk.Spinbox(self.frame, from_=1, to=100, font=("Arial", 12))
        self.num_palabras.pack(side="top", pady=20)

        self.tiempo_entre_palabras = ttk.Spinbox(self.frame, from_=1, to=60, font=("Arial", 12))
        self.tiempo_entre_palabras.pack(side="top", pady=20)

    def actualizar_bases_disponibles(self):
        self.bd.path = "./BD/"
        bases = self.bd.obtener_bases_de_datos_disponibles()
        self.bases_disponibles.delete(0, tk.END)
        for base in bases:
            self.bases_disponibles.insert(tk.END, base)

    def reproducir(self):
        seleccion = self.bases_disponibles.curselection()
        if seleccion:
            archivo_seleccionado = self.bases_disponibles.get(seleccion[0])
            self.bd.archivo = "./BD/" + archivo_seleccionado

            if self.bd.abrir_archivo():
                num_elem = int(self.num_palabras.get())
                delay = int(self.tiempo_entre_palabras.get())
                elementos = self.bd.obtener_elementos(num_elem=num_elem)
                self.tts.reproducir_elementos(elementos, delay)
                self.bd.cerrar_archivo()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
