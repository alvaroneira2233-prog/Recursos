```python
class Personaje:
    nombre = "default"
    vida = 0
    fuerza = 0
    inteligencia = 0
    defensa = 0
#colocamos dos giones bajos(__) antes de el atributo para que este sea privado y nadie pueda modificarlo 
#lamentablementeben python no se puede poner privado de verdad solo lo aparenta
    def __init__(self, nombre, vida, fuerza, inteligencia, defensa):
        self.nombre = __nombre 
        self.vida = __vida     
        self.fuerza = __fuerza
        self.inteligencia = __inteligencia
        self.defensa = __defensa

    def atributos(self):
        print(self.__nombre , ":", sep="")
        print("vida", self.__vida)
        print("fuerza", self.__fuerza)
        print("inteligencia", self.__inteligencia)
        print("defensa", self.__defensa)

    def subir_nivel(self, vida, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def estar_vivo(self):
        self.__vida > 0 

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ah muerto")
        

    def daño(self, enemigo):
        return self.__fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ah realizado", daño, "puntos de daño a ", enemigo.__nombre)
        print("la vide de ", enemigo.__nombre, "es", enemigo.__vida)
        if enemigo.esta_vivo():
            print("la vida de", enenmigo.__nombre, "es", enemigo.__vida)

        else:
            enemigo.morir()
        #el metodo get esta para que nos devulva el atributo
        def get_fuerza(self):
          return self.__fuerza
        #y el metodo set recibira uno nuevo para cambiarlo por el actual 
        def set_fuerza(self, fuerza):
          if fuerza < 0:
            print("error en la fuerza")

          else:
              self.__fuerza = fuerza<

mi_personaje = personaje("pedro", 20, 10, 5, 10)
mi_enemigo = personaje("maduro", 5, 5, 5, 5)

mi_personaje.set_fuerza(-5)
mi_personaje.atributos()

# aunque en principio no se deberia poder cambiar un metodo o atributo en privado, (recordando que es ponendo dos "__" antes del
#atributo o metodo que queramos poner en privado) en python aun se pueden acceder con ciertos comandos, aun asi no se deberia de
#poder acceder a esos archivos en cualquier otro programa 

``` 
