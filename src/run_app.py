from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import uvicorn
import os
from tasks import start_task
from db.db_functions import drop_results_table, list_results, append_words, found_len_words_table

api = FastAPI()



@api.get('/')
def index_page():
    body="<html>" \
        "<body style='padding: 10px;'>" \
        "<h1>Welcome to the GUESS_WORD_GAME API</h1>" \
        "<div>" \
        "Try it: <a href='/start/5'>/start/5</a>" \
        "<div>" "</div>" \
        "Check results you can here: <a href='/results'>/results</a>" \
        "<div>"  \
        "Clear list results: <a href='/clear_results'>/clear_results</a>" \
        "</div>" \
        "</body>" \
        "</html>"
    return HTMLResponse(content=body)

@api.get('/start/{level}')
def start_py(level: int):
    start_task.delay(level)
    #print(start_task.task_id)
    return Response(content='Program working, please check "results"')

@api.get('/append_words')
def appendword():
    # print(os.getcwd())
    append_words()
    return True


@api.get('/results')
def get_results():
    list = list_results()
    if list == False:
        return HTMLResponse('<h1>Results clear!</h1>')
    else:
        return {
            'results': list
            }


@api.get('/clear_results')
def clear_results():
    drop_results_table()
    return HTMLResponse('<h1>Results clear!</h1>')


@api.get('/words')
def check_words():
    return found_len_words_table()

if __name__ == "__main__":
   uvicorn.run(api, host="127.0.0.1", port=8000)