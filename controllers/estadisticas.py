import web
from controllers.pedidos import fila_prioritaria, fila_normal, datos_globales

render = web.template.render('views')

class Estadisticas:
    def GET(self):
        prio = len(fila_prioritaria)
        norm = len(fila_normal)
        pendientes = prio + norm
        preparados = datos_globales['preparados']
        cancelados = datos_globales['cancelados']
        total = pendientes + preparados + cancelados

        return render.stats(total, pendientes, preparados, cancelados, prio, norm)