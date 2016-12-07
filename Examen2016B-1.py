##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##PROGRAMACION AVANZADA
##AUTOR:BENAVIDES,CARDENAS,ESPAÑA,OCHOA,SALDAÑA,USHCASINA
##TITULO:EXAMEN DEL PRIMER BIMESTRE
import sys
##Ejercicio1
def creartxt():
    archi=open('100.txt','w')
    archi.close()
    
def grabartxt(a):
    archi=open('100.txt','a')
    archi.write(a)
    archi.close()

def crear2txt():
    archi=open('1024.txt','w')
    archi.close()
    
def grabar2txt(b):
    archi=open('1024.txt','a')
    archi.write(b)
    archi.close()

def conteo():
    inter="BENAVIDES TOAQUIZA BYRON DANILO CARDENAS VACA MICHAEL STEVEN ESPAÑA TEDES BRYAN RAFAEL OCHOA TOLEDO DANNA SALDAÑA MIRANDA JUAN DAVID USHCASINA CHACUA PAOLA FERNANDA"
    union=""
    union2=""
    n=0
    while n != 102400:
        for i in range(len(inter)):
            if n <102400:
                union=union+inter[i]
                n=n+1
    creartxt()
    grabartxt(union)
    n=0

    while n != 1048576:
        for i in range(len(inter)):
            if n <1048576:
                union2=union2+inter[i]
                n=n+1
    crear2txt()
    grabar2txt(union2)
##Fin Ejercicio1

##Ejercicio3
def rectangular ():
    print ('Volume_rectangular')
    altura=int(input("ingrese la altura de la pisina rectangular"))
    largo=int(input("ingrese el largo de la pisina "))
    ancho= int(input("ingrese el ancho de la piscina"))
    volumen=altura*largo*ancho
    print("el volumen es",volumen,"metros cubicos")
    
def eliptica():
    print('Volumen_eliptica')
    pi=(3.14)
    ejem=int(input("ingrese el eje menor"))
    ejemM=int(input("ingrese el eje mayor"))
    h=int (input("ingrese la altura "))
    volumen=pi*ejem*ejemM*h
    print("el volumen del eliptica es",volumen)

def radio():
    print('volumen_radio')
    a=(4/3)
    pi=(3.14)
    r=int(input("ingrese la radio del circulo "))
    volumen=(a*pi)*(r**3)
    print("el volumen de la radio es",volumen)

def repetir():
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        main()  #aqui damos la opcion al usuario de si desea continuar en el programa
    print ("Programa Terminado")
    sys.exit()
    



def main2():
#Opcion
    choice=""
    while(choice!=3):
        print("Bienvenido eliga una opcion  ")
        print("(1)Ver a la piscina de modo  rectangular volumen")
        print("(2)Ver a la piscina de modo eliptica volumen")
        print("(3)Ver a la psiicina de modo circular volumen")
        print("digite cero para salir")
        print("ingrese la opcion")
        choice=int(input(""))
        if choice ==1:
            rectangular()
            repetir()
        elif choice ==2:
            eliptica()
            repetir()
        elif choice ==3:
            radio()
            repetir()
        elif choice==0:
            print("ADIOS")
            exit()
        else:
            print("opcion incorrecta")
            print("vuelva a ingresar")





##Fin Ejercicio3
    
def main():
    print("\t\t\t     Escuela Politécnica Nacional")
    print("\t\t\t  Escuela de Formación de Tecnólogos")
    print("\t\t\t\t  Programación Avanzada")
    print("\t\t\t     EXAMEN PRIMER BIMESTRE")
    op = int(input("Seleccione la opción que desee: "))
    while op != "":
        if op == 1:
            conteo()
        elif op ==2:
            Ej()
        elif op==3:
            main2()
        else:
            exit()
        print("\n")
        print("\n")
        op = int(input("Seleccione la opción que desee: "))

main()
    
