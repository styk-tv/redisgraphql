FROM python:3.7.2
ADD locust-tasks /locust-tasks
ADD flask-redis /flask-redis
RUN pip install -r /locust-tasks/requirements.txt
RUN pip install -r /flask-redis/requirements.txt
EXPOSE 5557 5558 8089 8080
RUN chmod 755 /locust-tasks/run.sh
RUN chmod 755 /flask-redis/run.sh
ENTRYPOINT ["/locust-tasks/run.sh"] 
