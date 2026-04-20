class Personaje:
    nombre = "default"
    vida = 0
    fuerza = 0
    inteligencia = 0
    defensa = 0

    def __init__(self, nombre, vida, fuerza, inteligencia, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa

    def atributos(self):
        print(self.nombre , ":", sep="")
        print("vida", self.vida)
        print("fuerza", self.fuerza)
        print("inteligencia", self.inteligencia)
        print("defensa", self.defensa)

    def subir_nivel(self, vida, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def estar_vivo(self):
        self.vida > 0 

    def morir(self):
        self.vida = 0
        print(self.nombre, "ah muerto")
        

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ah realizado", daño, "puntos de daño a ", enemigo.nombre)
        print("la vide de ", enemigo.nombre, "es", enemigo.vida)
        if enemigo.esta_vivo():
            print("la vida de", emnmigo.nombre, "es", enemigo.vida)

        else:
            enemigo.morir()
    
mi_personaje = Personaje("personaje1", 50, 20, 15, 20)
mi_enemigo = Personaje("carlos", 20, 10, 5, 10)
mi_personaje.atacar(mi_enemigo)
# mi_enemigo.atributos()
