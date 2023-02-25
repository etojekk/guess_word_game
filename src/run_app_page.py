from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from tasks import start_task, drop_table, drop_all_words
from db.db_functions import list_results, append_words, found_len_words_table

api = FastAPI()


@api.get('/')
def index_page():
    body="<html>" \
        "<body style='padding: 10px;'>" \
        "<style>" \
        "h4 {" \
        "color: #ff0000;}" \
        "</style>" \
        "<h1>Welcome to the GUESS_WORD_GAME API</h1>" \
        "<div>" \
        "First you need to append words to table: <a href='/append_words'>'/append_words'</a>" \
        "<div>"  \
        "Now you can try it: <a href='/start/5'>/start/5</a>" \
        "<div>" "</div>" \
        "Check results you can here: <a href='/results'>/results</a>" \
        "<div>"  \
        "If you need check length table:: <a href='/words'>/words</a>" \
        "<div>"  \
        "Clear list results: <a href='/clear_results'>/clear_results</a>" \
        "</div>" \
        "<h4>If you need delete WORDS TABLE: <a href='/deleteallwords'>/deleteallwords</a>" \
        "</body>" \
        "</html>" \

    return HTMLResponse(content=body)


@api.get('/start/{level}')
def start(level: int):
    start_task.delay(level)
    return HTMLResponse(content='Program working, words will be to found\nPlease check "results" a little be later')


@api.get('/append_words')
async def appendword():
    try:
        await append_words()
    except TypeError:
        return HTMLResponse('<h1>Words did add in table, program ready</h1>')
    except:
        return HTMLResponse('<h1>Words already in table, program ready</h1>')

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
    drop_table.delay()
    return HTMLResponse('<h1>Results clear!</h1>')


@api.get('/deleteallwords')
def clear_all_words():
    drop_all_words.delay()
    return HTMLResponse('<h1>Words did delete!</h1>')


@api.get('/words')
def check_words():
    try:
        return {
            'amount words': found_len_words_table()
        }
    except:
        return HTMLResponse('<h1>Words not be found!</h1>')


# if __name__ == "__main__":
#    uvicorn.run(api, host="0.0.0.0", port=8000)