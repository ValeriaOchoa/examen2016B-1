def menu():
    print("\n********************************************")
    print("\tGRUPO 1")
    print("\t BIENVENIDOS AL MENU")
    print("1.- Serie de Fibonacci\n")
    print("2.- Determinar si un numero es par\n")
    print("3.- Determinar si un numero es divisible para 3\n")
    print("4.- Factorial de un numero\n")
    print("5.- Poetncia de un numero\n")
    print("6.- Salir.....\n")

def Fibo():
    print("\tSERIE FIBONACCI")
    a,b=0,1
    while b<100:
        print(b)
        a,b=b,a+b
    
def Det_Par():
     print("\DETERMINA SI UN NUMERO ES PAR O NO")
     numero=int(input("\tINGRESE UN NUMERO\n"))
     if numero % 2 == 0:
         print("EL NUMERO ES PAR")
     else:
         print("EL NUMERO ES IMPAR")
         
def Divisible():
     print("\tDETERMINA SI UN NUMERO ES DIVISIBLE PARA 3")
     numero=int(input("\tINGRESE UN NUMERO\n"))
     if numero % 3 == 0:
         print("EL  NUMERO INGRESADO ES DIVISIBLE PARA 3")
     else:
         print("EL  NUMERO INGRESADO NO ES DIVISIBLE PARA 3 ")
         
def Facto():
    print("\tFACTORIAL")
    f=int(1)
    n=int(input("ingrese un numero: "))
    while(n!=0):
        f=f*n
        n=n-1
        print(f)

def Poten():
    print("\tPOTENCIA")
    x=int(input("ingrese base: "))
    p=int(input("ingrese exponente"))
    z=(x**p)
    print(z)
        
def main():
    opcion=1
    while(opcion!=6):
     menu()
     print("ESCOJA ANA OPCION: ")
     opcion=int(input())
     
     if opcion == 1:
        Fibo()
        
     elif opcion == 2:
        Det_Par()
        
     elif opcion == 3:
        Divisible()

     elif opcion == 4:
        Facto()

     elif opcion == 5:
      Poten()

     elif opcion==6:
        print ("Has salido de la aplicación")
        exit()
     else:
            print("Opcion incorrecta:....!!!!")
            
main() 
