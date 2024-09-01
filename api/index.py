from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get(path="/")
def home() -> HTMLResponse:
    return HTMLResponse(content="<h1>Welcome to the API</h1>", status_code=200,)
