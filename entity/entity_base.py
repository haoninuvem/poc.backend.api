from sqlalchemy.orm import declarative_base

# Must to be a base references to creata a new entity.
# For mor details look at: https://docs.sqlalchemy.org/en/14/orm/quickstart.html#declare-models
Base = declarative_base()