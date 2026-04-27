´´´python
class Componente:
    def __init__(self, nombre, marca, precio, stock):
        # Atributos privados
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__marca = marca

    # --- GETTER Y SETTER PARA PRECIO (Encapsulamiento completo) ---
    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    # --- MÉTODOS DE ACCIÓN Y CÁLCULO ---
    
    # Método 1: Vender (Resta del stock)
    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Venta realizada. Quedan {self.__stock} unidades.")
        else:
            print("Stock insuficiente.")

    # Método 2: Aplicar Descuento (Cálculo matemático)
    def aplicar_descuento(self, porcentaje):
        descuento = self.__precio * (porcentaje / 100)
        self.__precio -= descuento
        print(f"Descuento del {porcentaje}% aplicado. Nuevo precio: ${self.__precio}")

    # Método 3: Valor Total de Bodega (Cálculo matemático)
    def calcular_valor_inventario(self):
        total = self.__precio * self.__stock
        print(f"El valor total en stock de {self.__nombre} es: ${total}")

# --- INSTANCIACIÓN ---
comp1 = Componente("Ryzen 5", "AMD", 150000, 10)
comp2 = Componente("RTX 4060", "NVIDIA", 350000, 5)

# Demostración
comp1.vender(2)
comp1.aplicar_descuento(10)
comp1.calcular_valor_inventario()

comp2.vender(1)
comp2.calcular_valor_inventario()
´´´
