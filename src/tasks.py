from celery import Celery
from fastapi import Response

from py_func import start as start_py
from db.db_functions import drop_results_table, drop_table_Words


app = Celery('tasks', backend='redis://redis:6379/', broker='redis://redis:6379/')


@app.task()
def start_task(level: int):
    start_py(level)


@app.task()
def drop_table():
    drop_results_table()


@app.task()
def drop_all_words():
    drop_table_Words()