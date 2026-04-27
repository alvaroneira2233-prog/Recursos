# while 
--- 

primero cramos un archivo que termine en .py para programar en el, los ciclos while son bucles infinitos que solo se terminan al completar un aconcicion en especifica 
ej:
```python 
contraseña = "iguana"
while true:
       contraseña_input = input(introduzca una contraseña:)
       if contraseña _input == "iguana":
       print("contraseña correcta")
       break 

       else: print("contraseña incorrecta, introduzca la correcta down")
```
ahora si quisieramos agregarles intentos agregamos otra variable

```python 
contraseña = "iguana"
contador = 0

while true:
       contraseña_input = input(introduzca una contraseña:)

       contador +=1  

       if contador  > 3: 
          print("has sobrepasado los intentos")
 
 
       elif contraseña _input == "iguana":

       print("contraseña correcta")
       break 

       else
           print("contraseña incorrecta, introduzca la correcta down")
```
