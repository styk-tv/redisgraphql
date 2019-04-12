
from flask import Flask, render_template, request
from meinheld import server, middleware
from redis.sentinel import Sentinel
from redisgraph import Node, Edge, Graph

sentinel = Sentinel([('io-madstat-prod-redis-redis-ha.redis', 26379)], socket_timeout=5)
slave = sentinel.slave_for('mymaster', socket_timeout=5)
redis_graph = Graph('bulk', slave)

SECRET_KEY = 'development key'
DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)



@app.route('/')
def root():
    return 'RedisGraphQL Mainheld Testing Service\n'



@app.route('/redis',  methods=['GET', 'POST'])
def redis():
    query = "MATCH (t:Tag {name: 'odin'}) RETURN t"
    result = redis_graph.query(query)

    status = b'200 OK'
    res = result.result_set
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(res)))]
    start_response(status, response_headers)
    return [res]





server.listen(("0.0.0.0", 8080))
server.run(app)