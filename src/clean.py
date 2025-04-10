import unicodedata

def quitar_acentos(cadena):
    """Elimina acentos de una cadena"""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', cadena)
        if not unicodedata.combining(c)
    )

def clean_data (clients):
    """recorre la lista de nombres y genera otra limpia y ordenada """

    nombres_limpios = []
    vistos = set()

    for nombre in clients:

        if not nombre or not nombre.strip():
            continue  # Ignorar nulos o espacios vacíos
        
        limpio = nombre.strip().title() # dar formato

        clave = quitar_acentos(limpio).lower()  #saco acepto para detectar duplicados
        
        if clave not in vistos:
            vistos.add(clave)
            nombres_limpios.append(limpio)

    return sorted(nombres_limpios)
    