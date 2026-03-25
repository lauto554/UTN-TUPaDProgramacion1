 #Simular una compra con validaciones y cálculo de total.

print("########### SISTEMA DE CAJAS ##############")
total_productos_sin_descuento = 0
descuento_total = 0
productos = []
print()

nombre_cliente_input = input("Nombre del cliente: ")
nombre_cliente = nombre_cliente_input.strip()

###################### nombre ###################### 
while not nombre_cliente.isalpha() or nombre_cliente == "":
    print()
    print("Ingrese un nombre valido...(sin numeros, espacios ni vacio)La")
    print()
    nombre_cliente = input("Nombre del cliente: ").strip()
    print()

###################### cantidad productos ###################### 
cantidad_productos_input = input("Cantidad de Productos: ")

while not cantidad_productos_input.isdigit() or int(cantidad_productos_input) <= 0:
    print()
    print("La cantidad de productos debe ser un numero entero positivo")
    print()
    cantidad_productos_input = input("Cantidad de Productos: ")
    print()

######################  bucle for ###################### 
print("Ingresa precio del producto y si tiene descuento o no")
for producto in range(int(cantidad_productos_input)):
    print()
    print(f"Producto {producto + 1}")
    print()
    
    ###################### precio producto ###################### 
    precio_producto_input = input("Precio del Producto: ")
    
    while not precio_producto_input.isdigit() or precio_producto_input == "" or int(precio_producto_input) <= 0:
        print()
        print("Ingrese un precio válido mayor a 0...")
        print()
        precio_producto_input = input("Precio del Producto: ")
        print()

    total_productos_sin_descuento += int(precio_producto_input)
    
    ###################### descuento ###################### 
    tiene_descuento_input = input("Tiene descuento? (S/N): ")
    
    while tiene_descuento_input.lower() != "s" and tiene_descuento_input.lower() != "n" or tiene_descuento_input == "":
        print()
        print("Ingrese un dato valido(s para 'Si', n para 'NO')")
        print()
        tiene_descuento_input = input("Tiene descuento? (S/N): ")
        print()
    
        
    if tiene_descuento_input.lower() == "s":
        descuento_producto = int(precio_producto_input) * 0.1
        descuento_total += descuento_producto
        
    tiene_descuento_input = tiene_descuento_input.lower()
    productos.append([producto + 1,int(precio_producto_input),tiene_descuento_input])

print()
print("===================================================")
print()

print(f"Cliente: {nombre_cliente.capitalize()}")
print(f"Cantidad de Productos: {cantidad_productos_input}")

for p in productos:
    print(f"Producto {p[0]} - Precio: {p[1]}    Descuento (S/N): {p[2]}")

print(f"Total sin desc: ${total_productos_sin_descuento:.2f}")
print(f"Total con desc: ${total_productos_sin_descuento - descuento_total:.2f}")
print(f"Ahorro total: ${descuento_total:.2f}")
print(f"Promedio por producto: ${(total_productos_sin_descuento - descuento_total) / int(cantidad_productos_input):.2f}")

print()
print("===================================================")

    
    
    
    

    
#print(f"Nombre: {nombre_cliente} - Productos: {cantidad_productos}")