import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()
TOKEN: str | None = os.getenv(key="TOKEN")
CHAT_ID: str | None = os.getenv(key="CHAT_ID")

@app.get(path="/")
def home() -> HTMLResponse:
    return HTMLResponse(
        content="<h1>Welcome to the Backend of <a href='https://MH0386.github.io'>MH0386.github.io</a></h1>",
        status_code=200,
    )

@app.get(path="/send")
def send_message(text: str):
    response: requests.Response = requests.post(
        url=f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text,
        },
    )
    return response.json()
