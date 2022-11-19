from ast import main

def resultado():
    suma="2"+10
    try:
        suma
    except TypeError:
        return"No se puede sumar un string a un int"

print(resultado()) 

if __name__=="__main__":
    main()