import web

render = web.template.render('views')

fila_prioritaria = []
fila_nromal = []
pedidos_preparados = 0
pedidos_cancelados = 0
contador_id = 1

def obtener_siguiente():
    if len(fila_prioritaria) > 0:
        return fila_prioritaria[0]
    elif len(fila_normal) > 0:
        return fila_normal[0]
    return None


class ListaPedidos:
    # 4. Mostrar pedidos pendientes y 3. Consultar siguiente pedido
    def GET(self):
        siguiente = obtener_siguiente()
        return render.index(fila_prioritaria, fila_normal, siguiente)


class RegistrarPedido:
    # 1. Registrar pedido
    def GET(self):
        return render.registrar()

    def POST(self):
        global contador_id
        datos = web.input()

        nuevo_pedido = {
            'id': contador_id,
            'cliente': datos.cliente,
            'producto': datos.producto,
            'cantidad': datos.cantidad,
            'tipo': datos.tipo,
            'tiempo': datos.tiempo
        }
        contador_id += 1

        # Encolar según el tipo (FIFO al final de cada lista)
        if datos.tipo == 'Prioritario':
            fila_prioritaria.append(nuevo_pedido)
        else:
            fila_normal.append(nuevo_pedido)

        raise web.seeother('/')


class PrepararPedido:
    # 2. Preparar el siguiente pedido
    def POST(self):
        global pedidos_preparados
        if len(fila_prioritaria) > 0:
            fila_prioritaria.pop(0)  # Saca el primero (FIFO)
            pedidos_preparados += 1
        elif len(fila_normal) > 0:
            fila_normal.pop(0)
            pedidos_preparados += 1

        raise web.seeother('/')


class CancelarPedido:
    # 6. Cancelar pedido por ID
    def POST(self, id_pedido):
        global pedidos_cancelados
        id_num = int(id_pedido)

        # Buscar y eliminar de prioritarios
        for p in fila_prioritaria:
            if p['id'] == id_num:
                fila_prioritaria.remove(p)
                pedidos_cancelados += 1
                raise web.seeother('/')

        # Buscar y eliminar de normales
        for p in fila_normal:
            if p['id'] == id_num:
                fila_normal.remove(p)
                pedidos_cancelados += 1
                raise web.seeother('/')

        raise web.seeother('/')