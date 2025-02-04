from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from logging.config import fileConfig
from alembic import context
from app.core.config import settings
from app.db.models.user import Base  # Import your models here

# Load Alembic config
config = context.config

# Setup logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# Set target metadata
target_metadata = Base.metadata

# Create an async engine
def get_url():
    return settings.DATABASE_URL

async def run_migrations_online():
    connectable = create_async_engine(get_url())

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations():
    if context.is_offline_mode():
        context.configure(url=get_url(), literal_binds=True)
        with context.begin_transaction():
            context.run_migrations()
    else:
        await run_migrations_online()

import asyncio
asyncio.run(run_migrations())
