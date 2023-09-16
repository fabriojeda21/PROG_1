from datos_stark import lista_personajes

"B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe"

def obtener_nombre(lista_heroes: list[dict]):
    """Imprime el nombre de cada superheroe\n
        Recibe la lista completa de personajes\n
        Recorre la lista e imprime  al heroe
    """
    for i in lista_heroes:
        nombre = i.get("nombre")
        print(nombre)

obtener_nombre(lista_personajes)

