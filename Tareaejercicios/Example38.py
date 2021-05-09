#Ejercicio numero 3.8
print("Tenga usted buen día")
#Datos de entrada
años=int(input("Porfavor ingrese años completos de su labor en la empresa:"))
sueldo=float(input("Ingrese el sueldo que recibe por parte de la empresa:"))
#Variables

bonomenor=0.20
bonomayor=0.30
sueldo1=0.25
sueldo2=0.15
sueldo3=0.10
bonosueldo1=0.0
bonosueldo2=0.0
bonofinal=0.0
#Proceso
if años>2 and años<5:
  bonosueldo1=sueldo*bonomenor
elif años>=5:
  bonosueldo1=sueldo*bonomayor

#siguiente descuento del sueldo neto

if sueldo<1000:
  bonosueldo2=sueldo*sueldo1
elif sueldo>1000 and sueldo<=3500:
  bonosueldo2=sueldo*sueldo2
elif sueldo>3500:
  bonosueldo2=sueldo*sueldo3

#Indicando el mayor

if bonosueldo1>bonosueldo2:
  bonofinal=bonosueldo1
elif bonosueldo2>bonosueldo1:
  bonofinal=bonosueldo2

#Datos de salida
print(f"El bono que recibira es:${bonofinal:.2f}")