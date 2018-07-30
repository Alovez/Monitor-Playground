FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y htop
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/celery_workers
CMD ["celery","-A", "basic_task", "worker", "-B", "-l", "info", "-Q", "adnetwork_filling_gap", "-c", "2", "--autoscale=10,3"]
