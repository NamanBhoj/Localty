# db logic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()


DATABASE_URI = os.getenv("DATABASE_URI")

if not DATABASE_URI:
    print("URI Issues")

db_engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base = declarative_base()


def create_db():
   

    print("Creating")
    Base.metadata.create_all(bind=db_engine)
    print("Creatied")


# print(create_db())