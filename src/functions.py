def select_lines (zen_text):
    """retorno las lineas del texto zen que cumplen la condicion"""

    zen_final = ""
    for linea in zen_text.splitlines():     #separo en lineas
        palabras = linea.split()    #retorna una lista de palabras
        #verifico si hay al menos 2 palabras y si la 2da es vocal
        if len(palabras) >= 2 and palabras[1][0].lower() in "aeiou":
            zen_final += linea + "\n"

    return zen_final


def longest_title (titles):
    return max(titles, key=len)

def imprimir_reglas(rules, clave):
    rules_final = ""
    for linea in rules.split("\n"):
        if clave in linea:
            rules_final += linea + "\n"
    return rules_final 