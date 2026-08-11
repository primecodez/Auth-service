from fastapi import FastAPI

app = FastAPI(title="Authentication Service")


@app.get("/")
def root():
    return {"message": "Authentication Service is running!"}

"""POST   /users          → create_user()
GET    /users/{id}     → get_user_by_id()
GET    /users          → get_users()
PUT    /users/{id}     → update_user()
DELETE /users/{id}     → delete_user()"""