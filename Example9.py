print("Bienvenido estimado cliente")
#Variables
cobertAmpli=0
cobertTerc=0
planA=1200
planB=950
alcohol1=0.10
lentes1=0.05
enfermedad1=0.05
anhosmayor=0.20
anhosmenor=0.10
#Proceso
seguro=("Estamos ofreciendo dos tipos de seguro, porfavor elija el que le sea mas conveniente:\nCA=Cobertura Amplia\nCT=Cobertura Terciaria")
años=("Porfavor ingrese cuantos años tiene:")
alcohol=("Usted frecuenta beber alcohol:\nSi frecuenta=Si\nNo frecuento=No")
lentes=("Usted utiliza lentes o gafas:\nSi utilizo=Si\nNo utilizo=No")
enfermedad=("Usted tiene alguna deficiencia cardiaca o tiene diabetes:\nDeficiencia cardiaca=DF\nDiabetes=DIAB")
#Proceso
if años>40 and seguro=="CA":
  cobertAmpli=(planA)+(alcohol"Si",planA*alcohol1)+(lentes"Si",planA*alcohol1*lentes1)+(enfermedad"Si",planA*alcohol1*lentes1*enfermedad1)+(planA*alcohol1*lentes1*enfermedad1*anhosmayor)
elif años>40 and seguro=="CA":
  cobertAmpli=(planA)+(alcohol"No",planA*alcohol1)+(lentes"No",planA*alcohol1*lentes1)+(enfermedad"No",planA*alcohol1*lentes1*enfermedad1)+(planA*alcohol1*lentes1*enfermedad1*anhosmayor)
if años<=40 and seguro=="CA":
  cobertAmpli=(planA)+(alcohol"Si",planA*alcohol1)+(lentes"Si",planA*alcohol1*lentes1)+(enfermedad"Si",planA*alcohol1*lentes1*enfermedad1)+(planA*alcohol1*lentes1*enfermedad1*anhosmenor)
elif años<=40 and seguro=="CA":
  cobertAmpli=(planA)+(alcohol"No",planA*alcohol1)+(lentes"No",planA*alcohol1*lentes1)+(enfermedad"No",planA*alcohol1*lentes1*enfermedad1)+(planA*alcohol1*lentes1*enfermedad1*anhosmenor)

if años>40 and seguro=="CT":
  cobertTerc=(planB)+(alcohol"Si",planB*alcohol1)+(lentes"Si",planB*alcohol1*lentes1)+(enfermedad"Si",planB*alcohol1*lentes1*enfermedad1)+(planB*alcohol1*lentes1*enfermedad1*anhosmayor)
elif años>40 and seguro=="C":
  cobertTerc=(planB)+(alcohol"No",planB*alcohol1)+(lentes"No",planB*alcohol1*lentes1)+(enfermedad"No",planB*alcohol1*lentes1*enfermedad1)+(planB*alcohol1*lentes1*enfermedad1*anhosmayor)
if años<=40 and seguro=="CA":
  cobertTerc=(planB)+(alcohol"S",planB*alcohol1)+(lentes"Si",planB*alcohol1*lentes1)+(enfermedad"Si",planB*alcohol1*lentes1*enfermedad1)+(planB*alcohol1*lentes1*enfermedad1*anhosmenor)
elif años<=40 and seguro=="CA":
  cobertTerc=(planB)+(alcohol"No",planB*alcohol1)+(lentes"No",planB*alcohol1*lentes1)+(enfermedad"No",planB*alcohol1*lentes1*enfermedad1)+(planB*alcohol1*lentes1*enfermedad1*anhosmenor)
#Datos de salida
print("Este es el costo del seguro que usted eligio:")