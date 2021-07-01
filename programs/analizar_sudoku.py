def ComprobarDistintos(linea):
    return sorted(linea) == [str(i) for i in range(1,10)]

def ComprobarFilas(lista):
    for fila in lista:
        if not ComprobarDistintos(fila):
            return False
    return True

def ComprobarColumnas(lista):
    for fila in lista:
        columna = ""
        for i in range(9):
            columna += fila[i]
        if not ComprobarDistintos(columna):
            return False
    return True

def ComprobarCajas(lista):
    for linea in range(0,9,3):    
        for col in range(0,9,3):
            caja = ""
            for fila in range(3):
                caja += lista[fila + linea][col : col + 3]
            if not ComprobarDistintos(caja):
                return False
    return True

def ImprimirSudoku(sudoku):
    linea_hor = ("+" + "-" * 9) * 3 + "+"

    print("\n"+linea_hor)
    for linea in range(9):
        print("|", end = "")
        for letra in range(9):
            print(" " + sudoku[linea][letra] + " ", end = "")
            if (letra + 1) % 3 == 0:
                print("|", end = "")
        print()
        if (linea + 1) % 3 == 0:
            print(linea_hor)


                                            ### VALORES DE PRUEBA ####
#sudoku = ["295743861","431865927","876192543","387459216","612387495","549216738","763524189","928671354","154938672"] #válido
#sudoku = ["534678912","672195348","198342567","859761423","426853791","713924856","961537284","287419635","345286179"] #válido
#sudoku = ["123456789","456789123","789123456","234567891","567891234","891234567","345678912","678912345","912345678"] #válido
#sudoku = ["195743862","431865927","876192543","387459216","612387495","549216738","763524189","928671354","254938671"] #erróneo
#sudoku = ["285743862","432865827","876282543","387458226","622387485","548226738","763524288","828672354","254838672"] #erróneo (div por 9 y suma = 45)
sudoku = ["123456789","234567891","345678912","431865927","567891234","678912345","789123456","876192543","928671354"] #erróneo
'''
print()
i = 0
sudoku = []
while i < 9:
    fila = input("Ingrese los 9 dígitos (1 al 9) de la fila " + str(i + 1) +" consecutivamente: ")

    if len(fila) == 9 and fila.isdigit() and "0" not in fila:
        sudoku.append(fila)
        i += 1
    else:
        print("** Error: El valor digitado no es válido. Vuelva a intentar...\n")
'''
ImprimirSudoku(sudoku)

if ComprobarFilas(sudoku) and ComprobarColumnas(sudoku) and ComprobarCajas(sudoku):
    print("\nEl sudoku es válido\n")
else:
    print("\nEl sudoku es erróneo\n")