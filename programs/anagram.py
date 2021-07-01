def OrdenarLetras(texto):
    lista = []
    for letra in texto:
        lista.append(letra)
    lista.sort()
    return "".join(lista)

def Anagramas(texto1, texto2):
    if OrdenarLetras(texto1.lower()) == OrdenarLetras(texto2.lower()):
        print("\nSi son anagramas")
    else:
        print("\nNo son anagramas")

def ValidarString(cadena):
#Valida si una cadena de caracteres (string) está compuesta por letras (obligatorio) y/o espacios
    '''if cadena == "":
        return
    else:'''
    cadena = "".join(cadena.split())
    if not cadena.isalpha() or cadena == "":
        print("** Error: La frase no es válida. Solo letras y espacios, por favor\n")
        return False
    return cadena

frases = []
i = 0

while i < 2:
    frase = ValidarString(input("\nEscriba la frase " + str(i + 1) +": "))
    if frase == False: #or frase == None:
        continue
    else:
        frases.append(frase)
        i += 1

Anagramas(frases[0],frases[1])
