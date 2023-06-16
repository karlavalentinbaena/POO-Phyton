from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)


    print("-----Herencia alumno-----")
    al1 = Alumno("Jose", 19,"37374488484", "ICO")
    print(al1)
    print(Alumno.descripcion)

    print("-----Constructor defecto-----")
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("---Herencia profesor")
    profe1= Profesor("Jesus", 30 + 16, 8458849494, "Ingenieria en software")
    print(profe1)
    profe1.dormir()

    print("-----Herencia ayudante profe")
    ayudante = AyudanteProfesor("Adrian", 20, "4383838", "ICO", 848483, "ing software", 4)
    print(ayudante)
main()
