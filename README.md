# Gestor de Arboles Jerarquicos

Un sistema de gestion de carpetas y archivos basado en estructuras de arbol general en Python.

Estado: Funcional (Dias 1-4 completados)
Ultima actualizacion: 5 de diciembre de 2025
Pruebas: 13/13 pasando
Lineas de codigo: 481

## Descripcion del Proyecto

Este sistema gestor de archivos jerarquico permite:

- Crea, mueve, renombrar y elimina nodos (carpetas/archivos)
- Buscar nodos por nombre
- Muestra rutas completas
- Guarda y carga en JSON
- Usar papelera temporal con restauracion

## Arquitectura

### Componentes

nodo.py
  Define clase base para nodos (Dia 1)
  Proporciona: id, nombre, tipo, contenido, children

arbol.py
  Proporciona estructura jerarquica y operaciones (Dias 2-3)
  Ofrece 14 metodos: agregar, buscar, mover, renombrar, eliminar, etc.

guardar.py
  Maneja persistencia en JSON (Dia 4)
  Proporciona: guardar() y cargar()

tests.py/tests_arbol.py
  Implementa pruebas unitarias (Dias 2-3)
  Contiene 13 pruebas

main.py
  Demuestra funcionalidades 
  Ejecuta ejemplo completo del sistema

### Modelo de Datos

```
Nodo:
  - id: int (unico)
  - nombre: str
  - tipo: "carpeta" | "archivo"
  - contenido: str (solo para archivos)
  - children: list[Nodo]
```

## Progreso por Dia

### Dia 1: Definir MVP y Estructuras
- Define clase Nodo con atributos
- Crea clase Arbol con raiz
- Establece formato JSON de persistencia

Archivos: nodo.py, arbol.py

### Dia 2-3: Arbol y Operaciones Basicas
- agregar(id_padre, nodo) - Agrega nodo como hijo
- buscar(nodo, id) - Busca recursivamente por ID
- buscar_por_nombre(nombre) - Busca por nombre
- renombrar(id, nuevo_nombre) - Renombra nodo
- eliminar(id, usar_papelera) - Elimina con papelera temporal
- mover(id, id_nuevo_padre) - Mueve nodo a otro padre
- listar_hijos(id) - Lista hijos de un nodo
- crear_en_ruta(ruta, nombre, tipo, contenido) - Crea en ruta especifica
- obtener_ruta(id) - Obtiene ruta completa
- mostrar(nodo, nivel) - Imprime arbol con indentacion
- papelera: restaura(), lista(), vacia()

Implementa: 13 pruebas unitarias

Archivos: arbol.py, tests.py/tests_arbol.py

### Dia 4: Persistencia JSON
- guardar(arbol, archivo) - Guarda arbol en JSON
- cargar(archivo) - Carga arbol desde JSON
- Mantiene contador_id en persistencia
- Preserva/restaura papelera

Archivos: guardar.py, main.py

## Instalacion y Ejecucion

### Requisitos
- Python 3.7+
- Sin dependencias externas

### Estructura de Carpetas
```
arbol binario equipo/
├── nodo.py
├── arbol.py
├── guardar.py
├── main.py
├── arbol.json (generado)
├── tests.py/
│   └── tests_arbol.py
├── ejecutar.bat
├── .gitignore
├── README.md
└── .github/

```

### Ejecutar Demostracion
```bash
cd "c:\Users\ASUS\Downloads\arbol binario equipo"
python main.py
```

Salida: Demostracion paso a paso de todas las operaciones (11 pasos)

### Ejecutar Pruebas Unitarias
```bash
python -m unittest discover -s tests.py -p "tests_*.py" -v
```

O directamente:
```bash
python tests.py/tests_arbol.py
```

## Operaciones Disponibles

### Operaciones Basicas

