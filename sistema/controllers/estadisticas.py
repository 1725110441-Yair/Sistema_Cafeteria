import web
from controllers.pedidos import fila_prioritaria, fila_normal, pedidos_preparados, pedidos_cancelados

render = web.template.render('views')

class Estadisticas:
    # 5. Consultar estadísticas
    def GET(self):
        pendientes = len(fila_prioritaria) + len(fila_normal)
        total = pendientes + pedidos_preparados + pedidos_cancelados

        return render.stats(
            total,
            pendientes,
            pedidos_preparados,
            pedidos_cancelados,
            len(fila_prioritaria),
            len(fila_normal)
        )