### Ejercicio 2
print ("BUSCADOR DE NOMBRES")
palabra = raw_input("Nombre a buscar: ")
arch = raw_input("Nombre del archivo donde buscar: ")

##f = open(str(arch),'r')
##pa=0
##
##for i in f.readlines():
##        palabras1=i.split(" ")
##        pa=pa+len(palabras1)
##        
##print("\nel total de palabras es: "+str(pa)) 
##f.close()

repetidas = 0 
f = open(str(arch))
lines=f.readlines()
for line in lines:
    palabras = line.split(' ')
    for p in palabras:
        if p==palabra:
            repetidas = repetidas+1

print "la palabra "+str(palabra)+" se repite "+str(repetidas)+" veces"

f.close()

def creartxt():
                archi=open('Numero_repetidas.txt','a')
                archi.close

archi=open('Numero_repetidas.txt','a')
archi.write('\nEl nombre se repite :'+str(repetidas)+' veces')
archi.close
            

