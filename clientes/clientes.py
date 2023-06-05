import os
import json
# Ingresando


def saludar():
    print("BIENVENIDO A LA LIGA DE LOS MATEROS")


saludar()
# Preguntar
option = int(input("1) Para crearte una cuenta \n2) Si ya tenes cuenta \n-"))
datos = {}
datos["materos"] = []
os.system("cls")

if (option == 1):
    print("Hora de registrarnos\n")
    name = input("Nombre del Matero: ")
    email = input("Correo: ")
    pwd = input("Contraseña: ")

    file = open("./clientes/clientes.json", "a")
    file.write(f"{name}|{pwd}|{email}\n")
    file.close()
    print("Registro Exitoso!")
elif (option == 2):
    print("INICIAR SESION\n")
    name = input("Nombre del Matero: ")
    pwd = input("Contraseña: ")
    os.system("cls")
    file = open("./clientes/clientes.json", "r")
    for line in file.readlines():
        data = line.split("|")
        if (data[0] == name and data[1] == pwd):
            print(f"Bueenas {data[0]}")
            print("Listo para cebar unos matencios")
            file.close()
            break
    else:
        print("Este matero no existe :(")
