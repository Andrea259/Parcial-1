# Dfinimos la clase que utilizaremos 
class Tienda:
    def __init__(self):
        self.inventario = {}
        self.ventas = []

    def agregar_producto(self, nombre, cantidad, precio_sugerido):
        if nombre in self.inventario:
            self.inventario[nombre]['cantidad'] += cantidad
        else:
            self.inventario[nombre] = {'cantidad': cantidad, 'precio': precio_sugerido}
        print(f"Producto agregado: {nombre} - Cantidad: {cantidad} - Precio sugerido: {precio_sugerido}")

    def registrar_venta(self, nombre, cantidad):
        if nombre in self.inventario and self.inventario[nombre]['cantidad'] >= cantidad:
            total = cantidad * self.inventario[nombre]['precio']
            self.inventario[nombre]['cantidad'] -= cantidad
            self.ventas.append({'producto': nombre, 'cantidad': cantidad, 'total': total})
            print(f"Venta registrada: {nombre} - Cantidad: {cantidad} - Total: {total}")
            return total
        else:
            print(f"Error: No hay suficiente stock de {nombre} o el producto no existe.")
            return 0

    def calcular_vuelto(self, total, pago):
        if pago >= total:
            return pago - total
        else:
            print("Error: El pago es insuficiente.")
            return None

    def mostrar_inventario(self):
        print("\nInventario actual:")
        for producto, detalles in self.inventario.items():
            print(f"Producto: {producto} - Cantidad: {detalles['cantidad']} - Precio: {detalles['precio']}")

    def mostrar_ventas(self):
        print("\nHistorial de ventas:")
        for venta in self.ventas:
            print(f"Producto: {venta['producto']} - Cantidad: {venta['cantidad']} - Total: {venta['total']}")

# Acontinuacion muestro un ejemplo de como se aplicaria 

# Ejemplo de uso
tienda = Tienda()

# Agregar productos al inventario
tienda.agregar_producto("Manzana", 100, 0.5)
tienda.agregar_producto("Pan", 50, 1.0)
tienda.agregar_producto("Leche", 30, 1.5)

# Mostrar inventario
tienda.mostrar_inventario()

# Registrar una venta
total_venta = tienda.registrar_venta("Manzana", 10)

# Calcular vuelto
pago_cliente = 10
vuelto = tienda.calcular_vuelto(total_venta, pago_cliente)
print(f"Vuelto: {vuelto}")

# Mostrar ventas
tienda.mostrar_ventas()
