char_v = "█"
char_h = "■"
ancho = 5

dib_linea = (char_v + " " * (ancho - 1),              #0: linea vert izq
             " " * (ancho - 1) + char_v,              #1: linea vert der
             char_v + " " * (ancho - 2) + char_v,     #2: linea vert ambos
             " " + char_h * (ancho - 2) + " ")        #3: linea horizontal

num_seg =  ("1110111",               ##0##
            "0010010",              #     # 
            "1011101",              #1    #2
            "1011011",               ##3##
            "0111010",              #     #
            "1101011",              #4    #5
            "1101111",               ##6##
            "1010010",
            "1111111",
            "1111011")

while True:
    numero = input("Digite el número a representar como LEDs: ")

    if not numero.isdigit():
        print("** ERROR: Solo se aceptan números. La entrada no es válida.\n")
    else:
        break

matriz_num = [[" " * ancho for i in range(len(numero))] for i in range(7)]

for i in range(len(numero)):
    aux = num_seg[int(numero[i])]
    for seg in range(7):
        if int(aux[seg]):
            if seg in (0,3,6):
                matriz_num[seg][i] = dib_linea[3]
            elif seg in (1,4):
                if aux[seg] == aux[seg + 1]:
                    matriz_num[seg][i] = dib_linea[2]
                else:
                    matriz_num[seg][i] = matriz_num[seg+1][i] = dib_linea[0]
            elif seg in (2,5):
                if aux[seg] == aux[seg - 1]:
                    matriz_num[seg][i] = dib_linea[2]
                else:
                    matriz_num[seg][i] = matriz_num[seg-1][i] = dib_linea[1]

for i in range(7):
    print("  ".join(matriz_num[i]))
