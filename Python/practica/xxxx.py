ejercicios
1:Calculadora de temperatura de CPU
```python 
temperatura = int(input(print("ingrese la temperatura actual de su procesador")))

if temperatura <40:
        print("temperatura normal")
elif temperatura >75:
        print("PELIGRO REVISE SUS VENTILADORES!!!")
else: 
        print ("temperatura elevada")
  ```

2:Adivina el Número
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

3:Generador de Correos
```python 
nombre = input("Nombre: ").lower()
apellido = input("Apellido: ").lower()
empresa = input("Empresa: ").lower()
print(f"{nombre}.{apellido}@{empresa}.cl")
```

4:Filtro de Números Pares
```python
numeros = [3, 8, 15, 22, 7, 10]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(f"Números pares: {pares}")
```

5:Inventario de Videojuego
```python
inv = {"pociones": 5, "monedas": 100}
print(f"Tienes {inv['monedas']} monedas.")
inv["monedas"] += 50
print(f"Ahora tienes {inv['monedas']} monedas.")
```

6:Contador de Vocales
```python
frase = input("Frase: ").lower()
contador = 0
for letra in frase:
    if letra in "aeiou":
        contador += 1
print(f"Vocales encontradas: {contador}")
```

7:La Calculadora Modular
```python 
def sumar(a, b): return a + b
def dividir(a, b): 
    return a / b if b != 0 else "Error: Div por 0"

res = sumar(10, 5)
print(f"Resultado: {res}")
```

8:Cajero a Prueba de Fallos
```python
try:
    monto = int(input("Monto a retirar: "))
    print(f"Retirando ${monto}")
except ValueError:
    print("Error: Por favor ingresa solo números enteros.")
```

9:Validador de Contraseña
```python
psw = input("Crea tu clave: ")
tiene_numero = any(char.isdigit() for char in psw)

if len(psw) >= 8 and tiene_numero:
    print("Contraseña segura")
else:
    print("Falta longitud o un número")
```

10:Secuencia de Fibonacci
```python 
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
```








