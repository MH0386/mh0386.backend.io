import os

import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()


@app.get(path="/")
def home() -> HTMLResponse:
    return HTMLResponse(
        content=open(file="api/home.html", mode="r").read(),
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


@app.get(path="/get_nasa_space_apps_challenge")
def get_nasa_space_apps_challenge() -> FileResponse:
    return FileResponse(
        path="docs/nasa_space_apps_challenge.pdf",
        media_type="application/pdf",
        filename="nasa_space_apps_challenge.pdf",
        headers={
            "Content-Disposition": "inline; filename=nasa_space_apps_challenge.pdf"
        },
    )
