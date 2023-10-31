from Transportes import *

def buscar_transporte(modelo):
    for transporte in transportes:
        if transporte.modelo == modelo:
            return transporte.presentar_informacion()

# Solicitar al usuario que ingrese un modelo de transporte
modelo = input("Por favor, ingresa el modelo del transporte que estás buscando: ")

# Buscar el transporte e imprimir la información
print(buscar_transporte(modelo))