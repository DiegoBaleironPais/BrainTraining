import tkinter as tk
from tkinter import ttk
from LecturaBD import LecturaBD
from TTS import TTS

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Fortalecer Memoria")
        self.master.resizable(False, False)  # Hace que la ventana no sea redimensionable
        self.master.geometry("550x400")  # Tamaño de la ventana ajustado

        self.bd = LecturaBD()
        self.tts = TTS()

        # Frame contenedor
        self.frame = tk.Frame(self.master)
        self.frame.configure(bg='white')
        self.frame.pack(expand=True, fill="both")

        # Encabezado
        self.encabezado = tk.Label(self.frame, text="Bases de Datos Disponibles", font=("Nunito", 12), bg="white")
        self.encabezado.pack(side="top", pady=20)

        # Lista de bases de datos disponibles
        self.lista_bds = ttk.Combobox(self.frame, font=("Nunito", 12))
        self.lista_bds['values'] = self.bd.obtener_bases_de_datos_disponibles()
        self.lista_bds.pack(side="top", pady=10)

        # Encabezado
        self.encabezado = tk.Label(self.frame, text="Numero de elementos", font=("Nunito", 12), bg="white")
        self.encabezado.pack(side="top", pady=20)

        # Selectores para el número de palabras y el tiempo entre ellas
        self.num_palabras = ttk.Spinbox(self.frame, from_=1, to=100, font=("Nunito", 12))
        self.num_palabras.pack(side="top", pady=10)

        # Encabezado
        self.encabezado = tk.Label(self.frame, text="Segundos entre elementos", font=("Nunito", 12), bg="white")
        self.encabezado.pack(side="top", pady=20)

        self.tiempo_entre_palabras = ttk.Spinbox(self.frame, from_=1, to=60, font=("Nunito", 12))
        self.tiempo_entre_palabras.pack(side="top", pady=10)

        self.reproducir_btn = tk.Button(self.frame, text="Reproducir", command=self.reproducir, font=("Nunito", 12))
        self.reproducir_btn.pack(side="top", pady=10)

    def actualizar_lista_bds(self):
        self.bd.path = "./BD/"
        bases = self.bd.obtener_bases_de_datos_disponibles()
        self.lista_bds.delete(0, tk.END)
        for base in bases:
            self.lista_bds.insert(tk.END, base)

    def reproducir(self):
        archivo_seleccionado = self.lista_bds.get()  # Obtiene el valor seleccionado del combobox
        if archivo_seleccionado:  # Verifica que se haya seleccionado algo
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
