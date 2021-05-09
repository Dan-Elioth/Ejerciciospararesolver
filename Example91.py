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
  precioseguro=planA*anhosmayor
if alcohol=="Si":
  precioseguro=planA*anhosmayor*alcohol1
else:
  precioseguro=planA*anhosmayor
if lentes=="Si":
  precioseguro=planA*anhosmayor*alcohol1*lentes1
else:
  precioseguro=planA*anhosmayor
if enfermedad=="Si":
  precioseguro=planA*anhosmayor*enfermedad1
else:
  precioseguro=planA*anhosmayor