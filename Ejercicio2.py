### Ejercicio 2
from time import time

print ("BUSCADOR DE NOMBRES")
palabra = str(input("Nombre a buscar: "))
arch = str(input("Nombre del archivo donde buscar: "))

f = open(arch,'r')
p=0
for i in f.readlines():
        palabras1=i.split(" ")
        p=p+len(palabras1)
        
print("\nel total de palabras es: "+str(p))
   

repetidas = 0 
lines = f.readlines()
for line in lines:
    palabras = line.split(' ')
    for pa in palabras:
        if pa==palabra:
            repetidas = repetidas+1

print ("la palabra "+str(palabra)+" se repite "+str(repetidas)+" veces")

def creartxt():
                archi=open('Numero_repetidas.txt','a')
                archi.close

archi=open('Numero_repetidas.txt','a')
archi.write('\nEl nombre se repite :'+str(repetidas)+' veces')
archi.close
            

#funcion
def duracion (n):
    inicio = time()
    j=0
    for i in range (n):
        j= j+i
    fin = time()

    return fin -inicio

def main():
    print("i\t Tiempo de duracion de la busqueda de palabras")
    for i in range (10):
        n=i*1000
        print(n,"\t",duracion(n))
main()
