from flask import Flask, render_template, request
from methods import *
import os
from random import random
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    table_html = None
    image_name = None  
    medidas = None  # Aquí guardaremos cuartiles, deciles, percentiles

    if request.method == "POST":
        try:
            # Capturar datos del formulario
            valor_min = float(request.form["valor_min"])
            valor_max = float(request.form["valor_max"])
            frecuencias_str = request.form["frecuencias"]

            # Convertir frecuencias en lista de enteros
            frecuencias = [int(f.strip()) for f in frecuencias_str.split(",") if f.strip()]

            # Cálculos
            amplitud = calcular_amplitud(valor_min, valor_max, len(frecuencias))
            Fi = calcular_fi(frecuencias)

            # Generar tabla HTML
            table_html = "<table border='1' style='border-collapse: collapse; width: 60%; text-align:center;'>"
            table_html += "<tr><th>Intervalo</th><th>fi</th><th>Fi</th></tr>"
            for i, f in enumerate(frecuencias):
                table_html += f"<tr><td>{i+1}</td><td>{f}</td><td>{Fi[i]}</td></tr>"
            table_html += "</table>"

            # Medidas de posición
            q1, q2, q3 = cuartiles(frecuencias)
            d = deciles(frecuencias)
            p = percentiles(frecuencias)

            medidas = {
                "Cuartiles": f"Q1 = {q1}, Q2 (Mediana) = {q2}, Q3 = {q3}",
                "Deciles": ", ".join([f"D{i+1}={d[i]}" for i in range(9)]),
                "Percentiles": ", ".join([f"P{i+1}={p[i]}" for i in range(9)]),
            }

            # Resultado principal
            resultado = f"Amplitud: {amplitud:.2f}"

            # (Opcional) Generar gráfico
            plt.figure()
            plt.bar(range(1, len(frecuencias)+1), frecuencias, color="skyblue")
            plt.title("Frecuencia absoluta")
            plt.xlabel("Intervalo")
            plt.ylabel("fi")

            image_name = f"graph_{random():.5f}.png"
            image_path = os.path.join("static", image_name)
            plt.savefig(image_path)
            plt.close()

        except Exception as e:
            error = str(e)

    return render_template("index.html", resultado=resultado, error=error,
                           table=table_html, image_path=image_name, medidas=medidas)

if __name__ == "__main__":
    app.run(debug=True)
