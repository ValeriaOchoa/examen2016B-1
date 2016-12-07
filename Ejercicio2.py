### Ejercicio 2
print "BUSCADOR DE NOMBRES"
palabra = raw_input("Nombre a buscar: ")
arch = raw_input("Nombre del archivo donde buscar: ")

repetidas = 0 
f = open(str(arch),'r')
lines = f.readlines()
for line in lines:
    palabras = line.split(' ')
    for p in palabras:
        if p==palabra:
            repetidas = repetidas+1

print "la palabra "+str(palabra)+" se repite "+str(repetidas)+" veces"

def creartxt():
                archi=open('Numero_repetidas.txt','w')
                archi.close

archi=open('Numero_repetidas.txt','a')
archi.write('\nEl nombre se repite :'+str(repetidas)+' veces')
archi.close
            
