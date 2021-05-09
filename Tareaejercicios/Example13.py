print("Buenos dias estimados clientes veamos cuanto es el costo de nuestro servicio de autobuses, el cual es para su viaje de estudios")
#variables
costo=0
costo1=20
costo2=35
costo3=40
costo4=70
#Datos de entrada
alumnos=int(input("Porfavor necesito el numero exacto de los alumnos:"))
#Proceso
if alumnos>100:
  costo=costo1/alumnos
elif alumnos>=50 and alumnos<=100:
  costo=costo2/alumnos
elif alumnos>=20 and alumnos<=49:
  costo=costo3/alumnos
elif alumnos<20:
  costo=costo4/alumnos
#Datos de salida
print(f"El costo a pagar por alumno es de: ${costo:.2f}")