from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Estructuras de datos en memoria
cola_pendientes = []
pila_historial = []
siguiente_id = 1


@app.route("/")
def index():
    return render_template(
        "index.html",
        pendientes=cola_pendientes,
        historial=pila_historial,
    )


@app.route("/registrar", methods=["POST"])
def registrar():
    global siguiente_id

    cliente = request.form.get("cliente", "").strip()
    asunto = request.form.get("asunto", "").strip()

    if cliente and asunto:
        solicitud = {
            "id": siguiente_id,
            "cliente": cliente,
            "asunto": asunto,
            "estado": "pendiente",
        }
        cola_pendientes.append(solicitud)
        siguiente_id += 1

    return redirect(url_for("index"))


@app.route("/atender", methods=["POST"])
def atender():
    if cola_pendientes:
        solicitud = cola_pendientes.pop(0)
        solicitud["estado"] = "atendida"
        pila_historial.append(solicitud)
    return redirect(url_for("index"))


@app.route("/deshacer", methods=["POST"])
def deshacer():
    if pila_historial:
        solicitud = pila_historial.pop()
        solicitud["estado"] = "pendiente"
        cola_pendientes.insert(0, solicitud)
    return redirect(url_for("index"))


@app.route("/cancelar/<int:id_solicitud>", methods=["POST"])
def cancelar(id_solicitud):
    for i, solicitud in enumerate(cola_pendientes):
        if solicitud["id"] == id_solicitud:
            cola_pendientes.pop(i)
            break
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
