from Jugador import Jugador

class Casilla:
    
    def __init__(self):
        self.simbolo = ' ' # Almacena el símbolo que representará la casilla
        self.propietario = None # Almacena el propietario de la casilla
        self.es_borde = False # Atributo booleano para saber si una casilla está en el borde o no
        
    # Método para saber si la casilla está ocupada    
    def esta_ocupada(self):
        return self.propietario is not None
    
    # Método para ocupar la casilla por un jugador
    def ocupar_casilla(self, jugador):
        self.propietario = jugador
        self.simbolo = jugador.simbolo
        
        print(f"Casilla ocupada por {jugador.nombre}.")
        print()
    
    # Método para representar una casilla con su símbolo
    def __str__(self):
        return self.simbolo

    # Método para representar una casilla en cadena con su símbolo
    def __repr__(self):
        return f"Casilla(simbolo='{self.simbolo}')"
    