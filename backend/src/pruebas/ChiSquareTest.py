import numpy as np
import scipy.stats as stats

def chi_square_test(numbers, bins=10, alpha=0.05):
    """
    Realiza la prueba de Chi-cuadrado para evaluar la uniformidad de una secuencia de números pseudoaleatorios.
    
    :param numbers: Lista de números pseudoaleatorios entre 0 y 1.
    :param bins: Número de intervalos en los que se dividirán los datos.
    :param alpha: Nivel de significancia para la prueba.
    :return: Diccionario con los resultados detallados de la prueba.
    """
    n = len(numbers) 
    
    observed, bin_edges = np.histogram(numbers, bins=bins, range=(0, 1))
    expected = np.full(bins, n / bins)
    
    chi_square_statistic = np.sum((observed - expected) ** 2 / expected)
    degrees_of_freedom = bins - 1
    
    critical_value = stats.chi2.ppf(1 - alpha, degrees_of_freedom)
    p_value = 1 - stats.chi2.cdf(chi_square_statistic, degrees_of_freedom)
    
    reject_null = chi_square_statistic > critical_value
    
    return {
        "chi_square_statistic": chi_square_statistic,
        "critical_value": critical_value,
        "p_value": p_value,
        "reject_null": reject_null,
        "observed_frequencies": observed.tolist(),
        "expected_frequencies": expected.tolist(),
        "degrees_of_freedom": degrees_of_freedom,
        "alpha": alpha
    }

# Ejemplo de uso
if __name__ == "__main__":
    random_numbers = np.random.uniform(0, 1, 1000) 
    result = chi_square_test(random_numbers, bins=10, alpha=0.05)
    print(result)