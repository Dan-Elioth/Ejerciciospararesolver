#Ejercicio prueba 3.8
print("Buen dia")
#Datos de entrada
años=int(input("Porfavor ingrese sus años de laborr en la empresa:"))
sueldo=float(input("Ingrese el sueldo que recibe por parte de la empresa:"))
bonoañomenor=0.20
bonoñormayor=0.30
sueldo1=0.25
sueldo2=0.15
sueldo3=0.10
bonosemi1=0.0
bonosemi2=0.0
bonofinal=0.0
#Proceso
if años>2 and años<5:
  bonoalsueldo=sueldo*bonoañomenor
  if sueldo<1000:
    bonosemi1=bonoalsueldo*sueldo1
  elif sueldo>1000 and sueldo<=3500:
    bonosemi1=bonoalsueldo*sueldo2
  elif sueldo>3500:
    bonosemi1=bonoalsueldo*sueldo3
if años>=5:
  bonoalsueldo=sueldo*bonoñormayor
  if sueldo<1000:
    bonosemi2=bonoalsueldo*sueldo1
  elif sueldo>1000 and sueldo<=3500:
    bonosemi2=bonoalsueldo*sueldo2
  elif sueldo>3500:
    bonosemi2=bonoalsueldo*sueldo3
if bonosemi1>bonosemi2:
  bonofinal=bonosemi1
elif bonosemi2>bonosemi1:
  bonofinal=bonosemi2

#Datos de salida
print(f"El bono que recibira es ${bonofinal:.2f}")  