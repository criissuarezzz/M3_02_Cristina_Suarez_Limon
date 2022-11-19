from ast import main

def paises():
    paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
    try:
        paises["alemania"]
    except KeyError:
        return "No ha sido posible encontrar el elemento."

print(paises())


if __name__=="__main__":
    main()