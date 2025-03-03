import os
import markdown
from datetime import datetime
import frontmatter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
# Initialize Jinja2 templates with 'templates' directory
templates = Jinja2Templates(directory="templates")
# Serve static files from 'images' directory at '/images' endpoint
app.mount("/images", StaticFiles(directory="images"), name="images")


# Retrieve blog posts from Markdown files
def get_blog_posts():
    content_dir = "content"
    posts = []
    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(content_dir, filename)
            # Get file creation timestamp and convert to datetime object
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_time)

            with open(file_path, "r", encoding="utf-8") as file:
                post = frontmatter.load(file)
                # Convert Markdown content to HTML
                html_content = markdown.markdown(post.content)

                post_data = {
                    "title": post.get("title", filename.replace(".md", "")),
                    "content": html_content,
                    # Generate summary from first line or truncate content
                    "summary": post.get("summary", post.content.split("\n")[0][:150]),
                    "date": post.get("date", creation_date),
                    "tags": post.get("tags", []),
                    # Create URL-friendly slug from filename
                    "slug": filename.replace(".md", "").replace(" ", "-").lower(),
                }

                # Convert date string to datetime object if needed
                if isinstance(post_data["date"], str):
                    post_data["date"] = datetime.strptime(post_data["date"], "%Y-%m-%d")

                posts.append(post_data)

    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts


# Home route rendering blog list
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    posts = get_blog_posts()
    return templates.TemplateResponse(
        "index.html", {"request": request, "posts": posts}
    )


# Single post route by slug
@app.get("/blog/{post_title}", response_class=HTMLResponse)
async def single_post(request: Request, post_title: str):
    posts = get_blog_posts()
    # Find post by matching slug
    post = next((p for p in posts if p["slug"] == post_title), None)
    return (
        templates.TemplateResponse(
            "single_post.html", {"request": request, "post": post}
        )
        if post
        else HTMLResponse("Post not found", status_code=404)
    )
