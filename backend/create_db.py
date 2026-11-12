from sqlalchemy import create_engine
from app.models import Base

engine = create_engine("sqlite:///dev.db", echo=True)
Base.metadata.create_all(engine)