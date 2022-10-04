from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = 'sqlite:///'+os.path.join(BASE_DIR, 'site.db')

Base = declarative_base()
engine = create_engine(connection_string, echo=True)

"""
class user
    id int
    username str
    email str
    datee_created datetime
I have added this one I am dali
"""


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key = True)
    username = Column(String(25), nullable = False, unique = True)
    email = Column(String(80), unique=False, nullable=False)
    date_created = Column(DateTime(), default = datetime.utcnow)

    def __repr__(self):
        return f'<User username = {self.username} email = {self.email}>'


new_user = User(id=1, username='Sam', email='sam@test.com')
print(new_user)
