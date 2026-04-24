```python
class Personaje:
    nombre = "default"
    vida = 0
    fuerza = 0
    inteligencia = 0
    defensa = 0
## aqui va el costructor el (__init__) 
    def __init__(self, nombre, vida, fuerza, inteligencia, defensa):
        self.nombre = nombre #el self. sirven parar acceder a tanto atributo como a metodos de la clase  
        self.vida = vida     
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
# el def es para que lo tome como una funcion
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
        if enemigo.estar_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)

        else:
            enemigo.morir()
    

class guerrero(Personaje):
    
    def __init__ (self, nombre, vida, fuerza, inteligencia, defenza, espada):
        super().__init__( nombre, vida, fuerza, inteligencia, defenza)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("elije un arma: (1) pata de mesa, daño 8. (2) la insanita, daño 15"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 15
        else: 
            print("numero equivocado")

    def atributos(self):
        return super().atributos()  
        print("espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
        
escritorio = guerrero("escritorio", 50, 45, 5, 30, 5)
class mago(Personaje):

    def __init__(self, nombre, vida, fuerza, inteligencia, defensa, libro):
        super().__init__(nombre, vida, fuerza, inteligencia, defensa)
        self.libro = libro 

    def atributos(self):
        super().atributos()
        print("libro", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
class marginado(Personaje):
    def __init__(self, nombre, vida, fuerza, inteligencia, defensa, palo):
        super().__init__(nombre, vida, fuerza, inteligencia, defensa)
        self.palo = palo

    def atributos(self):
        return super().atributos()
        print("palo", self.palo)

    def daño(self, enemigo):
        return self.fuerza*self.palo - enemigo.defensa

juan = marginado("juan", 20, 15, 15,30, 5)
carlos = Personaje("carlos", 20, 15, 10, 10)
escritorio = guerrero("escritorio", 50, 45, 5, 30, 5)
mango = mago("mango", 25, 5, 40, 10, 5)
juan.atacar(carlos)
carlos.atacar(escritorio)
escritorio.atacar(mango)
mango.atacar(juan)
juan.atributos()
carlos.atributos()
escritorio.atributos()
mango.atributos()

```
