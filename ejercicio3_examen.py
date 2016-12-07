import sys
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
    
def main():
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
main()
