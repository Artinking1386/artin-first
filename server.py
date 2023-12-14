from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <header>
            <title>Artin Home Page</title>
        </header>
        <body>
            <h1>Hello I am Artin</h1>
        </body>
    </html>
    """


@app.get("/say/{name}")
def read_item(name: str):
    return "hello " + name
