# switch/match case
es una condicional que busca entre varias opciones, primero evaluara un valor que ñe demos y lo comparara con todas las opciones que esten dentro del switch cuando  encuentre una 
coincidencia cuando encuentre uno que coincida va a ejecutar su instruccion
ej:
```python
dia = int(intput("ingrese el valor numerico de un dia de la semana: "))
match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
         print("dia de la semana inexisstente")
```
aparte le podemos agregar un caso por defecto, este vendria en la ultima linea y ponoendo un "_" asi si alguien pone un elemnto que no coincida con los casos se pondra este automaticamente
 ---
