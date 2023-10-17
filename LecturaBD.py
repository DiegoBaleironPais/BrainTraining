import os

class LecturaBD:
    def __init__(self, archivo=""):
        self.ruta_bd = "./BD/"
        self.archivo = os.path.join(self.ruta_bd, archivo)
        self.file_obj = None

    def abrir_archivo(self):
        try:
            self.file_obj = open(self.archivo, 'r')
        except FileNotFoundError:
            print("Archivo no encontrado.")
            return False
        return True

    def cerrar_archivo(self):
        if self.file_obj:
            self.file_obj.close()

    def obtener_elementos(self, num_elem=None):
        if self.file_obj:
            lineas = self.file_obj.readlines()
            elementos = []

            for linea in lineas:
                terminos = linea.strip().split(';')
                elementos.extend([t for t in terminos if t])

            return elementos[:num_elem] if num_elem else elementos
        else:
            print("El archivo no está abierto.")
            return None

    def obtener_bases_de_datos_disponibles(self):
        try:
            return [f for f in os.listdir(self.ruta_bd) if f.endswith('.txt')]
        except FileNotFoundError:
            print("Carpeta BD no encontrada.")
            return None


# Uso de la clase LecturaBD
if __name__ == "__main__":
    bd = LecturaBD()

    print("Bases de datos disponibles: ", bd.obtener_bases_de_datos_disponibles())

    bd.archivo = os.path.join(bd.ruta_bd, "marcas_coches.txt")  # Reemplaza 'tu_archivo.txt' con el archivo que quieras leer
    
    if bd.abrir_archivo():
        elementos = bd.obtener_elementos(num_elem=5)  # Obtén los primeros 5 elementos
        print("Elementos de la base de datos: ", elementos)
        bd.cerrar_archivo()
