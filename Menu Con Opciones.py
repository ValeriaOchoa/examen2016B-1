def menu():
    print("\n********************************************")
    print("\tGRUPO 1")
    print("\t BIENVENIDOS AL MENU")
    print("1.- Programa que crea un archivo\n")
    print("2.- Contiene archivos del ejercicio anterior\n")
    print("3.- Calcular el volumen de una piscina\n")
    print("4.- Salir.....\n")

def crear_archi():
    print("\tCree un archivo de texto")
    
    
def leer_archi():
     print("\Entrada de archivos")
     

def vol_pis():
    print("\tCalculo volumen de una piscina")
   
        
def main():
    opcion=1
    while(opcion!=4):
     menu()
     print("ESCOJA ANA OPCION: ")
     opcion=int(input())
     
     if opcion == 1:
        crear_archi()
        
     elif opcion == 2:
        leer_archi()
        
     elif opcion == 3:
        vol_pis()

     elif opcion==4:
        print ("Has salido de la aplicación")
        exit()
     else:
            print("Opcion incorrecta:....!!!!")
            
main() 
