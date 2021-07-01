from string import ascii_lowercase as minuscula, ascii_uppercase as mayuscula

def isInt(texto):

    if texto != "":
        if texto[0] == "-":
            aux = texto[1:]
        else:
            aux = texto
        if aux.isdigit():
            return int(texto)

    print("** Error: El dato ingresado no es un número entero\n")
    return

def cifradoCaesar(texto, desp):
    cifrado = ""
    difAtoZ = ord("z") - ord("a") + 1

    for letra in texto:
        if letra in minuscula + mayuscula:
        #limitado a alfabeto latino (a - z, A - Z)    
            aux = ord(letra.lower()) + desp % difAtoZ
            if aux > ord("z"):
                aux -= difAtoZ
            if letra in mayuscula:
                aux -= 32
            cifrado += chr(aux)            
        else:
            cifrado += letra

    return cifrado

texto = input("Ingrese el texto a ser codificado: ")

desp = None
while desp == None:
    desp = isInt(input("\nIngrese el valor de desplazamiento (solo enteros): "))

print("\nEl texto cifrado es: '" + cifradoCaesar(texto, desp) + "'")
