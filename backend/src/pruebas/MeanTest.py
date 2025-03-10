import numpy as np
from scipy.stats import norm

def prueba_media(numeros, alfa=0.05):
    n = len(numeros)
    media_muestral = np.mean(numeros)
    sigma = 1 / np.sqrt(12)  # Desviación estándar teórica
    Z = (media_muestral - 0.5) / (sigma / np.sqrt(n))
    
    # Valor crítico para un nivel de significancia alfa (prueba bilateral)
    Z_critico = norm.ppf(1 - alfa / 2)

    print(f"Media muestral: {media_muestral}")
    print(f"Estadístico Z: {Z}")
    print(f"Valor crítico (α={alfa}): ±{Z_critico}")

    if abs(Z) > Z_critico:
        print("Rechazamos H0: los números no parecen uniformes.")
    else:
        print("No se rechaza H0: los números pueden ser uniformes.")

if __name__ == "__main__":
    # Ejemplo de uso (se ejecuta solo si el módulo se corre directamente)
    numeros = [0.7087, 0.4272, 0.6408, 0.2718, 0, 0.3786, 0.8155, 0.2427, 0.5049, 0.9612,
               0.7184, 0.5922, 0.4466, 0.9709, 0.8835, 0.3981, 0.1456, 0.8544, 0.9029, 0.7282,
               0.7573, 0.2524, 0.6699, 0.767]
    prueba_media(numeros);