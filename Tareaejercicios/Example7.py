#Ejercicio 3.7
print("Hola, sea bienvenido al sistema de becas que ha concedido el presidente de la república")
#Datos de entrada
edad=int(input("Por favor ingrese su edad:"))
promedio=float(input("Porfavor ingrese su promedio:"))
bono=0
bonomayor1=2000.00
bonomayor2=1000.00
bonomayor3=500.00
bonomenor1=3000.00
bonomenor2=2000.00
bonomenor3=100.00
recomendación=("estimado estudiante le motivo para que usted pueda seguir esforzandose un poco mas.")
#Proceso
if edad>18 and promedio>=9.0:
  bono=print(f"Usted a sido acreedor de ${bonomayor1:.2f}")
elif edad>18 and promedio>=7.5:
  bono=print(f"Usted a sido acreedor de ${bonomayor2:.2f}")
elif edad>18 and promedio<7.5 and promedio>=6.0:
 bono=print(f"Usted a sido acreedor de ${bonomayor3:.2f}") 
if edad<=18 and promedio>=9.0:
 bono=print(f"Usted a sido acreedor de ${bonomenor1:.2f}") 
elif edad<=18 and promedio<9.0 and promedio>=8.0:
 bono=print(f"Usted a sido acreedor de ${bonomenor2:.2f}") 
elif edad<=18 and promedio<8.0 and promedio>=6.0:
 bono=print(f"Usted a sido acreedor de ${bonomenor3:.2f}") 
elif promedio<6.0:
  print("Usted no fue aprobado,",recomendación)

