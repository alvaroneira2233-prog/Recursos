# lo que entendi y no entendi
que es poo, para recordar primero dividiremos en dos el codigo: atributos y metodos, los atributos son las caracteristicas del objeto
mientras que elmetodo son las acciones que puede hacer 
ej: 
atributos de una manzana: peso, color cantidad
matodos: agararla(), morderla(), tirarla()

para darle esos valores utilizamos el metodo "constuctor()" que va a variar el nombre depediendo del lenguaje de programacion
importante que para ver los atibutos del objeto se acccede mediante (nombredelobjeto. ) despues del punto se coloca lo que se quiera
hacer con el atributo: verlo, modificarlo o utilizarl el metodo.

# 1:abstraccion 
---
entendi: al crear un objeto hay que ser directo con la informacion de los atributos osea "abstraerce" de poner informacion de mas
recordando que ene metodos siempre tiene que ir el "construcctor()"
entonces en la abstraccion solo vemos cuales seran los atributos y metodos que definiran al objeto


no entendi:

---

# 2:encapsulacion
---
entendi: este funciona para definir si el funcionamiento de los metodos o atributos pueden o no ser mdodificables y como modificarlos
en caso de que queramos modiicar un atributo se utilisan comandos como: "get"(para ver el atributo) y "set"(para modificarlo) 
de igual forma funciona con los metodos para que no se puedan modificar ciertas acciones,
entonces si no declaramos los atributos como privados se les podira hacer cualquier modificacion desde el . (recordando que apra acceder
a la informacion de un objeto utilizamos "nombre_del_objeeto. ") pero al ponerlo en privado estos solamente se podiran modificar mediante 
el comando "get" y "set", tambien la forma de volverlos publicos o privaods depende del lenjuage 


no entendi: como volver un metodo privado

---

# 3:herencia
---
entendi: en principio es una forma de reciclar atributos y metodos, en caso de que se le squiera hacer modificaciones a las copias solamente
hay que agregarles los metodos y atributos nuevos, al objeto original se le llama "clase padre" o "superclase" y a las copias modificadas 
se les dice "clase hija" o "subclase"

no entendi:

---

# 4:polimorfismo
---
entendi: sirve para que de una misma accion o atributo se pueda desenbucar en distintos resultados dependiendo de que le modifiquemos, tambien
es importante definir el tipo de la variable ya que las variables que sean diferentes no seran compatibles, solo los erian variables del mismo tipo
ej: atracar, tendremos tres personajes 
mago: inteligencia (atacar*inteligencia = 40)
gerrero: fuerza (atacar*fuerza = 45)
sacerdote: fe (atacar*fe = 60)
 los tres utilizaran el mismo comado de atacar, pero cada uno tendra una estadistica distinta por sus atributos y asi nos ahorrariamos hacer 
 muchas funciones por cada ejemplo

no entendi

---
