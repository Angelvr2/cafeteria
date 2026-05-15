from flask import Flask, render_template, request
from listas.inventario import inventario
from entidades.pedido import Pedido
from entidades.ticket import Ticket

app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template("index.html", productos = inventario)


@app.route("/ticket", methods=["POST"])
def generar_ticket():

    nombre_producto = request.form["producto"]
    cantidad = int(request.form["cantidad"])

    producto_seleccionado = None


    for producto in inventario:

        if producto.nombre == nombre_producto:
            producto_seleccionado = producto
    
    if producto_seleccionado is None:
        return "Nombre invalido"


    pedido = Pedido(producto_seleccionado, cantidad)

    ticket = Ticket(pedido)

    return render_template(
        "ticket.html",
        pedido=pedido,
        subtotal=pedido.calcular_subtotal(),
        impuesto=ticket.calcular_impuesto(),
        descuento=ticket.calcular_descuento(),
        total=ticket.calcular_total()
    )


if __name__ == "__main__":
    app.run(debug=True)