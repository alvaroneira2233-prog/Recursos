---
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
    
---









