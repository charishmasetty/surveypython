from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    street_address = Column(String(100))
    city = Column(String(50))
    state = Column(String(50))
    zip = Column(String(10))
    telephone = Column(String(20))
    email = Column(String(120))
    date_of_survey = Column(Date)
    liked_most = Column(String(100))
    interest_source = Column(String(100))
    recommendation = Column(String(20))  # Yes/No
