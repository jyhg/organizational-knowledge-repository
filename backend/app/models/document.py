from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True)
    title = Column(String(255), nullable=False)
    category = Column(String(50), nullable=False)
    content = Column(Text)
    status = Column(Enum("pending", "indexed", "failed", name="doc_status"), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
