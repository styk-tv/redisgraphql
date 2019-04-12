
from flask import Flask
#, render_template, request
#from meinheld import server

from redis.sentinel import Sentinel
from redisgraph import Node, Edge, Graph

sentinel = Sentinel([('io-madstat-prod-redis-redis-ha.redis', 26379)], socket_timeout=5)
slave = sentinel.slave_for('mymaster', socket_timeout=5)
redis_graph = Graph('bulk', slave)

SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
#app.config.from_object(__name__)


@app.route('/')
def root(status, response_headers):
    return 'RedisGraphQL Mainheld Testing Service\n'



@app.route('/redis',  methods=['GET'])
def redis(environ, start_response):
    query = "MATCH (t:Tag {name: 'odin'}) RETURN t"
    result = redis_graph.query(query)

    status = '200 OK'
    res = str(result.result_set[1][0],'utf-8')
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(res)))]
    start_response(status, response_headers)
    return [bytes(res, 'utf-8')]


#meinheld.listen(("0.0.0.0", 8080))
#meinheld.run(app)
