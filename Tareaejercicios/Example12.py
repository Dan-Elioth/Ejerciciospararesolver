print("Buenos dias")
#Variables
Pagofinal=0
pagointermedio=0
Pagofinalabso=0
#Datos de entrada
horas=int(input("Cuantas horas trabaja usted a la semana:"))
pago=int(input("Cuatos es la paga por hora:"))
#proceso

if horas>=41 and horas<=45:
  pagointermedio=(pago*2)
  if horas==41:
    Pagofinal=(pago*2)
  elif horas==42:
    Pagofinal=(pago*2*2)
  elif horas==43:
    Pagofinal=(pago*2*2*2)
  elif horas==44:
    Pagofinal=(pago*2*2*2*2)
  elif horas==45:
    Pagofinal=(pago*2*2*2*2*2)
if horas>=46 and horas<=50:
  Pagointermedio=(pago*3)
  if horas==46:
    Pagofinal=(pago*3)
  elif horas==47:
    Pagofinal=(pago*3*3)
  elif horas==48:
    Pagofinal=(pago*3*3*3)
  elif horas==49:
    Pagofinal=(pago*3*3*3*3)
  elif horas==50:
    Pagofinal=(pago*3*3*3*3*3)
if horas>50:
  print("Señor usted no esta permitido para poder trabajar mas de 50 horas de trabajo, porfavor acerquese al la gerencia para poder solucionar su caso, gracias.")
#Datos de salida
Pagofinalabso=Pagofinal+(horas*pago)
print(f"El pago por las horas de trabajo es ${Pagofinal:.2f}")

print(f"El pago total de la semana es: ${Pagofinalabso:.2f}")
