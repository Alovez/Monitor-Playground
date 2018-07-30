# Copyright (c) 2018 App Annie Inc. All rights reserved.

from celery import Celery
from celery.schedules import crontab
from time import sleep
import random
import numpy as np


app = Celery()

@app.task
def sleep_and_add(x, y):
    a = np.random.rand(1000000, 1000000)
    b = np.random.rand(1000000, 1000000)
    c = a * b
    d = a ** b
    e = a.dot(b)

app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    broker_url='redis://redis:6379/0',
    beat_schedule={
        "morning_msg_1": {
            "task": "basic_task.sleep_and_add",
            "schedule": crontab(minute='*'),
            "args": (random.randint(0, 10), random.randint(0, 10))
        }
    }
)