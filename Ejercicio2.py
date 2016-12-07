### Ejercicio 2

def leer():
    archi=open('100.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()
    archi.close

leer()

def contar():
    archi=open('100.txt','r')
    archir=open('ResultadoContar.txt','w')
    p=0
    for i in archi.readlines():
        palabras=i.split(" ")
        p=p+len(palabras)
    print("\nel total de palabras es: ",p)
    archir.write("el total de palabras es: "+str(p))
    archi.close()
    archir.close()

contar()

def palab():
    palabra=input("ingrese palabra a  buscar: ")
    archir=open('ResultadoContar.txt','a')
    archi=open('100.txt','r')
    
    repeti=0
    lineas=archi.readlines()
    for line in lineas:
        palabras=line.split(" ")
        for p in palabras:
            if p==palabra:
                repeti=repeti+1
    print("la palabra: ",palabra,"\nse repite: ",repeti)
    print("(",palabra,",",repeti,")")
    archir.write("\n("+str(palabra))
    archir.write(","+str(repeti)+")")
    archi.close
    archir.close
    
    
def denuevo():
    global nuevo
    print("Desea intentar nuevamente(si/no)")
    nuevo=input()
    nuevo=nuevo.lower()
    while(nuevo!="no"):
        palab()
        denuevo()

palab()
denuevo()

    



