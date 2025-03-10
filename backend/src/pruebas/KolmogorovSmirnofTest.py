import numpy as np

def kolmogorov_smirnov_test(numbers, alpha=0.05):
    
    # Ordenar los números
    sorted_numbers = np.sort(numbers)
    n = len(sorted_numbers)
    
    # Calcular la función de distribución acumulativa empírica (ECDF)
    ecdf = np.arange(1, n + 1) / n
    
    # Calcular la función de distribución acumulativa teórica (CDF) para una distribución uniforme
    # Para una distribución uniforme en [0,1], la CDF es simplemente F(x) = x
    theoretical_cdf = sorted_numbers
    
    # Calcular las diferencias absolutas
    differences_plus = np.abs(ecdf - theoretical_cdf)  # D+ = máx|F(x) - Fn(x)|
    differences_minus = np.abs(theoretical_cdf - (ecdf - 1/n))  # D- = máx|Fn(x-) - F(x)|
    
    # Estadístico D de Kolmogorov-Smirnov (el máximo de las diferencias)
    d_plus = np.max(differences_plus)
    d_minus = np.max(differences_minus)
    ks_statistic = max(d_plus, d_minus)
    
    # Calcular el valor crítico para el nivel de significancia dado
    # Estos son los valores críticos aproximados para la prueba KS
    # Para un nivel de significancia de 0.05, el valor crítico es aproximadamente 1.36/sqrt(n)
    # Para otros niveles de significancia, se pueden usar diferentes constantes
    if alpha == 0.01:
        critical_value = 1.63 / np.sqrt(n)
    elif alpha == 0.05:
        critical_value = 1.36 / np.sqrt(n)
    elif alpha == 0.10:
        critical_value = 1.22 / np.sqrt(n)
    else:
        # Para otros valores de alpha, usar la aproximación asintótica
        critical_value = np.sqrt(-0.5 * np.log(alpha / 2)) / np.sqrt(n)
    
    # Determinar si se rechaza la hipótesis nula
    reject_null = ks_statistic > critical_value
    
    # Aproximación del p-valor usando la fórmula de Kolmogorov
    # Esta es una aproximación para n grande
    p_value = np.exp(-2 * n * ks_statistic**2)
    
    return {
        "ks_statistic": ks_statistic,
        "critical_value": critical_value,
        "p_value": p_value,
        "reject_null": reject_null,
        "n": n,
        "alpha": alpha,
        "d_plus": d_plus,
        "d_minus": d_minus
    }

def format_ks_result(result):
    
    output = "Resultados de la Prueba Kolmogorov-Smirnov\n"
    output += "=========================================\n"
    output += f"Tamaño de la muestra (n): {result['n']}\n"
    output += f"Nivel de significancia (α): {result['alpha']}\n"
    output += f"Estadístico D de KS: {result['ks_statistic']:.6f}\n"
    output += f"D+: {result['d_plus']:.6f}\n"
    output += f"D-: {result['d_minus']:.6f}\n"
    output += f"Valor crítico para α = {result['alpha']}: {result['critical_value']:.6f}\n"
    output += f"p-valor aproximado: {result['p_value']:.6f}\n"
    output += "\nConclusión: "
    
    if result['reject_null']:
        output += "SE RECHAZA la hipótesis nula.\n"
        output += "Los números no siguen una distribución uniforme."
    else:
        output += "NO SE RECHAZA la hipótesis nula.\n"
        output += "No hay evidencia suficiente para concluir que los números no siguen una distribución uniforme."
    
    return output

# Ejemplo de uso
if __name__ == "__main__":
    # Generar algunos números aleatorios para probar
    np.random.seed(42)  # Para reproducibilidad
    random_numbers = np.random.uniform(0, 1, 1000)
    
    # Realizar la prueba KS
    result = kolmogorov_smirnov_test(random_numbers)
    
    # Mostrar los resultados
    print(format_ks_result(result))
    
    # También podemos probar con números que no siguen una distribución uniforme
    print("\nPrueba con números NO uniformes:")
    non_uniform = np.random.beta(2, 5, 1000)  # Distribución Beta, no uniforme
    result_non_uniform = kolmogorov_smirnov_test(non_uniform)
    print(format_ks_result(result_non_uniform))
