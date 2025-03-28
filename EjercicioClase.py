

class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa) 
        print("Vida:", self.vida)       
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
        
mi_personaje = Personaje("AGES", 150, 50, 100, 200)
mi_personaje.subir_nivel(50, 25, 20)
mi_personaje.atributos()

