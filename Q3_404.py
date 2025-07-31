from fastapi import FastAPI

app = FastAPI()

@app.get("/{path:path}")
def not_found(path: str):
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>404 Not Found</title>
    </head>
    <body>
        <h1>404 NOT FOUND</h1>
    </body>
    </html>
    """

 