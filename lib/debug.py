#!/usr/bin/env python3

# lib/sqlalchemy_sandbox.py

#!/usr/bin/env python3

# imports
from sqlalchemy import create_engine

# data models

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
