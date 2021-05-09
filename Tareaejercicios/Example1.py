#Ejercicio 3.1
def ejercicio01():
  print ("Como saber si puedes votar por tu edad")
  mensaje=""
  #Ingreso de datos
  edadP=int(input("ingrese la edad que tiene:"))
  #Proceso
  if edadP>=18:
    mensaje="Usted cuenta con la edad necesaria para registrar su voto"
  else:
    mensaje="Usted no tiene la edad minima para registrar su voto"
  print(mensaje)
ejercicio01()