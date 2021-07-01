char_v = "█"
char_h = "■"
ancho = 5

dib_linea = (char_v + " " * (ancho - 1),              #0: linea vert izq
             " " * (ancho - 1) + char_v,              #1: linea vert der
             char_v + " " * (ancho - 2) + char_v,     #2: linea vert ambos
             " " + char_h * (ancho - 2) + " ",        #3: linea horizontal
             " " * ancho)                             #4: espacio horizontal

dib_num = ((3,2,2,4,2,2,3),
           (4,1,1,4,1,1,4),
           (3,1,1,3,0,0,3),
           (3,1,1,3,1,1,3),
           (4,2,2,3,1,1,4),          
           (3,0,0,3,1,1,3),
           (3,0,0,3,2,2,3),
           (3,1,1,4,1,1,4),
           (3,2,2,3,2,2,3),
           (3,2,2,3,1,1,3))

while True:
    numero = input("Digite el número a representar como LEDs: ")

    if not numero.isdigit():
        print("** ERROR: Solo se aceptan números. La entrada no es válida.\n")
    else:
        break

for linea in range(7):
    for digito in numero:
        print(dib_linea[dib_num[int(digito)][linea]] + "  ", end = "")
    print()
