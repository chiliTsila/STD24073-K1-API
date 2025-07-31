from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

posts = []

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: str

@app.put("/posts")
def update_posts(post_list: List[Post]):
    for post in post_list:
        existing_post = next((p for p in posts if p['title'] == post.title), None)
        if existing_post:
            existing_post.update(post.dict())
        else:
            posts.append(post.dict())
    return posts

 