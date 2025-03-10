class CuadradosMedios:
    """
        Número_(i+1) = Dígitos centrales de (Número_i)^2
        
            semilla : Número entero inicial.
            n       : Cantidad de iteraciones (números pseudoaleatorios a generar).
    """

    @staticmethod
    def generar_cuadrados_medios(semilla, n):
        result = ""
        for i in range(n):
            cuadrado = semilla * semilla
            medio = (cuadrado // 100) % 10000
            semilla = medio
            result += f"Número aleatorio {i + 1}: {semilla}\n"
        return result

if __name__ == "__main__":
    numbers = CuadradosMedios.generar_cuadrados_medios(2573, 10)
    print(numbers)
