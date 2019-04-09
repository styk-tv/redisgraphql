#!/bin/bash

TARGET_HOST="http://127.0.0.1:8080"
LOCUST="/Users/piotrek/builds/venv_redis/bin/locust"
LOCUS_OPTS="-f /Users/piotrek/git/distributed-load-testing-using-kubernetes/docker-image/locust-tasks/tasks.py --host=$TARGET_HOST"
LOCUST_MODE=${LOCUST_MODE:-standalone}

if [[ "$LOCUST_MODE" = "master" ]]; then
    LOCUS_OPTS="$LOCUS_OPTS --master"
elif [[ "$LOCUST_MODE" = "worker" ]]; then
    LOCUS_OPTS="$LOCUS_OPTS --slave --master-host=$LOCUST_MASTER"
fi

echo "$LOCUST $LOCUS_OPTS"

$LOCUST $LOCUS_OPTS
