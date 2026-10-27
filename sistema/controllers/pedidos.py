import web

render = web.template.render('views')

fila_prioritaria = []
fila_normal = []
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
    def GET(self):
        siguiente = obtener_siguiente()
        return render.index(fila_prioritaria, fila_normal, siguiente)


class RegistrarPedido:
    def GET(self):
        return render.registrar()

    def POST(self):
        global contador_id
        datos = web.input()

        nuevo = {
            'id': contador_id,
            'cliente': datos.cliente,
            'producto': datos.producto,
            'cantidad': datos.cantidad,
            'tipo': datos.tipo,
            'tiempo': datos.tiempo
        }
        contador_id += 1

        if datos.tipo == 'Prioritario':
            fila_prioritaria.append(nuevo)
        else:
            fila_normal.append(nuevo)

        raise web.seeother('/')


class PrepararPedido:
    def POST(self):
        global pedidos_preparados
        if len(fila_prioritaria) > 0:
            fila_prioritaria.pop(0)
            pedidos_preparados += 1
        elif len(fila_normal) > 0:
            fila_normal.pop(0)
            pedidos_preparados += 1

        raise web.seeother('/')


class CancelarPedido:
    def POST(self, id_pedido):
        global pedidos_cancelados
        id_num = int(id_pedido)

        for p in fila_prioritaria:
            if p['id'] == id_num:
                fila_prioritaria.remove(p)
                pedidos_cancelados += 1
                raise web.seeother('/')

        for p in fila_normal:
            if p['id'] == id_num:
                fila_normal.remove(p)
                pedidos_cancelados += 1
                raise web.seeother('/')

        raise web.seeother('/')