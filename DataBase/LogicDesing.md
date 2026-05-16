# tablas de base de datos
estas son la base principal para la recopilacion de datos, estas son similares a las clases, solo que aqui los atributos 
pasarian a ser los datos a recopilar, es importante recordar que al hacer un a tabla hay q darle un id a cada dato guerdado en ella
para que no se nos confunda en los registros

## tabla de ejemplo

## ejemplo de mer 
![Flowchart]

## por que usar float?
en sese caso era mejor float ya que permite el uso de numeros decilames, mientras q int solo maneja numeros enteros
asi pudiendo poner 0,2 para representar meses, aun asi esta mal por que puede llegar a aser confuso y en un atabla de verdad
es mas recondable utilizar "DATE" que esta especializado en el uso de fechas 

## problema de edad
el problema con ingresar directamente edad es que en una base de datos eso se guardara cin ese numero y lo mantendra sin cambios
lo cual generaria confucion con el tiempo al tener que esatr sacando cuentas manualmente,es mejor colocar fecha de nacimiento
asi es mas facil ver la edad sin complicacionesde renovar la informacion constantemente

## dato vs realidad
el problema al poner float en la edad osea numeros decimales como 0.5 es que es la mitad de un numero entero cuadno el año tiene 12 meses
asi que nos diria feliz cumpleaños cada 5 meses

## ¿para qué tipo de relación se utiliza realmente una tabla intermedia como la que creamos en clase MASCOTA_TUTOR
Una tabla intermedia (también conocida como tabla asociativa, tabla pivote o junction table) se utiliza única y exclusivamente para resolver relaciones de Muchos a Muchos (N:M).

En las bases de datos relacionales, los motores de búsqueda no pueden interpretar una relación directa de "Muchos a Muchos" entre dos tablas. Para romper ese "bloqueo", la teoría de normalización nos obliga a transformarla en dos relaciones de "Uno a Muchos" usando una tabla intermedia.

##  Contexto de Negocio
caso A:
en la veterinaria solo dejan  tener un dueño por mascota lo que nos da una cardinalidad de (1..1) ya que obligatoriamente solo puede haber una mascota por dueño, y un dueño por mscota.

caso B:
en el hotel dejan que varios dueños puedan retirar a un amascota y aque a su vez el dueño pueda tener mas de una mascota, esto nos da una relaciond de (n..m) ya que la mascota tiene varios dueños y el dueño puede tener varias mascotas 
 

















