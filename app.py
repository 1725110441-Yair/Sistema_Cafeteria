import web
from controllers.pedidos import ListaPedidos, RegistrarPedido, PrepararPedido, CancelarPedido
from controllers.estadisticas import Estadisticas

urls = (
    '/', ListaPedidos,
    '/registrar', RegistrarPedido,
    '/preparar', PrepararPedido,
    '/cancelar/(\d+)', CancelarPedido,
    '/estadisticas', Estadisticas
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()