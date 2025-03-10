
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import config
import models

engine = create_engine(
    config.POSTGRES_URL,
    echo=True,
    future=True,
)

Session = sessionmaker(engine)

# create tables on start-up
models.Base.metadata.create_all(engine)
