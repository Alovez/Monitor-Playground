FROM redis:latest

COPY . /workers/
WORKDIR /workers/

RUN pip install celery
RUN celery -A celery_workers/basic_worker worker -B