from ast import main

def division(numerador, denominador):
    try:
        numero=numerador/denominador
        return numero
    except ZeroDivisionError:
        return("Error. No es posible la división de un número entre 0.")

print(division(7,0))

if __name__=="main__":
    main()
