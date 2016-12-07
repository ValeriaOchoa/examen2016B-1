##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##PROGRAMACION AVANZADA
##AUTOR:BENAVIDES,CARDENAS,ESPAÑA,OCHOA,SALDAÑA,USHCASINA
##TITULO:EXAMEN DEL PRIMER BIMESTRE
def main():
    print("\t\t\t     Escuela Politécnica Nacional")
    print("\t\t\t  Escuela de Formación de Tecnólogos")
    print("\t\t\t\t  Programación Avanzada")
    print("\t\t\t     EXAMEN PRIMER BIMESTRE")
    op = int(input("Seleccione la opción que desee: "))
    wile op != "":
        if op == 1:
            Ejercicio1()
        elif op ==2:
            Ejercicio2()
        elif op==3:
            Ejercicio3()
        else:
            exit()
        print("\n")
        print("\n")
        op = int(input("Seleccione la opción que desee: "))

main()
    

