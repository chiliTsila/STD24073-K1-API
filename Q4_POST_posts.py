from fastapi import FastAPI

app = FastAPI()

posts = []

@app.post("/posts")
def create_posts(post_list):
    for post in post_list:
        posts.append(post)
    return posts

 