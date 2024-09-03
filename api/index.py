import os

import mailersend
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

mailer = mailersend.NewApiClient()
app = FastAPI()
TOKEN: str = os.getenv(key="TOKEN")
CHAT_ID: str = os.getenv(key="CHAT_ID")


@app.get(path="/")
def home() -> HTMLResponse:
    return HTMLResponse(
        content="<h1>Welcome to the Backend of <a href='https://MH0386.github.io'>MH0386.github.io</a></h1>",
        status_code=200,
    )


@app.get(path="/send")
def send_message(text: str):
    response_telegram: requests.Response = requests.post(
        url=f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text,
        },
    )

    subject = "New request from MH0386.github.io"
    text = "There is a new request from your website."
    html = "There is a new request from your website."

    my_mail = "info@domain.com"
    subscriber_list = ["mohamed.hisham.abdelzaher@gmail.com"]

    mailer.send(my_mail, subscriber_list, subject, html, text)
    return response_telegram.json()
