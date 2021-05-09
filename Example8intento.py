#Ejercicio prueba 3.8
print("Buen dia")
#Datos de entrada
años=int(input("Porfavor ingrese los años de labor que tiene en la empresa:"))
sueldo=float(input("Ingrese el sueldo que recibe por parte de la empresa:"))

#Variables

bonoañomenor=0.20
bonoñormayor=0.30
sueldo1=0.25
sueldo2=0.15
sueldo3=0.10
bonofinal=0.0

#Proceso

if años>2 and años<5:
  bonoalsueldo=sueldo*bonoañomenor
  if sueldo<1000:
    bonofinal=bonoalsueldo*sueldo1
  elif sueldo>1000 and sueldo<=3500:
    bonofinal=bonoalsueldo*sueldo2
  elif sueldo>3500:
    bonofinal=bonoalsueldo*sueldo3
if años>=5:
  bonoalsueldo=sueldo*bonoñormayor
  if sueldo<1000:
    bonofinal=bonoalsueldo*sueldo1
  elif sueldo>1000 and sueldo<=3500:
    bonofinal=bonoalsueldo*sueldo2
  elif sueldo>3500:
    bonofinal=bonoalsueldo*sueldo3
if 
#Datos de salida
print(f"El bono que recibira es ${bonofinal:.2f}")