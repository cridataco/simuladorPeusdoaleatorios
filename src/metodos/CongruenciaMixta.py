class CongruenciaMixta:
    """
        Xn+1 = (a*Xn + c) mod m

        Xn > 0 ----> Semilla
        a > 0 ----> Multiplicador
        c > 0 ----> Constante aditiva (Incremento)
        m > 0 ----> Módulo (m > X0, a, c)

        Ri = Xn+1 / (m - 1)  # Normalización a [0,1]
        Scaled_Value = Min + Ri * (Max - Min)  # Escalamiento en un rango [Min, Max]
    """

    @staticmethod
    def generatePseudoNumbers(a, c, xn, mod, iterations, min_val, max_val):
        result = ""
        for i in range(iterations):
            xn = (a * xn + c) % mod
            ## En este caso el mod - 1 es para que Ri esté en [0,1], si se utiliza mod sería en [0,1).
            ri = xn / (mod - 1)  
            scaled_value = min_val + ri * (max_val - min_val)  # Escalamiento

            result += f"{i} - Xi| {xn} - Ri| {ri:.4f} - Escalado| {scaled_value:.4f}\n"
        return result

if __name__ == "__main__":
    numbers = CongruenciaMixta.generatePseudoNumbers(7, 5, 3, 16, 20, 4, 19)
    print(numbers)

