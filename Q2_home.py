from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome home!</h1>
    </body>
    </html>
    """, 200

 