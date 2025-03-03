# FastAPI Example Project Deployment Guide on Leapcell

## Introduction

This is an example project built with FastAPI. The primary goal of this project is to teach users how to deploy a FastAPI application on the Leapcell platform. Whenever you make changes to the content in the `content` directory and perform a `git merge` into the `main` branch, an automatic deployment will be triggered on Leapcell.

## Project Structure

```
.
├── content               # Directory to store Markdown files representing blog posts
│   ├── first-review.md   # A sample blog post in Markdown format
│   └── second.md         # Another sample blog post in Markdown format
├── images                # Directory for storing static image resources
│   └── logo.png          # Example logo image file
├── main.py               # The main entry point file of the FastAPI application
├── requirements.txt      # Lists all the Python dependencies required for the project
└── templates             # Directory containing Jinja2 HTML templates for rendering web pages
    ├── base.html         # Base HTML template that other templates can inherit from
    ├── index.html        # HTML template for the home page
    └── single_post.html  # HTML template for displaying a single blog post
```

## Prerequisites

- A GitHub (or other Git - based) repository for your project.
- A Leapcell account. You can sign up at [Leapcell's official website](https://leapcell.io).
- Basic knowledge of Git commands and Python programming.

## Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/leapcell/fastapi-blog
   cd fastapi-blog
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application Locally**
   ```bash
   uvicorn main:app --reload
   ```
   Then, open your browser and visit `http://127.0.0.1:8000` to see the application running.

## Deployment on Leapcell

1. **Connect Your Repository to Leapcell**
   - Log in to your Leapcell account.
   - Navigate to the project creation page and select the option to connect your Git repository (e.g., GitHub).
   - Authorize Leapcell to access your repository and choose the `main` branch.
2. **Configure the Deployment**
   - **Build Command**: In Leapcell, set the build command to `pip install -r requirements.txt`. This will install all the necessary Python packages.
   - **Start Command**: Set the start command to `uvicorn main:app --host 0.0.0.0 --port 8000`.
   - **Port**: 8000
3. **Initial Deployment**
   - After configuration, Leapcell will automatically start the first deployment. You can monitor the deployment progress on the Leapcell dashboard.

## Try Making Changes and Merging to the Main Branch

1. **Modify a Blog Post**
   - Open one of the Markdown files in the `content` directory, such as `first - review.md`.
   - Make some changes to the content, for example, add a new paragraph or correct a typo.
2. **Stage and Commit Your Changes**
   ```bash
   git add content/first - review.md
   git commit -m "Update the content of first - review.md"
   ```
3. **Create a New Branch (Optional but Recommended)**
   ```bash
   git checkout -b new - content - branch
   ```
4. **Merge Your Changes to the Main Branch**
   - First, switch back to the `main` branch:
     ```bash
     git checkout main
     ```
   - Then, pull the latest changes from the remote `main` branch:
     ```bash
     git pull origin main
     ```
   - Finally, merge your changes from the new branch (if you created one):
     ```bash
     git merge new - content - branch
     ```
   - Push the updated `main` branch to the remote repository:
     ```bash
     git push origin main
     ```
5. **Watch the Automatic Deployment**
   - Once you push the changes to the `main` branch, Leapcell will detect the changes and start an automatic deployment.
   - Check the Leapcell dashboard to see the deployment progress. After the deployment is successful, you can visit your application's URL on Leapcell to see the updated content.

## Troubleshooting

- If the deployment fails, check the deployment logs on Leapcell. They usually provide detailed error messages.
- Ensure that all the dependencies in the `requirements.txt` file are correctly specified and compatible with each other.

## Conclusion

By following this guide, you should be able to deploy your FastAPI application on Leapcell and experience the automatic deployment feature when you update your content. Try making more changes to your blog posts and enjoy the seamless deployment process!
