```mermaid
classDiagram
    class Componente {
        -String nombre
        -String marca
        -float precio
        -int stock
        +__init__(nombre: String, marca: String, precio: float, stock: int)
        +get_nombre() String
        +get_marca() String
        +get_precio() float
        +get_stock() int
        +set_precio(nuevo_precio: float) void
        +vender(cantidad: int) bool
        +aplicar_descuento(porcentaje: float) float
        +calcular_valor_inventario() float
    }
```
## Guía rápida para leer este diagrama:
El bloque superior: Nombre de la clase (Componente).

El bloque medio (-): Son tus atributos privados. El símbolo - indica que no se pueden tocar desde fuera de la clase.

El bloque inferior (+): Son tus métodos públicos. El símbolo + significa que cualquier parte de tu programa puede llamarlos.

Tipos de datos: Después de los : verás si devuelve un texto (String), un número decimal (float), un entero (int) o un booleano (bool). Cuando un método no devuelve nada (solo hace una acción), se suele poner void o None.








