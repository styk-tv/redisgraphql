import redis
from redisgraph import Node, Edge, Graph
r = redis.Redis(host='localhost', port=6379)
redis_graph = Graph('bulk', r)
query = "MATCH (t:Tag {name: 'odin'}) RETURN t"
#OK-query = "MATCH (jenn:Tag) RETURN jenn LIMIT 5"
#FAIL-query = "MATCH (a:Tag {name: 'detective'})-[r]-(b) RETURN type(r), a, b"
#FAIL-query="Match (n:Indicator) return properties(n), ID(n)" -->> Unknown function 'properties'
#FAIL-query="MATCH (n) RETURN DISTINCT keys(n), size(keys(n)) ORDER BY size(keys(n)) DESC" -->> Unknown function 'keys'
result = redis_graph.query(query)
result.pretty_print()
