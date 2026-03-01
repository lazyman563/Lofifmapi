from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Track:
    def __init__(self, track_id, title, thumbnail, duration=None):
        self.track_id = track_id
        self.title = title
        self.thumbnail = thumbnail
        self.duration = duration

class DBTrack(Base):
    __tablename__ = "library"
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    thumbnail = Column(String)
    added_at = Column(DateTime, default=datetime.utcnow)
