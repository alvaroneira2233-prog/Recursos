# operaciones basicas para pyton 
aprender y repasar: tipo, variables y operadores que utilizaremos en python recurrentemente

## los 4 tipos de datos mas importantes
---
* texto = string "str"
* entero = integer "int"
* racional = float 
* logico = boolean "bool"
---
## sus funciones 
---
str: sirve para hacer cadenas de caracteres que tienen que ir entre "" como: "hola mundo"

int: para utilizar numeros enteros como: -12, 42

float:para numeros con decimales: 3.1415, -20,2

bool: para true or false, 1 o 0 
---
## comentarios
a diferencia de psint en pyton se utiliza # para agregar comentarios que no sean leibles por el programa
ej:
```python
print("hola mundo")
# print("hola mundo")
```
todo lo que se escriba al lado de una almohadilla no se escribira cuando se ejecute el programa
## type
se utiliza para que al escribirlo antes de un dato este te doga que tipo de dato es 
ej:
```python
print(type"hola mundo")
```
este debedria decir que es un "str" y es aplicable a todos los tipos de datos
## variables
son contenedores de datos que puedes utilizar mas adelante su sintasis es
```python
caja = "carlos"
```
y luego utilizarse como
```python
print(carlos)
```
asi se escribira el valor que le hayamos agregado, en este caso "carlos"
recordando que no se le puede agregar cualquier nombre a la variable como empezar con numeros o _
y ciertos nombres que estan restringuidos por phyton
## operadores
operan utilizando datos tipo: numeros o variables
ej:
```python
print("suma:", 3 + 2)
```
ahi el programa realizara la suma y entregara el resultado 
tambien se pueden aplocar operadores como:
* 3 - 3 "resta"
* 3 * 3 "multipicacion"
* 3 / 3 "division"
* 3 ** 3 "potencia"
* 3 // 3 "suelo"
* 3 % 3 "modulo"
 esto mismo es aplicable y mas recomdable a variables para que no haya mucha confucion, es mejor poner "num_1"
a una variable para asignarle un valor numerico y hacer mas eficientemente los problemas, es importante recordar que se pueden utilizar varios operadores en una misma linea (respetando las reglas matemitacias) aunque si es que quisieras que un aoperacion especifica se haga antes puedes utilizar () para priorizarla 

## operadores relacionalaes
funcionan en base al true o false, en resumen que si una operacion es verdadera o falza ependiendo de que estemos haciendo 
ej:






estos sirven para la toma de deciciones 
# condicionales
---
## if
se utiliza en la toma de deciciones sindo if el "verdadero" y else "falso" entocies si no se cumple lo que se estipule en if automaticamente se ejecutara else
ej:
```python 
numero = int(intput("digite un numero:"))
if numero>0:
      print("el numero es positivo")
elif numero==0:
      print("el numero es cero")
else: 
      print("el numero es negativo")

print("fin del programa")
```

el "elif" es un agregado que puede ayudar si es que se necesite una tercera opcion en este caso al 0 no seer mayor que cero lo toma como negaivo lo 
cual es incorrecto , entonces utilizamos el elif para agregar que cero es cero y asi no tener un error 

---

# ciclo for
---
este se utiliza para hacer repeticiones en cadena, a diferencia de otros lenguajes en python se utiliza junto a collecciones, es decir lo que sea que queramos que repita tiene que si o si ir en una variable,
al lado en in se coloca la cantidad de veces que queramos repetir, en resumen lo que queramos que se repita 
ej:
```python
for i in [1,2,3,4,5]:
     print("hola mundo")
```

 tambien podemos ver el valor de cada numero en la colleccion poniendo la variable entre (), y tambien la coleccion puede ir por separado
ej: 
```python
coleccion = [1,2,3,4,5]
for i in coleccion:
     print(f"elemento:(i)")
```
---
# while 
--- 

















