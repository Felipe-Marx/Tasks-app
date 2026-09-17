from database import engine, Base
import db_models
from fastapi import FastAPI


Base.metadata.create_all(bind=engine)

app = FastAPI()