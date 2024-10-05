import json
import os
from git import Repo
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse

app = FastAPI()
data = "data/info.json"
repo = Repo(path=".")
repo.git.refresh(path=os.getenv(key="GIT_PYTHON_GIT_EXECUTABLE"))


@app.get(path="/")
def home() -> HTMLResponse:
    views_count: int = json.loads(s=open(file=data, mode="r").read())["views"]
    with open(file=data, mode="w") as file:
        file.write(json.dumps(obj={"views": views_count + 1}, indent=4))
    if repo.is_dirty():
        repo.git.add(data)
        repo.git.commit(message="update views count")
        repo.git.pull()
        repo.git.push()
    return HTMLResponse(
        content=open(file="api/home.html", mode="r").read(),
    )


@app.get(path="/send")
def send_message(text: str) -> JSONResponse:
    response_telegram: requests.Response = requests.post(
        url=f"https://api.telegram.org/bot{os.getenv(key='TOKEN')}/sendMessage",
        data={
            "chat_id": os.getenv(key="CHAT_ID"),
            "text": text,
        },
    )
    return JSONResponse(
        content=response_telegram.json(),
    )


@app.get(path="/get_resume")
def get_resume() -> FileResponse:
    return FileResponse(
        path="data/docs/resume.pdf",
        media_type="application/pdf",
        filename="mohamed_hisham_abdelzaher_resume.pdf",
        headers={
            "Content-Disposition": "inline; filename=mohamed_hisham_abdelzaher_resume.pdf"
        },
    )


@app.get(path="/get_nasa_space_apps_challenge")
def get_nasa_space_apps_challenge() -> FileResponse:
    return FileResponse(
        path="data/docs/nasa_space_apps_challenge.pdf",
        media_type="application/pdf",
        filename="nasa_space_apps_challenge.pdf",
        headers={
            "Content-Disposition": "inline; filename=nasa_space_apps_challenge.pdf"
        },
    )


@app.get(path="/get_views_count")
def get_views_count() -> JSONResponse:
    return JSONResponse(
        content=json.loads(s=open(file=data, mode="r").read()),
    )
