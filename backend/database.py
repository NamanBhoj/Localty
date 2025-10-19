# db logic

from backend.base import Base, db_engine




def create_db():
    from backend import models  
   

    print("Creating")
    Base.metadata.create_all(bind=db_engine)
    print("Creatied")


if __name__ == "__main__":
    
    create_db()