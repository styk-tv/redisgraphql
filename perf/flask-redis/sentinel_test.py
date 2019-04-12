from redis.sentinel import Sentinel
from redisgraph import Node, Edge, Graph

sentinel = Sentinel([('localhost', 26379)])
#sentinel = Sentinel([('io-madstat-prod-redis-redis-ha.redis', 26379)], socket_timeout=0.1)
print "MASTERS > {0}".format(sentinel.discover_master('mymaster'))
print "SLAVES  > {0}".format(sentinel.discover_slaves('mymaster'))


slave = sentinel.slave_for('mymaster', socket_timeout=0.3)

redis_graph = Graph('bulk', slave)
query = "MATCH (t:Tag {name: 'odin'}) RETURN t"
result = redis_graph.query(query)
result.pretty_print()
