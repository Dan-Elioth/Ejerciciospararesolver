print("Bienvenido al programa de bono al empleado de nuestra tienda")
#Variables
bono=0 
bono1=100 
bono2=200
bono3=300
bono4=400
bono5=500
bonomayor=1000
#Datos de entrada
años=float(input("Ingrese los años que labora en la tienda:"))
#Proceso
if años==1:
  bono=bono1
if años==2:
  bono=bono2
if años==3:
  bono=bono3
if años==4:
  bono=bono4
if años==5:
  bono=bono5
if años>5:
  bono=bonomayor
#Datos de salida
print(f"El bono con el que usted cuenta es de: ${bono:.2f}")
