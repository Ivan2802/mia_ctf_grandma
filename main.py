from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
def get_headers(request: Request):
    headers = dict(request.headers)
    print(headers)
    return {'headers': headers}