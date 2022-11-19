from ast import main

def resultado():
    try:
        suma="2"+10
    except TypeError:
        return"No se puede sumar un string a un int."

print(resultado()) 

if __name__=="__main__":
    main()