def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#  
        linea = ("+" + "-" * 7) * 3 + "+"
        entre_lin = ("|" + " " * 7) * 3 + "|"

        print(linea)
        for fila in board:     
                print(entre_lin)
                for col in fila:
                        print("|  ", col, "  ", end = "")
                print("|\n" + entre_lin)
                print(linea)
        

def ConvPos2Coord(posicion):
#
# Convierte una posición numerica 1 a 9 dentro del tablero a una tupla de
# coordenadas de posición (i, j)
#
        return ((posicion - 1) // 3, (posicion - 1) % 3)


def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
        pos = input("\nElige una casilla vacía de juego (1 a 9): ")
        
        if len(pos) == 1 and pos >= "1" and pos <= "9": #Determinar que no ingresen datos basura, solo numeros del 1 al 9
                pos = int(pos)
                coord = ConvPos2Coord(pos)
                if coord in FreeFields(board):
                        board[coord[0]][coord[1]] = "O"
                        return
                else:
                        print("*** La casilla",pos,"ya está ocupada. Elige otra...")
                        return EnterMove(board)
        else:
                print("*** El valor digitado no es válido. Vuelve a intentar...")
                return EnterMove(board)
        
        

def FreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
        posxy = []
        for fila in range(3):
                for col in range(3):
                        if board[fila][col] not in ["X","O"]:
                                posxy.append((fila, col))
                        
        return posxy
        

def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
        victoriaIf = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        posJugador = []
        cont = 1
        
        for fila in board:
                for col in fila:
                        if col == sign:
                                posJugador.append(cont)
                        cont += 1

        for comb in victoriaIf:
                cont = 0
                for pos in comb:
                        if pos in posJugador:
                                cont += 1
                        else:
                                break
                if cont == 3:
                        if sign == "X":
                                print("\nHa ganado la CPU... ¡Mejor suerte a la próxima!")
                        else:
                                print("\n¡Felicidades! ¡Has ganado la partida!")
                        return True
        return False

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#     
        from random import randrange

        pos = 5
        coord = ConvPos2Coord(pos)
        while coord not in FreeFields(board):
                pos = randrange(1,10)
                coord = ConvPos2Coord(pos)
        print("\nLa CPU ha elegido la casilla",pos)
        board[coord[0]][coord[1]] = "X"


###################################################################
###                     PROGRAMA PRINCIPAL                      ###
###################################################################

tablero = [[col + fila for col in range(3)] for fila in range(1,9,3)]
turno = "X"

while FreeFields(tablero):
        if turno == "X":
                DrawMove(tablero)
        else:
                EnterMove(tablero)
                
        DisplayBoard(tablero)
        
        if VictoryFor(tablero,turno):
                break;
        
        if turno == "X":
                turno = "O"
        else:
                turno = "X"
else:
        print("\n¡Es un empate! ¡No ha ganado nadie!")
