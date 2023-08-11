from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Synchronous engine and session for Celery tasks
sync_engine = create_engine(
    settings.DATABASE_URI,
    pool_pre_ping=True,
    echo=True if settings.LOGGING_LEVEL == "DEBUG" else False,
)

sync_session = sessionmaker(
    bind=sync_engine,
    autoflush=False,
    expire_on_commit=False,
)
