def IsPalindrome(texto):
    texto = texto.upper()
    reverse = texto[::-1]
    return texto == reverse

while True:
    frase = input("\nEscriba la frase para determinar si es un palíndromo: ")
    if frase == "":
        print("*** ¡Adios! ***")
        break
    frase = "".join(frase.split())
    if not frase.isalpha():
        print("** Error: La frase no es válida. Solo letras y espacios, por favor")
        continue
    if IsPalindrome(frase):
        print("** La frase ES un palíndromo **")
    else:
        print("** La frase NO ES un palíndromo **")
