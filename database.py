from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Doctor, Nurse, Ward, Patient

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Prepopulate Wards
if not session.query(Ward).count():
    session.add_all([
        Ward(name="General"),
        Ward(name="ICU"),
        Ward(name="Surgery"),
        Ward(name="Pediatrics")
    ])
    session.commit()

session.close()
print("Database initialized successfully.")