inventario = [

["A01","Teclado",5,10],
["A02","Mouse",15,10],
["A03","Monitor",2,6],
["A04","USB",8,10],
["A05","Audifonos",12,10]
]
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual

    else:
        cantidad = 0

    return cantidad


print("===================================")
print("LISTA DE PEDIDOS DE INVENTARIO")
print("===================================")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print("Código:",codigo)
    print("Artículo:",nombre)
    print("Cantidad a pedir:",pedido)
    print("-----------------------------")