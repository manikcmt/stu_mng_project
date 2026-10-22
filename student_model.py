from database import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__= "students"

    id = Column(Integer, primary_key= True)
    roll = Column(String(50), nullable= False, unique= True)
    first_name = Column(String(50), nullable= False)
    last_name = Column(String(50))
    session = Column(Integer)
    department = Column(String(50))
