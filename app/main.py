from fastapi import FastAPI

app = FastAPI(title="Authentication Service")


@app.get("/")
def root():
    return {"message": "Authentication Service is running!"}