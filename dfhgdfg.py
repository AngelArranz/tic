def consultar_subsidio():
    renta = float(input("Ingrese su renta: "))
    demandante_energetico = input("¿Está inscrito como demandante energético? (SI/NO): ")

    if renta < 10000 or (renta < 15000 and demandante_energetico.upper() == "SI"):
        print("Le corresponde subsidio.")
    else:
        print("No le corresponde subsidio.")

    opcion = input("¿Desea realizar otra consulta? (S/N): ")
    if opcion.upper() == "N":
        return False
    elif opcion.upper() == "S":
        return True
    else:
        print("Opción inválida. El programa finalizará.")
        return False
