import tkinter as tk
from tkinter import ttk
import sys
import os

# Añadir la ruta del directorio raíz para importar LecturaBD y TTS
sys.path.append(os.path.abspath(os.path.join('../..')))
dir_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(dir_path)
sys.path.append(parent_path)
print(sys.path)

from LecturaBD import LecturaBD
from TTS import TTS

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Fortalecer Memoria")
        self.master.geometry("400x300")

        self.bd = LecturaBD()
        self.tts = TTS()

        self.bases_disponibles = tk.Listbox(self.master)
        self.actualizar_bases_disponibles()
        self.bases_disponibles.pack()

        self.num_palabras_label = tk.Label(self.master, text="Número de palabras:")
        self.num_palabras_label.pack()
        
        self.num_palabras = tk.Spinbox(self.master, from_=1, to=100)
        self.num_palabras.pack()

        self.tiempo_entre_palabras_label = tk.Label(self.master, text="Tiempo entre palabras:")
        self.tiempo_entre_palabras_label.pack()

        self.tiempo_entre_palabras = tk.Spinbox(self.master, from_=1, to=10)
        self.tiempo_entre_palabras.pack()

        self.reproducir_btn = tk.Button(self.master, text="Reproducir", command=self.reproducir)
        self.reproducir_btn.pack()

    def actualizar_bases_disponibles(self):
        self.bd.path = "../BD/"
        bases = self.bd.obtener_bases_de_datos_disponibles()
        self.bases_disponibles.delete(0, tk.END)
        for base in bases:
            self.bases_disponibles.insert(tk.END, base)

    def reproducir(self):
        seleccion = self.bases_disponibles.curselection()
        if seleccion:
            archivo_seleccionado = self.bases_disponibles.get(seleccion[0])
            self.bd.archivo = "../BD/" + archivo_seleccionado

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
