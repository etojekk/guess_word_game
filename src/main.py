import uvicorn

from run_app_page import api
from start_celery import start_celery_worker


def run_server():

    selery_worker_process = start_celery_worker()

    uvicorn.run(api, host="0.0.0.0", port=8000)

    selery_worker_process.terminate()

if __name__ == "__main__":
    run_server()