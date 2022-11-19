from ast import main

def lista_error():
    lista = [4, 7, 30, 23, 5]
    try:
        lista[10]
    except IndexError:
        return("No existe ese valor en la lista.")

print(lista_error())    

if __name__=="__main__":
    main()
