from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
def get_headers(request: Request):
    headers = dict(request.headers)
    return {'headers': headers}