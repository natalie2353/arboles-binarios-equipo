class Nodo:
    def __init__(self, id, nombre, tipo, contenido=""):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo  # "carpeta" o "archivo"
        self.contenido = contenido
        self.children = []

    def renombrar(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def __repr__(self):
        return f"Nodo(id={self.id}, nombre={self.nombre}, tipo={self.tipo})"
