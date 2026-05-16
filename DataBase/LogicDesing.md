# tablas de base de datos
estas son la base principal para la recopilacion de datos, estas son similares a las clases, solo que aqui los atributos 
pasarian a ser los datos a recopilar, es importante recordar que al hacer un a tabla hay q darle un id a cada dato guerdado en ella
para que no se nos confunda en los registros

## tabla de ejemplo

## ejemplo de mer 
![Flowchart](<img width="4000" height="3000" alt="imagen_2026-05-16_115821207" src="https://github.com/user-attachments/assets/9fbc0cc8-3688-446b-99b1-c13c5c9da360.png" />)

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


