from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

# 함수로 정의
def get_utc_now():
    return datetime.now(timezone.utc)

class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, nullable=False)
    url = Column(String, nullable=False)
    timestamp = Column(DateTime, default=get_utc_now) 