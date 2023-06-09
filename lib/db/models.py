from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    score = Column(Integer())

    def __repr__(self):
        return f'User {self.id}: ' \
            + f'{self.username}, ' \
            + f'{self.score}'

class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    description = Column(String())
    minimum_score = Column(Integer())

    def __repr__(self):
        return f'Achievement {self.id}: ' \
            + f'{self.title}, ' \
            + f'{self.description}, ' \
            + f'{self.minimum_score}'

class UserAchievement(Base):
    __tablename__ = 'user_achievements'

    user_id = Column(Integer(), ForeignKey('users.id'), primary_key=True)
    achievement_id = Column(Integer(), ForeignKey('achievements.id'), primary_key=True)
    user = relationship(User)
    achievement = relationship(Achievement)

    def __repr__(self):
        return f'UserAchievement(user_id={self.user_id}, achievement_id={self.achievement_id})'