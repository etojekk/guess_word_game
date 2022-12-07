from celery import Celery
import os
import logging
from py_func import start as start_py


app = Celery('tasks', backend='redis://redis:6379/', broker='redis://redis:6379/')

@app.task()
def start_task(level: int):
    start_py(level)
