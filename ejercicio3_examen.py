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



def main():
#Opcion
    choice=""
#Menu
    print("Bienvenido eliga una opcion  ")
    print("ver a la piscina de modo  rectangular volumen")
    print("ver a la piscina de modo eliptica volumen")
    print("Ver a la psiicina de modo circular volumen")
    choice=int(input(""))

    if choice ==1:
        rectangular()
    if choice ==2:
        eliptica()

main()
  
    
