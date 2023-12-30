from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import jinja2
from leapcell import Leapcell
import os
import markdown
import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()

api = Leapcell(
    os.environ.get("LEAPCELL_API_KEY"),
)

author = os.environ.get("AUTHOR", "Leapcell User")
avatar = os.environ.get("AVATAR", "https://leapcell.io/logo.png")
resource = os.environ.get("TABLE_RESOURCE", "issac/flask-blog")
table_id = os.environ.get("TABLE_ID", "tbl1738878922167070720")

table = api.table(repository=resource, table_id=table_id)


@app.get("/")
def index():
    records = table.select().query()
    params = {
        "author": author,
        "avatar": avatar,
        "posts": records,
        "timestamp_format": lambda timestamp: datetime.datetime.fromtimestamp(
            timestamp
        ).strftime("%B %d, %Y %H:%M:%S"),
    }
 
    template =jinja2.Environment(loader=jinja2.FileSystemLoader("templates")).get_template("index.html")
    return HTMLResponse(template.render(**params))

@app.get("/category/{category}")
def category(category):
    records = table.select().where(table["category"].contain(category)).query()
    params = {
        "author": author,
        "avatar": avatar,
        "posts": records,
        "category": category,
        "timestamp_format": lambda timestamp: datetime.datetime.fromtimestamp(
            timestamp
        ).strftime("%B %d, %Y %H:%M:%S"),
    }
    template = jinja2.Environment(loader=jinja2.FileSystemLoader("templates")).get_template("index.html")
    return HTMLResponse(template.render(**params))


@app.get("/search")
def search(request: Request):
    query = request.query_params.get("query", "")
    records = table.search(query=query)
    params = {
        "author": author,
        "avatar": avatar,
        "posts": records,
        "query": query,
        "timestamp_format": lambda timestamp: datetime.datetime.fromtimestamp(
            timestamp
        ).strftime("%B %d, %Y %H:%M:%S"),
    }
    template = jinja2.Environment(loader=jinja2.FileSystemLoader("templates")).get_template("index.html")
    return HTMLResponse(template.render(**params))


@app.get("/post/{post_id}")
def post(post_id):
    record = table.get_by_id(post_id)
    markdown_html = markdown.markdown(record["content"])
    params = {
        "author": author,
        "avatar": avatar,
        "post": record,
        "markdown_html": markdown_html,
        "timestamp_format": lambda timestamp: datetime.datetime.fromtimestamp(
            timestamp
        ).strftime("%B %d, %Y %H:%M:%S"),
    }

    template = jinja2.Environment(loader=jinja2.FileSystemLoader("templates")).get_template("post.html")
    return HTMLResponse(template.render(**params))