import random
 
def dibujarTablero(tablero):
    #0 1 2
    #3 4 5
    #6 7 8
    print('     |     |')
    print(' ' + tablero[0] + '   | ' + tablero[1] + '   | ' + tablero[2])
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(' ' + tablero[3] + '   | ' + tablero[4] + '   | ' + tablero[5])
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(' ' + tablero[6] + '   | ' + tablero[7] + '   | ' + tablero[8])
    print('     |     |')
 
def elegirLetra():
    letra = ''
    while not (letra== 'X' or letra == 'O'):
        print('¿Qué letra desea ser X/O?')
        letra = input().upper()
 
    # Si el jugador elije X, entonces la maquina sera O y viceversa
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def vaPrimero():
    # Con la funcion randit elejimos de forma aleatoria quien inicia primero maquina o jugador
    if random.randint(0,1) == 0:
        return 'maquina'
    else:
        return 'jugador'

 
 
def jugarDeNuevo():
    print('quieres jugar de nuevo? (si o no)')
    
    return input().lower().startswith('s')
 
def moverLetra(tablero, letra, posicion):
    tablero[posicion] = letra
 
def esGanador(tab, let):
    return ((tab[0] == let and tab[1] == let and tab[2] == let) or 
    (tab[3] == let and tab[4] == let and tab[5] == let) or 
    (tab[6] == let and tab[7] == let and tab[8] == let) or 
    (tab[0] == let and tab[3] == let and tab[6] == let) or 
    (tab[1] == let and tab[4] == let and tab[7] == let) or 
    (tab[2] == let and tab[5] == let and tab[8] == let) or 
    (tab[2] == let and tab[4] == let and tab[6] == let) or 
    (tab[0] == let and tab[4] == let and tab[8] == let)) 
 

 
def copiarTablero(tablero):
    # Duplica el tablero para ir verificando las posiciones 
    copiaTab = []
 
    for i in tablero:
        copiaTab.append(i)
 
    return copiaTab
 
def posicionValidaLibre(tablero, posicion):
    # Nos va a retornar verdadero si el espacio esta libre
    return tablero[posicion] == ' '




def maquinaMaquina():
    maquina="Maquina 1"
   
    tablero=dibujarTablero()
    
    while(turno<10):
        dibujarTablero(tablero)
        print("Turno de "+maquina)

        letra="X"
        if(letra=="X"):
           movimientoMaquina(tablero,letra)
           turno=vaPrimero()
           if(esGanador(tablero,letra)==1):
                dibujarTablero(tablero)
                break
            
           simbolo="O"
           jugador="Maquina 2"

           
        else:
            movimientoMaquina(simbolo,tablero,turno)
            if(verificarGanador(simbolo,tablero)==1):
                imprimirTablero(tablero)
                
                break
            maquina="Maquina 1"
            simbolo="X"
        turno+=1;

    else:
        print(maquina+" Ganó!")



def minmax(tablero,turno,letra):
    busca=1
    noBusca=-1
    
    if(letra=="X"):
       jugador="max"
    else:
        jugador="min"
        busca=-1
        noBusca=1

    if(esGanador(letra,tablero)):
        if(jugador=="max"):
            return 1
        else:
            return -1
    

    valida=posicionValidaLibre(tablero)
    indices=[]
    indicesUtiles=[]
    
    
    for intPos in valida:
        
        copia=copiarTablero(tablero)
        copia[intPos]=letra
        
        aux="X"
        if(letra=="X"):
            aux="O"

            
        turnoAux=turno+1
        indicesUtiles.append(minmax(copia,aux))
        indices.append(indice)
        indice+=1
    
    if (busca in utiles):
        
        print("Encontrado")
        index=indicesUtiles.index(utilABuscar);
        indice=indices[index];
        i=int(valida[indice][0])
        tablero[i]=letra
        
        return busca

     
    else:
        print("No encontrado")
        
        
def movimientoJugador(tablero):
    posicion = ' '
    while posicion not in '0 1 2 3 4 5 6 7 8 '.split() or not posicionValidaLibre(tablero, int(posicion)):
        print('Elije una posicion--> (0-8) :')
        posicion = input()
    return int(posicion)
 
def posibleGanador(tablero, lista):
    listaMovimientos = []
    for i in lista:
        if posicionValidaLibre(tablero, i):
            listaMovimientos.append(i)
 
    if len(listaMovimientos) != 0:
        return random.choice(listaMovimientos)
    else:
        return None
 
def movimientoMaquina(tablero, letraMaquina):
    if (letraMaquina == 'X'):
       letraJugador = 'O'
    else:
        letraJugador = 'X'
 
   
    for i in range(0, 9):
        copia = copiarTablero(tablero)
        if posicionValidaLibre(copia, i):
            moverLetra(copia, letraMaquina, i)
            if esGanador(copia, letraMaquina):
                return i
 
   
    for i in range(0, 9):
        copia= copiarTablero(tablero)
        if posicionValidaLibre(copia, i):
              moverLetra(copia, letraJugador, i)
              if esGanador(copia, letraJugador):
                return i
 

    posicion = posibleGanador(tablero, [0, 2, 6, 8])
    if posicion != None:
        return posicion
 
 
    if posicionValidaLibre(tablero, 4):
        return 4
 

    return posibleGanador(tablero, [1, 3, 5, 7])
 
def tableroLleno(tablero):
    for i in range(0,9):
        if posicionValidaLibre(tablero, i):
            return False
    return True


print("Bienvenido!")
 
while True:
    limTablero = [' '] * 9 
    letraJugador, letraMaquina = elegirLetra()
    turno = vaPrimero()
    print( turno + ' Va a tirar primero')
    juegoEnProceso = True
  
 
    while juegoEnProceso:
        if turno == 'jugador':
            # Player's turn.
            dibujarTablero(limTablero)
            posicion = movimientoJugador(limTablero)
            moverLetra(limTablero, letraJugador, posicion)
 
            if esGanador(limTablero, letraJugador):
                dibujarTablero(limTablero)
                print('HAS GANADO, FELICIDADES!')
                juegoEnProceso = False
            else:
                if tableroLleno(limTablero):
                    dibujarTablero(limTablero)
                    print('EMPATE')
                    break
                else:
                    turno = 'maquina'
 
        else:
            # Computer's turn.
            posicion = movimientoMaquina(limTablero, letraMaquina)
            moverLetra(limTablero, letraMaquina, posicion)
 
            if esGanador(limTablero,letraMaquina):
                dibujarTablero(limTablero)
                print('Gano la Maquina, HAS PERDIDO!')
                juegoEnProceso = False
            else:
                if tableroLleno(limTablero):
                    dibujarTablero(limTablero)
                    print('EMPATE!')
                    break
                else:
                    turno = 'jugador'


        

    if not jugarDeNuevo():
        maquinaMaquina()
        break


   
