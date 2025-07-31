from fastapi import FastAPI

app = FastAPI()

posts = []

@app.get("/posts")
def get_posts():
    return posts

 