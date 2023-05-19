import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///tables.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_new_user():
    name = input("Enter your name: ")

    connection = engine.connect()

    insert_query = User(username=name, score = 0)
    session.add(insert_query)
    session.commit()
    user_id = insert_query.id

    print("New user created successfully!")

    associate_achievements(connection, user_id)

def welcome_returning_user():

    name = input("Enter your name: ")

    connection = engine.connect()

    select_query = session.query(User).filter(User.username == name).first()
    print(select_query.username)
    if select_query is None:
        print("I don't see that username! Please create a new user entry.")
        create_new_user()
    else:
        print(f"Welcome back, {select_query.username}!")
        score = select_query.score
        if score > 0:
            last_score = max(score, key=lambda x: x['score'])
            print(f"Your last score: {last_score['score']}")

        choice = input("Do you want to try beating your last score? (yes/no): ")
        if choice == 'no':
            return
        
    #associate_achievements(connection, user_id)

def associate_achievements(connection, user_id):
    select_achievements_query = db.select([Achievement])
    achievements = connection.execute(select_achievements_query).fetchall()

    for achievement in achievements:
        insert_query = UserAchievement.insert().values(user_id=user_id, achievement_id=achievement['id'])
        connection.execute(insert_query)

