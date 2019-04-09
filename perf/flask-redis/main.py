#!/usr/bin/env python

from flask import Flask, request
import redis
from redisgraph import Node, Edge, Graph
import json

r = redis.Redis(host='io-madstat-prod-redis-redis-ha.redis', port=6379)
redis_graph = Graph('bulk', r)
app = Flask(__name__)


@app.route('/')
def root():
    return 'RedisGraphQL Flask Testing Service\n'

@app.route('/login',  methods=['GET', 'POST'])
def login():
    deviceid = request.values.get('deviceid')
    return '/login - device: {}\n'.format(deviceid)

@app.route('/metrics',  methods=['GET', 'POST'])
def metrics():
    deviceid = request.values.get('deviceid')
    timestamp = request.values.get('timestamp')
    
    return '/metrics - device: {}, timestamp: {}\n'.format(deviceid, timestamp)

@app.route('/redis',  methods=['GET', 'POST'])
def redis():
    query = "MATCH (t:Tag {name: 'odin'}) RETURN t"
    result = redis_graph.query(query)
    return json.dumps(result.result_set[0])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
