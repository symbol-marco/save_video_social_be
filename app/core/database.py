
from sqlalchemy import create_engine
from sqlmodel import Session, select

from app.core.config import settings

engine = create_engine(str(settings.sqlalchemy_database_uri))

def init(session: Session) ->None:
    user = session.exec(select(Us))
