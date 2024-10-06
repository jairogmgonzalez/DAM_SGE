import random
from Tablero import Tablero
from Jugador import Jugador
import time

class Quixo:
    
    # Se inicializa directamente el tablero, el jugador1 que seremos nosotros, el jugador IA y el contador de turnos
    def __init__(self):
        self.tablero = Tablero()
        self.jugador1 = self.crear_jugador('X')  # Crear jugador con símbolo 'X'
        self.jugadorIA = Jugador("Sistema", False, 'O')  # Crear IA con símbolo 'O'
        self.turno = 0
        
     # Método para inicializar el jugador1   
    def crear_jugador(self, simbolo):
        nombre = input("Por favor, introduce tu nombre: ")  # Solicitar nombre del jugador
        print()
        return Jugador(nombre, True, simbolo)  # Crear objeto Jugador con el nombre, símbolo y es_humano
    
    # Método para dar la bienvenida al jugador
    def bienvenida_partida(self):
        print(f"Bienvenido a QUIXO, {self.jugador1.nombre}, tu símbolo será: {self.jugador1.simbolo}.")
        print("Comenzando...")
        print()
        
    # Método principal para iniciar la partida
    def jugar(self):
        time.sleep(0.5)
        self.bienvenida_partida()
        time.sleep(1)
        
        # Bucle principal del juego, que no finalizará hasta que haya un ganador
        while True:

            # Verificar si es el turno del humano o de la IA
            if self.turno == 0 or self.turno % 2 == 0:
                # Turno del jugador humano
                self.turno_jugador()
                print()
                time.sleep(1)
            else:
                # Turno de la IA
                self.turno_IA()
                print()
                time.sleep(1)
            
            # Se verifica si hay un ganador y se muestra el tablero final
            if self.verificar_ganador():
                print()
                self.tablero.mostrar_tablero()
                break

            time.sleep(0.5)
                
            # Se incrementa el turno después de cada jugada
            self.turno += 1
    
    # Método para obtener el jugador del turno actual      
    def obtener_jugador_actual(self):
        return self.jugador1 if self.turno % 2 == 0 else self.jugadorIA
    
    # Método donde se encuentra la lógica del turno del jugador
    def turno_jugador(self):
        # Se indica quien tiene el turno actal
        print("Turno: ", self.obtener_jugador_actual())
        print()
        # Se muestra el tablero para que el jugador tenga una representación visual de él antes de elegir una casilla
        self.tablero.mostrar_tablero()
        
        print()
        
        # Paso 1: Se pregunta qué casilla desea ocupar
        fila, columna = self.preguntar_casilla()
        
        time.sleep(1)

        # Paso 2: Se marca la casilla como ocupada por el jugador si no está ocupada, en caso contrario se indica que ya es de su propiedad
        if not self.tablero.casillas[fila][columna].esta_ocupada():
            self.tablero.casillas[fila][columna].ocupar_casilla(self.jugador1)
        else:
            print("Esta casilla ya te pertenece, por lo que puedes cambiar su dirección.")
            print()
        
        # Se vuelve a mostrar el tablero para que vea la posición actual de su casilla antes de elegir la dirección final
        time.sleep(1)
        self.tablero.mostrar_tablero()
        time.sleep(1)
        
        # Paso 3: Se pregunta por la dirección final de su casilla y se muestra la decisión
        direccion = self.elegir_direccion(fila, columna)
        print()
        print(f"{self.jugador1.nombre} ha elegido la dirección: {direccion}")
        
        time.sleep(0.5)
        # Paso 4: Se mueve la ficha en la dirección elegida
        self.tablero.mover_casilla(fila, columna, direccion)
        
    
    # Método donde se encuentra la lógica de la IA
    def turno_IA(self):
        # Se indica quien tiene el turno actal
        print("Turno: ", self.obtener_jugador_actual()) 
        print()
        # Se muestra el tablero para tener una representación visual antes de que la IA elija una casilla
        self.tablero.mostrar_tablero()
        
        print()
        
        # Paso 1: Se pregunta por la casilla
        fila, columna = self.preguntar_casilla()
        
        time.sleep(1)

        # Paso 2: Se marca la casilla como ocupada por la IA si no está ocupada, en caso contrario se indica que ya es de su propiedadr
        if not self.tablero.casillas[fila][columna].esta_ocupada():
            self.tablero.casillas[fila][columna].ocupar_casilla(self.jugadorIA)
        else:
            print("Esta casilla ya te pertenece, por lo que puedes cambiar su dirección.")
            print()
        
        # Se vuelve a mostrar el tablero para ver la posición actual de su casilla antes de elegir la dirección final
        time.sleep(1)
        self.tablero.mostrar_tablero()
        time.sleep(1)
        
        # Paso 3: Se pregunta por la dirección final de su casilla y se muestra la decisión
        direccion = self.elegir_direccion(fila, columna)
        print()
        print(f"{self.jugadorIA.nombre} ha elegido la dirección: {direccion}")
        
        time.sleep(0.5)
        # Paso 4: Se mueve la casilla en la dirección elegida
        self.tablero.mover_casilla(fila, columna, direccion)
        time.sleep(1)
        

    # Método para preguntar la casilla que se quiere ocupar
    def preguntar_casilla(self):
        # Se verifica si es el turno del jugador
        if self.obtener_jugador_actual().es_humano:
            # Bucle en el que se pregunta la posición de la casilla hasta que no elija una casilla jugable
            while True:
                try:
                    fila = int(input("Introduce la fila que deseas (0-4): "))
                    columna = int(input("Introduce la columna que deseas (0-4): "))
                except ValueError:
                    print("Por favor, introduce un número válido.")
                    continue  # Vuelve al inicio del bucle
                
                # Se verifica si la posición de la casilla se encuentra entre el rango 0-4 (casillas jugables), en caso contrario, se repite el bucle
                if fila < 0 or fila > 4 or columna < 0 or columna > 4:
                    print("Por favor, introduce una fila y columna en el rango correcto (0-4)")
                    continue
            
                # Se verifica si la casilla está en el borde y, o bien es propiedad del jugador, o bien está vacía, en tal caso, se devolverá la posición de la casilla
                if self.tablero.casillas[fila][columna].es_borde and \
                (self.tablero.casillas[fila][columna].propietario == self.obtener_jugador_actual() 
                or not self.tablero.casillas[fila][columna].esta_ocupada()):
                    print("Fila: " + str(fila) + " Columna: " + str(columna))
                    print()
                    return fila, columna
                # Si no se cumple ninguna de las condiciones anteriores, se volverá a preguntar por una casilla válida
                else:
                    print("La casilla está ocupada por tu rival o no es jugable. Por favor, elige otra casilla.")
                    
        # Si es el turno de la IA:            
        else: 
            # Bucle en el que elige una casilla hasta que ésta sea válida
           while True:
            # Se elige una posición aleatoria entre 0 y 4 (casillas jugables) para la fila y columna de la casilla
            fila = random.randint(0, 4)
            columna = random.randint(0, 4)
            # Se verifica si la casilla es jugable y, o bien es propiedad de la IA, o bien está vacía, en tal caso, se devolverá la posición de la casilla
            if self.tablero.casillas[fila][columna].es_borde and \
            (self.tablero.casillas[fila][columna].propietario == self.obtener_jugador_actual() 
            or not self.tablero.casillas[fila][columna].esta_ocupada()):
                    print("Fila: " + str(fila) + " Columna: " + str(columna))
                    print()
                    return fila, columna
            # Si no se cumple ninguna de las condiciones anteriores, se repite el bucle
            else:
                continue
              
                
    # Método para elegir la dirección final de la casilla
    def elegir_direccion(self, fila, columna):
        # Se guarda en un diccionario todas las direcciones
        direcciones = {
            1: "arriba",
            2: "abajo", 
            3: "izquierda",
            4: "derecha"
        }

        # Lista donde se guardará las direcciones validas de la casilla actual
        direcciones_validas = []
    
        # Se determina a través de varias condiciones las direcciones válidas según la posición y se guardan en una lista
        if fila == 0 and columna == 0: # Borde superior izquierdo
            direcciones_validas = [2, 4]  # Abajo, Derecha
        elif fila == 0 and columna == 4: # Borde superior derecho
            direcciones_validas = [2, 3]  # Abajo, Izquierda
        elif fila == 4 and columna == 0: # Borde inferior izquierdo
            direcciones_validas = [1, 4]  # Arriba, Derecha
        elif fila == 4 and columna == 4: # Borde inferior derecho
            direcciones_validas = [1, 3]  # Arriba, Izquierda
        elif fila == 0:  # Borde superior entre las esquinas
            direcciones_validas = [2, 3, 4]  # Abajo, Izquierda, Derecha
        elif fila == 4:  # Borde inferior entre las esquinas 
            direcciones_validas = [1, 3, 4]  # Arriba, Izquierda, Derecha
        elif columna == 0:  # Borde izquierdo entre las esquinas
            direcciones_validas = [1, 2, 4]  # Arriba, Abajo, Derecha
        elif columna == 4:  # Borde derecho entre las esquinas
            direcciones_validas = [1, 2, 3]  # Arriba, Abajo, Izquierda

        # Se muestra las direcciones disponibles desde la casilla actual
        print("Direcciones disponibles:")
        for indice in direcciones_validas:
            print(f"{indice}: {direcciones[indice]}")
        
        print()

        # Se verifica si es el turno del jugador
        if self.obtener_jugador_actual().es_humano:
            # Bucle en el que se pide una dirección hasta que no sea válida
            while True:
                try:
                    opcion = int(input("Elige una opción (1-4): "))  # Se convierte la entrada a int

                    # Se verifica si la opción elegida está entre las disponibles, en caso contrario, se vuelve a repetir el bucle
                    if opcion not in direcciones_validas:
                        print("Por favor, introduce una opción válida:")
                        continue
                    
                    # Si la dirección es válida, se guarda y se devuelve
                    direccion = direcciones[opcion]
                
                    return direccion
                
                except ValueError:
                    print("Por favor, introduce un número válido.")
        
        # Si es el turno de la IA:
        else: 
            # Bucle en el que elige una dirección hasta que ésta sea válida
            while True:
                opcion = random.choice(direcciones_validas)

                # Se verifica si la opción elegida está entre las disponibles, en caso contrario, se vuelve a repetir el bucle
                if opcion not in direcciones_validas:
                    continue
                
                # Si la dirección es válida, se guarda y se devuelve
                direccion = direcciones[opcion]
                return direccion

    # Método para verificar si alguna fila entera pertenece a un mismo jugador
    def verificar_filas(self):
        # Se itera sobre cada fila
        for fila in self.tablero.casillas:
            simbolo = fila[0].simbolo  # Se guarda el símbolo de la primera casilla de la fila
            # Se verifica si no es una casilla vacía y si el resto de casillas tienen el mismo símbolo que la primera casilla de la fila
            if simbolo != ' ' and all(casilla.simbolo == simbolo for casilla in fila):
                if simbolo == self.jugador1.simbolo:
                    return self.jugador1
                elif simbolo == self.jugadorIA.simbolo:
                    return self.jugadorIA
            
        return None  # No hay fila que pertenezca a un mismo jugador

    # Método para verificar si alguna columna entera pertenece a un mismo jugador
    def verificar_columnas(self):
        # Se itera sobre cada columna
        for col in range(5): 
            simbolo = self.tablero.casillas[0][col].simbolo  # Se guarda el símbolo de la primera casilla de la columna
            # Se verifica si no es una casilla vacía y si el resto de casillas tienen el mismo símbolo que la primera casilla de la columna
            if simbolo != ' ' and all(self.tablero.casillas[fila][col].simbolo == simbolo for fila in range(5)):
                if simbolo == self.jugador1.simbolo:
                    return self.jugador1
                elif simbolo == self.jugadorIA.simbolo:
                    return self.jugadorIA
        
        return None  # No hay columna que pertenezca a un mismo jugador
    
    # Método para verificar si una de las 2 diagonales pertenece a un mismo jugador
    def verificar_diagonales(self):
        # Diagonal principal (de [0][0] a [4][4])
        simbolo = self.tablero.casillas[0][0].simbolo # Se guarda el símbolo de la primera casilla de la diagonal
        # Se verifica si no es una casilla vacía y si el resto de casillas tienen el mismo símbolo que la primera casilla de la diagonal
        if simbolo != ' ' and all(self.tablero.casillas[i][i].simbolo == simbolo for i in range(5)):
            if simbolo == self.jugador1.simbolo:
                return self.jugador1
            elif simbolo == self.jugadorIA.simbolo:
                return self.jugadorIA

        # Diagonal secundaria (de [0][4] a [4][0])
        simbolo = self.tablero.casillas[0][4].simbolo# Se guarda el símbolo de la primera casilla de la diagonal
        # Se verifica si no es una casilla vacía y si el resto de casillas tienen el mismo símbolo que la primera casilla de la diagonal
        if simbolo != ' ' and all(self.tablero.casillas[i][4 - i].simbolo == simbolo for i in range(5)):
            if simbolo == self.jugador1.simbolo:
                return self.jugador1
            elif simbolo == self.jugadorIA.simbolo:
                return self.jugadorIA
        
        return None  # No hay diagonal que pertenezca a un mismo jugador

    # Método para verificar si hay un ganador
    def verificar_ganador(self):
        # Se verifica si hay ganador horizontalmente
        ganador = self.verificar_filas()
        # Si hay un ganador, se imprime el mensaje
        if ganador:
            print(f"¡HAY GANADOR! {ganador.nombre} ha conseguido unir 5 casillas horizontalmente, ¡enhorabuena!")
            return True # Se sale del método en caso de haber ganadr

        # Se verifica si hay ganador verticalmente
        ganador = self.verificar_columnas()
        # Si hay un ganador, se imprime el mensaje
        if ganador:
            print(f"¡HAY GANADOR! {ganador.nombre} ha conseguido unir 5 casillas verticalmente, ¡enhorabuena!")
            return True # Se sale del método en caso de haber ganador

        # Se verifica si hay ganador en diagonales
        ganador = self.verificar_diagonales()
        # Si hay un ganador, se imprime el mensaje
        if ganador:
            print(f"¡HAY GANADOR! {ganador.nombre} ha conseguido unir 5 casillas diagonalmente, ¡enhorabuena!")
            return True # Se sale del método en caso de haber ganador
