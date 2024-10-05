import os
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get(path="/")
def home() -> HTMLResponse:
    return HTMLResponse(
        content="<h1>Welcome to the Backend of <a href='https://MH0386.github.io'>MH0386.github.io</a></h1>",
        status_code=200,
    )


@app.get(path="/send")
def send_message(text: str):
    response_telegram: requests.Response = requests.post(
        url=f"https://api.telegram.org/bot{os.getenv(key='TOKEN')}/sendMessage",
        data={
            "chat_id": os.getenv(key="CHAT_ID"),
            "text": text,
        },
    )
    return response_telegram.json()

@app.get(path="/get_resume")
def get_resume() -> FileResponse:
    return FileResponse(
        path="docs/resume.pdf",
        media_type="application/pdf",
        filename="mohamed_hisham_abdelzaher_resume.pdf",
        headers={
            "Content-Disposition": "inline; filename=mohamed_hisham_abdelzaher_resume.pdf"
        },
    )