def rectangular ():
    print ('Volume_rectangular')
    altura=int(input("ingrese la altura de la pisina rectangular"))
    largo=int(input("ingrese el largo de la pisina "))
    ancho= int(input("ingrese el ancho de la piscina"))
    volumen=altura*largo*ancho
    print("el volumen es",volumen,"metros cubicos")
    
    



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

main()
  
    