```python
from arbol import Arbol
from nodo import Nodo
from guardar import guardar, cargar

# Crear arbol
arbol = Arbol()

# Crear nodo con ID automatico
archivo = Nodo(arbol.generar_id(), "documento.txt", "archivo", "contenido")

# Agregar nodo
arbol.agregar(0, archivo)  # ID 0 es raiz

# Buscar por ID
nodo = arbol.buscar(arbol.raiz, 1)

# Buscar por nombre
nodos = arbol.buscar_por_nombre("documento.txt")

# Renombrar
arbol.renombrar(1, "nuevo_nombre.txt")

# Mover nodo
arbol.mover(1, 2)  # Mueve nodo 1 bajo nodo 2

# Eliminar (con papelera)
arbol.eliminar(1, usar_papelera=True)

# Restaurar de papelera
arbol.restaurar_papelera(0)

# Listar hijos
hijos = arbol.listar_hijos(1)

# Mostrar arbol
arbol.mostrar()
```

### Operaciones Avanzadas

```python
# Crear nodo en ruta especifica
exito, msg = arbol.crear_en_ruta("/Documentos", "archivo.txt", "archivo", "contenido")

# Obtener ruta completa
ruta = arbol.obtener_ruta(id_nodo)  # Retorna "/Documentos/archivo.txt"

# Papelera
papelera = arbol.listar_papelera()
arbol.vaciar_papelera()
```

### Persistencia

```python
# Guardar arbol
guardar(arbol, "arbol.json")

# Cargar arbol
arbol2 = cargar("arbol.json")
```

## Ejemplo Completo

```python
from arbol import Arbol
from nodo import Nodo
from guardar import guardar, cargar

# Crear estructura
arbol = Arbol()

# Agregar carpetas
docs = Nodo(arbol.generar_id(), "Documentos", "carpeta")
arbol.agregar(0, docs)

# Crear en ruta
arbol.crear_en_ruta("/Documentos", "cv.pdf", "archivo", "Mi CV")

# Mostrar
arbol.mostrar()
# Salida:
# - root (carpeta)
#   - Documentos (carpeta)
#     - cv.pdf (archivo)

# Guardar
guardar(arbol, "arbol.json")

# Cargar
arbol2 = cargar("arbol.json")
arbol2.mostrar()
```

## Pruebas

### Casos de Prueba

Crear nodo
Renombrar nodo
Insertar y buscar
Eliminar nodo
Mover nodo entre padres
Listar hijos
Crear en ruta especifica
Papelera y restauracion
Guardar y cargar JSON

Resultado: 13 pruebas pasadas

## Convenciones del Proyecto

1. IDs unicos - Usar arbol.generar_id() para crear nuevos nodos
2. Tipos validos - Solo "carpeta" y "archivo"
3. Raiz especial - ID=0, nombre="root", siempre carpeta
4. Rutas - Formato /Documentos/Proyectos/archivo.txt
5. Encoding - UTF-8 en todos los JSON
6. Indentacion - 2 espacios en visualizacion de arbol

## Formato JSON

```json
{
    "arbol": {
        "id": 0,
        "nombre": "root",
        "tipo": "carpeta",
        "contenido": "",
        "children": [
            {
                "id": 1,
                "nombre": "Mis Documentos",
                "tipo": "carpeta",
                "contenido": "",
                "children": [
                    {
                        "id": 4,
                        "nombre": "cv.pdf",
                        "tipo": "archivo",
                        "contenido": "Mi CV",
                        "children": []
                    }
                ]
            }
        ]
    },
    "contador_id": 7,
    "papelera": []
}
```

## Mantenimiento

### Agregar Nueva Operacion

1. Agregar metodo en Arbol en arbol.py
2. Agregar prueba unitaria en tests.py/tests_arbol.py
3. Documentar en README.md
4. Probar con main.py

### Estructura de Commits (Git)

Dia 1: Setup inicial - Nodo y Arbol
Dia 2: Operaciones basicas - CRUD
Dia 3: Pruebas unitarias y busqueda
Dia 4: Persistencia JSON

## Proximos Pasos (Dias 5-14)

- Dia 5-6: Implementar Trie para autocompletado
- Dia 7-9: Interfaz de consola interactiva
- Dia 10-11: Pruebas de integracion
- Dia 12: Documentacion final
- Dia 13: Demo
- Dia 14: Presentacion

## Soporte

Para preguntas o problemas, revisar:
1. .github/copilot-instructions.md - Notas tecnicas
2. tests.py/tests_arbol.py - Ejemplos de uso
3. main.py - Demostracion completa

---

Estado: Funcional (Dias 1-4)
Ultima actualizacion: 5 de diciembre de 2025
Equipo: [Tus nombres aqui]
