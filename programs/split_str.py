def misplit(strng):
    try:
        assert isinstance(strng,str)
        if strng == '' or strng.isspace():
            return [ ]
        words = []
        word = ""
        for letter in strng:
            if letter != " ":
                word += letter
            elif word != "":
                words.append(word)
                word = ""
        if word != "":
            words.append(word)
        return words
    except AssertionError:
        return "Error: El valor de la funcion misplit no es una cadena"

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
print(misplit(156))
print()