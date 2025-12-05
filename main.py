from nodo import Nodo
from arbol import Arbol
from guardar import guardar, cargar

def demo_dia4():
    """Demostración de operaciones del Día 1-4"""
    
    print("=" * 60)
    print("DEMOSTRACIÓN: ÁRBOLES JERÁRQUICOS (Día 1-4)")
    print("=" * 60)
    
    # Crear árbol
    arbol = Arbol()
    print("\n1. Árbol inicial (vacío):")
    arbol.mostrar()
    
    # Agregar carpetas
    print("\n2. Agregando carpetas...")
    docs = Nodo(arbol.generar_id(), "Documentos", "carpeta")
    proyectos = Nodo(arbol.generar_id(), "Proyectos", "carpeta")
    descargas = Nodo(arbol.generar_id(), "Descargas", "carpeta")
    
    arbol.agregar(0, docs)
    arbol.agregar(0, proyectos)
    arbol.agregar(0, descargas)
    
    print("Árbol con carpetas:")
    arbol.mostrar()
    
    # Crear nodos en rutas específicas
    print("\n3. Creando archivos en rutas específicas...")
    exito, msg = arbol.crear_en_ruta("/Documentos", "cv.pdf", "archivo", "Mi CV")
    print(f"   {msg}")
    
    exito, msg = arbol.crear_en_ruta("/Documentos", "contrato.txt", "archivo", "Contrato de trabajo")
    print(f"   {msg}")
    
    exito, msg = arbol.crear_en_ruta("/Proyectos", "proyecto.py", "archivo", "print('Hola')")
    print(f"   {msg}")
    
    print("\nÁrbol con archivos:")
    arbol.mostrar()
    
    # Listar hijos
    print("\n4. Listando hijos de 'Documentos':")
    hijos = arbol.listar_hijos(1)
    for hijo in hijos:
        print(f"   - {hijo.nombre} ({hijo.tipo})")
    
    # Mostrar ruta completa
    print("\n5. Rutas completas:")
    archivo_id = arbol.buscar_por_nombre("cv.pdf")[0].id if arbol.buscar_por_nombre("cv.pdf") else None
    if archivo_id:
        ruta = arbol.obtener_ruta(archivo_id)
        print(f"   Ruta de 'cv.pdf': {ruta}")
    
    # Renombrar
    print("\n6. Renombrando 'Documentos' a 'Mis Documentos'...")
    arbol.renombrar(1, "Mis Documentos")
    arbol.mostrar()
    
    # Mover archivo
    print("\n7. Moviendo 'contrato.txt' a 'Descargas'...")
    archivo_contrato = arbol.buscar_por_nombre("contrato.txt")[0].id if arbol.buscar_por_nombre("contrato.txt") else None
    if archivo_contrato:
        arbol.mover(archivo_contrato, 3)
    arbol.mostrar()
    
    # Eliminar con papelera
    print("\n8. Eliminando 'Descargas' (con papelera)...")
    arbol.eliminar(3, usar_papelera=True)
    print("Árbol después de eliminar:")
    arbol.mostrar()
    
    print("\nElementos en papelera:")
    for item in arbol.listar_papelera():
        print(f"   - {item.nombre} ({item.tipo})")
    
    # Restaurar de papelera
    print("\n9. Restaurando desde papelera...")
    arbol.restaurar_papelera(0)
    arbol.mostrar()
    
    # Guardar en JSON
    print("\n10. Guardando árbol en JSON...")
    guardar(arbol, "arbol.json")
    
    # Cargar desde JSON
    print("\n11. Cargando árbol desde JSON...")
    arbol_cargado = cargar("arbol.json")
    print("Árbol cargado:")
    arbol_cargado.mostrar()
    
    print("\n" + "=" * 60)
    print("[OK] Demostración completada - Día 4")
    print("=" * 60)

if __name__ == "__main__":
    demo_dia4()
