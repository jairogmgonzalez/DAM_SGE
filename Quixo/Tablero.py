from Casilla import Casilla

class Tablero:
    
    # Se inicializa directamente el tablero en una matriz 5x5 de Casillas
    def __init__(self):
        self.casillas = [[Casilla() for _ in range(5)] for _ in range(5)] 
        
        # Se establecen todos los bordes como las únicas casillas jugables
        for i in range(5):
            self.casillas[0][i].es_borde = True # Borde superior
            self.casillas[i][0].es_borde = True # Borde izquierdo
            self.casillas[4][i].es_borde = True # Borde inferior
            self.casillas[i][4].es_borde = True # Borde derecho
            
    
    # Método para mostrar el tablero
    def mostrar_tablero(self):
        # Muestra el índice de las columnas
        print("     0     1     2     3     4")  
        print("  +-----+-----+-----+-----+-----+")  

        for i, fila in enumerate(self.casillas):
            # Muestra el índice de las filas
            print(f"{i} |", end=" ")  
            for casilla in fila:
                # Si la casilla está ocupada por un jugador, mostrará la casilla con su símbolo, en caso contrario, la mostrará vacía
                if casilla.esta_ocupada():
                    print(f"[{casilla}] |", end=" ")  
                else:
                    print("[ ] |", end=" ")  
            print() 
            print("  +-----+-----+-----+-----+-----+")  
            
        print()
            
    
    # Método para mover la casilla desde la posición que introduzca hasta la dirección que elija
    def mover_casilla(self, fila, columna, direccion):
        # Se guarda la casilla que elija el jugador 
        casilla = self.casillas[fila][columna]
        
        # Si la dirección que elige es arriba
        if direccion == "arriba":
            
            # Se vacía la casilla actual
            self.casillas[fila][columna] = Casilla()
            
            # Se desplaza el resto de casillas hacia abajo
            for f in range(fila, 0, -1):
                self.casillas[f][columna] = self.casillas[f - 1][columna]
                # Se establece el atributo es_borde de la primera casilla desplazada a falso
                if f == fila:
                    self.casillas[f -1][columna].es_borde = False
            
            # Se establece la casilla de arriba como borde
            self.casillas[4][columna].es_borde = True 
            # Se coloca la casilla en la dirección final
            self.casillas[0][columna] = casilla
            
        
        # Si la dirección que elige es abajo
        if direccion == "abajo":
            
            # Se vacía la casilla actual
            self.casillas[fila][columna] = Casilla()
            
            # Se desplaza el resto de casillas hacia arriba
            for f in range(fila, 4):  
                self.casillas[f][columna] = self.casillas[f + 1][columna]
                # Se establece el atributo es_borde de la primera casilla desplazada a falso
                if f == fila:
                    self.casillas[f + 1][columna].es_borde = False
            
            # Se establece la casilla de arriba como borde
            self.casillas[0][columna].es_borde = True
            # Se coloca la casilla en la dirección final
            self.casillas[4][columna] = casilla
            
        
        # Si la dirección que elige es izquierda
        if direccion == "izquierda":
            
            # Se vacía la casilla actual
            self.casillas[fila][columna] = Casilla()

            # Se desplaza el resto de casillas hacia la derecha
            for c in range(columna, 0, -1):  
                self.casillas[fila][c] = self.casillas[fila][c-1]
                # Se establece el atributo es_borde de la primera casilla desplazada a falso
                if c == columna:
                    self.casillas[fila][c-1].es_borde = False
            
            # Se establece la casilla de la derecha como borde
            self.casillas[fila][4].es_borde = True 
            # Se coloca la casilla en la dirección final
            self.casillas[fila][0] = casilla 
        
        # Si la dirección es derecha
        if direccion == "derecha":
            
            # Se vacía la casilla actual
            self.casillas[fila][columna] = Casilla()
           
           # Se desplaza el resto de casillas hacia la izquierda
            for c in range(columna, 4): 
                self.casillas[fila][c] = self.casillas[fila][c+1]
                # Se establece el atributo es_borde de la primera casilla desplazada a falso
                if c == columna:
                    self.casillas[fila][c+1].es_borde = False
            
            # Se establece la casilla de la izquierda como borde
            self.casillas[0][columna].es_borde = True
            # Se coloca la casilla en la dirección final
            self.casillas[fila][4] = casilla
            
                
                    
                    


