from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuarios predefinidos para Ejercicio 2
USERS = {
    "juan": "admin",
    "pepe": "user"
}

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad_tarros = int(request.form.get("cantidad_tarros"))

        precio_tarro = 9000
        totalSinDescuento = cantidad_tarros * precio_tarro

        # Aplicar descuentos
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        totalDescuento = round(totalSinDescuento*descuento)

        total = round(totalSinDescuento * (1 - descuento))
        resultado = {
            "nombre": nombre,
            "totalSinDescuento": totalSinDescuento,
            "totalDescuento": totalDescuento,
            "total": total
        }
    return render_template("ejercicio1.html", resultado=resultado)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")

        if usuario in USERS and USERS[usuario] == contrasena:
            if usuario == "juan":
                mensaje = f"Bienvenido Administrador {usuario}"
            else:
                mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Credenciales incorrectas. Inténtalo nuevamente."
    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
