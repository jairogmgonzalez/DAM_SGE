
class Jugador:
    
    def __init__(self, nombre, es_humano, simbolo):
        self.nombre = nombre # Almacena el nombre del jugador
        self.es_humano = es_humano # Atributo booleano para diferenciar entre el jugador real y la IA
        self.simbolo = simbolo # Almacena el simbolo del jugador
    
    
    # Método para representar al jugador con su nombre junto a su símbolo
    def __str__(self):
        return f"{self.nombre} ({self.simbolo})" if self.nombre else self.simbolo
       

    
    