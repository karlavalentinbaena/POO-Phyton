from cosas import Alumno, Perro
def main():
    # __ significa que es privado
    al1 = Alumno("Jose", 19, "ICO")
    print(vars((al1))) #vars muestra variables internas de la clase
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("---------To string--------")
    print(al1)
    al1.set_edad(20)
    print(al1)
    al1.estudiar(3)
    print(al1)

    print("---------- Perro ----------")
    perro1 = Perro("Poodle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #set en notacion pythonic
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)
main()
