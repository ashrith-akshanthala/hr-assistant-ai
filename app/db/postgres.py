from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# engine = create_engine(
#     settings.POSTGRES_URL, pool_size=5, max_overflow=10, pool_timeout=30, pool_recycle=-1
# )  # default params
# engine = create_engine(
#     settings.POSTGRES_URL,
#     pool_recycle=1800,
#     pool_pre_ping=True,
#     pool_size=10,
#     max_overflow=20,
#     pool_timeout=30,
#     pool_use_lifo=True,
# )  # prod example

engine = create_engine(
    settings.POSTGRES_URL,
    pool_pre_ping=True,
    echo=True,  # echo will print logs and should be used only in dev.
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        with session.begin():
            yield session
    finally:
        session.close()
