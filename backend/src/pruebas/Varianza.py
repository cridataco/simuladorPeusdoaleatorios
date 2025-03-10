def calcular_varianza(datos):
    n = len(datos)
    if n == 0:
        return None  # Evitar división por cero
    media = sum(datos) / n
    varianza = sum((x - media) ** 2 for x in datos) / n  # Varianza poblacional
    return varianza

if __name__ == "__main__":
    # Bloque interactivo para ejecutar desde consola (no se ejecuta al importar)
    try:
        entrada = input("Ingrese los números separados por espacio: ")
        datos = list(map(float, entrada.split()))
        
        if len(datos) < 2:
            print("Debe ingresar al menos dos números para calcular la varianza.")
        else:
            resultado = calcular_varianza(datos)
            print(f"La varianza es: {resultado:.5f}")
    except ValueError:
        print("Error: Ingrese solo números válidos.")
