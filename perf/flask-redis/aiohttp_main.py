from aiohttp import web
from redis.sentinel import Sentinel
from redisgraph import Node, Edge, Graph

async def root(request):
    text = "Hello from aiohttp"
    return web.Response(text=text)

async def redis(request):
    query = "MATCH (t:Tag {name: 'odin'}) RETURN t"
    result = redis_graph.query(query)
    return web.Response(text=str(len(result.result_set[1][0])))



sentinel = Sentinel([('io-madstat-prod-redis-redis-ha.redis', 26379)], socket_timeout=5)
slave = sentinel.slave_for('mymaster', socket_timeout=0.3)
redis_graph = Graph('bulk', slave)

app = web.Application()
app.add_routes([web.get('/', root),
                web.get('/{name}', redis)])

web.run_app(app)
