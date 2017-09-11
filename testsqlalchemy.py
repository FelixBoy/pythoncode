# coding=UTF-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(100), primary_key=True)
    name = Column(String(20))

engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/test")
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='8', name='哈哈1')
session.add(new_user)
session.commit()
session.close()