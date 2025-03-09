from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Doctor, Nurse, Patient, Ward, nurses_patients

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()

# Fetch and display doctors
print("\nDoctors:")
for doctor in session.query(Doctor).all():
    print(f"ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}")

# Fetch and display nurses
print("\nNurses:")
for nurse in session.query(Nurse).all():
    print(f"ID: {nurse.id}, Name: {nurse.name}, Assigned Doctor ID: {nurse.doctor_id}")

# Fetch and display patients
print("\nPatients:")
for patient in session.query(Patient).all():
    print(f"ID: {patient.id}, Name: {patient.name}, Assigned Doctor ID: {patient.doctor_id}, Ward ID: {patient.ward_id}")

# Fetch and display wards
print("\nWards:")
for ward in session.query(Ward).all():
    print(f"ID: {ward.id}, Name: {ward.name}")

# Fetch and display nurse-patient relationships
print("\nNurse-Patient Relationships:")
for nurse in session.query(Nurse).all():
    print(f"Nurse {nurse.name} (ID: {nurse.id}) is assigned to patients:")
    for patient in nurse.patients:
        print(f"  - {patient.name} (ID: {patient.id})")

session.close()
