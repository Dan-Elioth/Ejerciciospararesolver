#Ejercicio 3.4
def Exampleone01():
  #definir variables
  print("Cobro de estacionamiento")
  montoP=0
  #Datos de entrada
  horasX=int(input("Ingrese las horas que estuvo:"))
  #Proceso
  if horasX<=2:
    montoP=horasX*5
  elif horasX>2 and horasX<5:
    montoP=horasX*4
  elif horasX>=5 and horasX<10:
    montoP=horasX*3
  else:
    montoP=horasX*2
  #Datos de salida
  print("El monto a pagar cada uno del estacionamiento es:",montoP)

Exampleone01()