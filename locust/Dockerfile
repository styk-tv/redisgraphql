FROM python:3.7.2
ADD locust-tasks /locust-tasks
RUN pip install -r /locust-tasks/requirements.txt
EXPOSE 5557 5558 8089
RUN chmod 755 /locust-tasks/run.sh
ENTRYPOINT ["/locust-tasks/run.sh"] 
