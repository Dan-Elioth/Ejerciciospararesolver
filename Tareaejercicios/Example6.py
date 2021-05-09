#Ejercicio 3.6
#Definir variables y otros
print("Compras y descuentos de productos")
#Dartos de entrada
precioX=float(input("digite el precio: "))
#Proceso
if precioX>=200: 
 Descuento= precioX*0.15
elif precioX>100 and precioX<200:
 Descuento= precioX*0.12
elif precioX<100:
 Descuento= precioX*0.10
#Datos de salida
Precio_final= precioX - Descuento
print(f"El monto a pagar es de ${Precio_final:.2f}")