
from fastapi import FastAPI
from fastapi.responses import Response, RedirectResponse
from fastapi import status
from db import engine, Session
from models import URL
import pydantic
import hashlib


app = FastAPI()


@app.get("/")
def root():
    return "URL shortener v.0.0.1"


class CreateShortURLRequest(pydantic.BaseModel):
    url: str

class CreateShortURLResponse(pydantic.BaseModel):
    url: str
    short: str


def calculate_hash(text):
    m = hashlib.md5()
    m.update(text.encode('utf8'))
    return m.hexdigest()


@app.put("/s/", response_model=CreateShortURLResponse, summary="Create short URL")
def create_short_url(item: CreateShortURLRequest):
    with Session() as session:
        item_hash = calculate_hash(item.url)
        url = URL()
        url.long = item.url
        url.short = item_hash
        session.add(url)
        session.commit()
    content = CreateShortURLResponse(
        url=item.url,
        short=item_hash,
    )
    return content


@app.get("/s/{short}", summary="Redirect to URL")
def redirect_to_url(short: str):
    with Session() as session:
        url = session.query(URL).where(URL.short==short).first()
    if url is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="URL not found")
    return RedirectResponse(url=url.long)
