ejercicios
1:
```python 
temperatura = int(input(print("ingrese la temperatura actual de su procesador")))

if temperatura <40:
        print("temperatura normal")
elif temperatura >75:
        print("PELIGRO REVISE SUS VENTILADORES!!!")
else: 
        print ("temperatura elevada")
  ```
2:
```python
# 1. Definimos la variable 
numero_secreto = 3

print("adivine el numero")

while True:
    # 2. Pedimos el número y lo convertimos a entero
    numero_seleccionado = int(input("introduzca el numero: "))
    
    # 3. Comparamos
    if numero_seleccionado < numero_secreto:
        print("numero muy bajo intente de nuevo")
        
    elif numero_seleccionado > numero_secreto:
        print("numero muy alto intente de nuevo")
        
    else:
        print("felicidades encontraste el numero")
        break
```  
