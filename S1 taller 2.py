#Luis Fernando Soria Guaranga
#Ingeniería en Software

#ejemplo sintaxys

num=20 
if type(num)==int:
    print("respuesta: ",num*2)
else:
    print("El dato no es numerico")

def mensaje(men):
    print(men)

mensaje("mi primer programa")
mensaje("Mi segundo programa")

#ejemplo clase sintaxis

class Sintaxis:
    def userVariables(self):
        edad,_peso = 50, 70.50 
        print(edad,_peso)

ejer1= Sintaxis()
ejer1.userVariables()

#ejercicio VAriable de clases

class sintaxis:
    instancia=0

    def __init__(self,dato="Inicializacion"):
        self.frase=dato

    def usoVariables(self):
        edad, _peso = 50,70.5
        nombres = "Luis Soria"
        Tipo_sexo ="M"
        civil = False
        print(nombres,edad)



        #ejercicios tuplas

        usuario=()
        usuario=("simer",10003,"simer@gmail.com",True)
        usuario[3]="milagro"

        #Listas
        materias=[]
        materias=["Programacion web","PHP","POO"]
        materias[1]="Python"
        materias.append("Go")

        #diccionario
        docente={}
        docente={"nombre": "Daniel","edad":50,"fac":"faci"}
        docente["nombre"]="Ana"

        #print("""Mi nombre es {}, tengo {}
        #    años """.format(nombres,edad))
        print(usuario,materias,docente)
        print(usuario,usuario[0],usuario[0:2],usuario[-1])
        print(materias,materias[2:],materias[:1],materias[::],materias[-2:])


ejer1= Sintaxis()
ejer1.usoVariables()

#ejercicios parte 2 segunda clase

#ejercicio 2
#condiciones

class Condicion:
    contador=0

    def __init__(self,num1=0,num2=1):
        self.numero1=num1
        self.numero2=num2
        numero=num1+num2
        self.numero3=numero
        #variables de instancia

    def usoI(self):
        if self.numero1==self.numero2:
            print("numero1:{}, numero2:{}: son iguales".format(self.numero1,self.numero2))
        elif self.numero1==self.numero3:
            print("numero1:{}, numero3:{}: son iguales".format(self.numero1,self.numero2))
        else:
            print("no son iguales")

#usar clase
#cod1=Condicion()
#print(cod1.numero1)
#print(cod1.numero2)

cod2=Condicion(10,20)
cod2.usoif
print(cod2.numero1)

#ejercicio 3 clase 2
#ciclos

class Ciclos:
    def __init__(self,num1=5):
        self.numero=num1
    
    def usoWhile(self):

        car=input("ingrese una vocal: ")
        car=car.lower
        while car not in("a", "e", "i", "o", "u"):
            car=input("Ingrese una vocal: ").lower()
        print("Felicitaciones el caracter:{} es una vocal".format(car))

clo1=Ciclos()
clo1.usoWhile()