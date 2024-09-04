from sqlmodel import create_engine, Session, SQLModel
from config import DATABASE_URL
from models.users import User
from models.musics import Music
from models.charts import Chart
from models.records import Record

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session