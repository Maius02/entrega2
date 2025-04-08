def select_lines (zen_text):
    """punto 1: retorno un string con todas las líneas (del zen de python) 
    cuya segunda palabra comienze con aeiouAEIOU"""

    zen_final = ""
    for linea in zen_text.splitlines():     #separo en lineas
        palabras = linea.split()    #retorna una lista de palabras
        #verifico si hay al menos 2 palabras y si la 2da es vocal
        if len(palabras) >= 2 and palabras[1][0].lower() in "aeiou":
            zen_final += linea + "\n"

    return zen_final


def longest_title (titles):
    """punto 2: retorna el titulo con mas palabras"""

    return max(titles, key=len)


def imprimir_reglas(rules, clave):
    """punto 3: retorna un string con las reglas que contienen la palabra clave"""

    rules_final = ""
    for linea in rules.split("\n"):
        if clave in linea:
            rules_final += linea + "\n"
    return rules_final 


def validar_nombre(nombre):
    """punto 4: devuelve true si el nombre cumple las condiciones
        Al menos 5 caracteres.
        Contiene al menos un número.
        Contiene al menos una letra mayúscula.
        Solo puede contener letras y números.

        .isalnum() # verificar si una cadena solo contiene caracteres alfanuméricos (letras y números) (return boolean)
        any() # evalúa un iterable (como una lista o generador) y devuelve True si al menos un elemento es True
    """
    if not len(nombre) >= 5:
        return False
    if not nombre.isalnum():
        return False
    if not any(char.isdigit() for char in nombre):
        return False
    if not any(char.isupper() for char in nombre):
        return False
    return True


def clasificar_velocidad(velocidad):
    """punto 5: clasifica la velocidad ingresada. En rápido, normal o lento"""

    if velocidad < 200:
        return "Rápido"
    elif 200 <= velocidad <= 500:
        return "Normal"
    else:
        return "Lento"
    
    
def cantidad_menciones(descripciones, palabra):
    """devuelve la cantidad de veces que la palabra se encuentra en las descripciones"""

    cantidad = 0

    #compara en minuscula, split separa en palabras y cuanta las que coinciden
    for desc in descripciones:
        cantidad += desc.lower().split().count(palabra.lower()) #desc.count(palabra)
    
    return cantidad

