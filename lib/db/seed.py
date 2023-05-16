from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Achievement

if __name__ == '__main__':

    engine = create_engine('sqlite:///lib/db/tables.db')
    Session = sessionmaker(bind=engine)
    session = Session()