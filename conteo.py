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
    
	
	
conteo()
