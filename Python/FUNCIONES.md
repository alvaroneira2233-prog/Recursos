## funciones 
---
las funciones sirven para crear listas de elemntos, ya sabiendo esto podemos hacer varias operaciones con la lista como medias aritmeticas o calcular varios datos sin la necesidad
de escribir codigo de mas 
ej:
```python
def puntuacion(clase):
    returm sum(clase) / len(clase)

clase = [7, 8, 9]
media = puntuacion(clase)
print("la puntuacion clase es:", media)
```
asi podemos crear funciones que sirvan de listas al poner returm se nos devolvemos la media, con "sum" le damos un argumento para que nos devuelva la suma de todos los numeros 
y para contar todos los elemnetos dentro de una lista utilizamos "len"

---
