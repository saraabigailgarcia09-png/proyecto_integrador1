from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reportes = []


@app.route("/")
def inicio():
    return render_template("index.html", reportes=reportes)


@app.route("/registrar", methods=["POST"])
def registrar():
    estudiante = request.form.get("estudiante", "").strip()
    categoria = request.form.get("categoria", "").strip()
    descripcion = request.form.get("descripcion", "").strip()

    if estudiante and categoria and descripcion:
        reporte = {
            "id": len(reportes) + 1,
            "estudiante": estudiante,
            "categoria": categoria,
            "problema": descripcion,
            "estado": "Pendiente"
        }

        reportes.append(reporte)

    return redirect(url_for("inicio"))


@app.route("/atender/<int:id>", methods=["POST"])
def atender(id):
    for reporte in reportes:
        if reporte["id"] == id:
            reporte["estado"] = "Atendido"
            break

    return redirect(url_for("inicio"))


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    global reportes

    reportes = [
        reporte for reporte in reportes
        if reporte["id"] != id
    ]

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)