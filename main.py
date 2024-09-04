from fastapi import FastAPI
from database.connection import create_tables

import uvicorn

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)