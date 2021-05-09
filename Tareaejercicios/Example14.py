print("Buen dia estimado estudiante, vamos ver tu calificaciones en base a letras.")
#Variables
nota1="A"
nota2="B"
nota3="C"
nota4="D"
nota5="F"
#Datos de entrada
nota=int(input("Ingrese su nota:\nDel 0-10:\n"))
#Proceso
if nota==10:
  print("Felicidades obtuviste una calificación de:",nota1)
if nota==9:
  print("Felicidades obtuviste una calificación de:",nota2)
if nota==8:
  print("Tu puede amigo fuerzas, casi lo logras, tu nota es:",nota3)
if nota==7:
  print("Estimado alumno le motivo a que pueda seguir adelante y a poner un poco mas de empeño, su nota es:",nota4)
if nota==6:
  print("Estimado alumno le motivo a que pueda seguir adelante y a poner un poco mas de empeño, su nota es:",nota4)
if nota<=5:
  print("Estimado alumno le motivo para que usted tome enserio su estudio y no a la ligera por que saco una:",nota5)
