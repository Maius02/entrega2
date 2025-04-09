import string

def verificar_cadena (cadena):
    """retorna tre si la cadena solo contiene letras"""

    return all(char in string.ascii_letters for char in cadena)

def verificar_anagramas (cadena1, cadena2):
    """para que sean anagramas deben tener la misma cantidad de letras y 
     las mismas letras. Por lo tanto si las ordeno deberian ser exactamente iguales
       """   
    return sorted(cadena1.lower())==sorted(cadena2.lower())

