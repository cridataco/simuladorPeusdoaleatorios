import os
import sys

# Agregamos el directorio "src" al path para que Python encuentre nuestros paquetes.
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
sys.path.insert(0, src_path)

from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np

# Importamos los módulos de generación
from metodos.CongruenciaLineal import GeneratorNum
from metodos.CongruenciaMixta import CongruenciaMixta
from metodos.CuadradosMedios import CuadradosMedios

# Importamos los módulos de pruebas
from pruebas.ChiSquareTest import chi_square_test
from pruebas.KolmogorovSmirnofTest import kolmogorov_smirnov_test, format_ks_result
from pruebas.MeanTest import prueba_media
from pruebas.Varianza import calcular_varianza

app = Flask(__name__)
app.secret_key = "clave_secreta"  # Necesario para usar flash messages

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        metodo = request.form.get("metodo")
        
        if metodo == "lineal":
            try:
                a = float(request.form.get("a"))
                xn = float(request.form.get("xn"))
                c = float(request.form.get("c"))
                mod = float(request.form.get("mod"))
                iterations = int(request.form.get("iterations"))
                min_val = float(request.form.get("min_val"))
                max_val = float(request.form.get("max_val"))
            except (ValueError, TypeError):
                flash("Revisa los valores ingresados para Congruencia Lineal.", "danger")
                return redirect(url_for("index"))
            gen = GeneratorNum(a, xn, c, mod, iterations, min_val, max_val)
            result_text = gen.generate_all_numbers()
            # Normalizamos la lista de números generados al intervalo [0,1] para pruebas estadísticas
            normalized = [(num - min_val) / (max_val - min_val) for num in gen.get_generated_numbers()]
            return render_template("resultado.html", metodo="Congruencia Lineal", result_text=result_text, numbers=normalized)
        
        elif metodo == "mixta":
            try:
                a = float(request.form.get("a"))
                c = float(request.form.get("c"))
                xn = float(request.form.get("xn"))
                mod = float(request.form.get("mod"))
                iterations = int(request.form.get("iterations"))
                min_val = float(request.form.get("min_val"))
                max_val = float(request.form.get("max_val"))
            except (ValueError, TypeError):
                flash("Revisa los valores ingresados para Congruencia Mixta.", "danger")
                return redirect(url_for("index"))
            # La función generatePseudoNumbers retorna un string
            result_text = CongruenciaMixta.generatePseudoNumbers(a, c, xn, mod, iterations, min_val, max_val)
            return render_template("resultado.html", metodo="Congruencia Mixta", result_text=result_text, numbers=None)
        
        elif metodo == "cuadrados":
            try:
                semilla = int(request.form.get("semilla"))
                n = int(request.form.get("n"))
            except (ValueError, TypeError):
                flash("Revisa los valores ingresados para Cuadrados Medios.", "danger")
                return redirect(url_for("index"))
            result_text = CuadradosMedios.generar_cuadrados_medios(semilla, n)
            return render_template("resultado.html", metodo="Cuadrados Medios", result_text=result_text, numbers=None)
        
        else:
            flash("Método no reconocido.", "danger")
            return redirect(url_for("index"))
    
    return render_template("index.html")

@app.route("/pruebas", methods=["POST"])
def pruebas():
    numeros_str = request.form.get("numeros")
    try:
        numbers = list(map(float, numeros_str.split(",")))
    except Exception as e:
        flash("Error al procesar la lista de números. Asegúrate de ingresar números separados por coma.", "danger")
        return redirect(url_for("index"))
    
    chi_result = chi_square_test(numbers)
    ks_result = kolmogorov_smirnov_test(numbers)
    ks_text = format_ks_result(ks_result)
    
    # Capturamos la salida de la función de prueba de media redirigiendo la salida estándar
    import io
    salida = io.StringIO()
    sys.stdout = salida
    prueba_media(numbers)
    sys.stdout = sys.__stdout__
    media_result = salida.getvalue()
    
    varianza = calcular_varianza(numbers)
    
    return render_template("pruebas.html", chi_result=chi_result, ks_text=ks_text, media_result=media_result, varianza=varianza)

if __name__ == "__main__":
    app.run(debug=True)
