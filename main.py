from fastapi import FastAPI
from database.connection import create_tables
from routes.users import user_router
from routes.auths import auth_router
from routes.records import record_router
from routes.charts import chart_router
from config import SSL_PASSWORD
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/api/users")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(record_router, prefix="/api/records")
app.include_router(chart_router, prefix="/api/charts")

@app.on_event("startup")
def on_startup():
    create_tables()

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True,
                ssl_keyfile="privatekey.pem",
                ssl_certfile="certificate.pem",
                ssl_keyfile_password= SSL_PASSWORD)  