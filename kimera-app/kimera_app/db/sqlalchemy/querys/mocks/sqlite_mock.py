from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import kimera_db.components.tools.mock as sqlalchemy_mock

mock_engine = sqlalchemy_mock.mock_engine()
mock_engine1 = sqlalchemy_mock.mock_engine()
mock_engine2 = sqlalchemy_mock.mock_engine()

Base = declarative_base()
Base1 = declarative_base()
Base2 = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    #         self.name, self.fullname, self.nickname)


class User1(Base1):
    __tablename__ = 'users1'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    #         self.name, self.fullname, self.nickname)


class User2(Base2):
    __tablename__ = 'users2'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    #         self.name, self.fullname, self.nickname)


Base.metadata.create_all(mock_engine)
Base1.metadata.create_all(mock_engine1)
Base2.metadata.create_all(mock_engine2)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
ed_user1 = User1(name='ed', fullname='Ed Jones1', nickname='edsnickname1')
ed_user2 = User2(name='ed', fullname='Ed Jones2', nickname='edsnickname2')

session = Session(binds={Base: mock_engine,
                         Base1: mock_engine1,
                         Base2: mock_engine2})

session.add(ed_user)
session.add(ed_user1)
session.add(ed_user2)

bind = session.get_bind(ed_user)
bind1 = session.get_bind(ed_user1)
bind2 = session.get_bind(ed_user2)

# session.commit()
# session.bind = session.get_bind(User)
result = session.query(User).all()

print(result)
