#!/usr/bin/env python

import json
from flask import Flask, request
from redis.sentinel import Sentinel
from redisgraph import Node, Edge, Graph

sentinel = Sentinel([('io-madstat-prod-redis-redis-ha.redis', 26379)], socket_timeout=5)
slave = sentinel.slave_for('mymaster', socket_timeout=0.3)
redis_graph = Graph('bulk', slave)
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
    return json.dumps(result.result_set[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
