from paciente import Paciente
pacientes:list[Paciente]=[]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("error: debe ingresar un numero entero.")

def menu():
    print("menu clinica")
    print("1.- agregar paciente")
    print("2.- editar paciente")
    print("3.- eliminar paciente")
    print("4.- mostrar un paciente")
    print("5.- mostar todos los pacientes")
    print("6.- salir")
    op=leer_numero("ingrese una opcion: ")
    return op 

def agregar_paciente()-> None:
    rut=input("ingrese rut del paciente: ")
    nombre=input("ingrese nombre del paciente: ")
    edad=leer_numero("ingrese edad del paciente: ")
    print("seleccione prevision del paciente: ")
    print("1.- fonasa")
    print("2.- isapre")
    print("3.- particular")
    print("4.- otro")
    op=leer_numero("seleccione una previson del paciente: ")
    if op==1:
        prevision="fonasa"
    elif op==2:
        prevision="isapre"
    elif op==3:
        prevision="particular"
    elif op==4:
        prevision="otro"

    paciente=paciente(rut,nombre,edad,prevision)
    paciente.append(paciente)
    print("paciente agregado exitosamente.")
    print(f"total de pacientes: {len(pacientes)}")           


def main():
   while True:
    opcion=menu()
    if opcion==1:
        print("agregar paciente")
    elif opcion==2:
        print("editar paciente")
    elif opcion==3:
        print("eliminar paciente")
    elif opcion==4:
        print("mostrar un paciente")
    elif opcion==5:
        print("mostrar todos los pacientes")
    elif opcion==0:
        print("saliendo del programa...")
        break
    else:
        print("opcion invalida. intente nuevamente")     



if __name__=="__main__":
    main()