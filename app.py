import click
from models import Doctor, Nurse, Patient, Ward
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

Session = sessionmaker(bind=engine)


@click.group()
def cli():
    """
    Command line interface for managing a hospital database.
    """
    pass

@cli.command()
@click.argument('name',prompt='Doctor Name')
@click.argument('specialization',prompt='Specialization',type=str)
def add_doctor(name, specialization):
    """
    Add a new doctor to the database.
    """ 
    session = Session()
    doctor = Doctor(name=name, specialization=specialization)
    session.add(doctor)
    session.commit()
    session.close()
    click.echo(f"{Doctor.name}: added successfully!")


@cli.command()
@click.argument('name', prompt='Nurse Name')
def add_nurse(name, doctor_id):
    """
    Add a new nurse to the database.
    """
    session = Session()
    doctor = session.query(Doctor).get(doctor_id)
    if doctor:
        nurse = Nurse(name=name, doctor_id=doctor_id)
        session.add(nurse)
        session.commit()
        session.close()
        click.echo(f"Nurse {name} added successfully!")
    else:
        click.echo(f"Doctor with ID {doctor_id} not found!")
        session.close()
    

@cli.command()
@click.argument('name', prompt='Patient Name')
@click.argument('doctor_id', prompt='Doctor ID')
@click.argument('ward_id', prompt='Ward ID')
def add_patient(name, doctor_id, ward_id):
    """
    Add a new patient to the database.
    """

    session = Session()
    doctor = session.query(Doctor).get(doctor_id)
    if doctor:
        ward = session.query(Ward).get(ward_id)
        if ward:
            patient = Patient(name=name, doctor_id=doctor_id, ward_id=ward_id)
            session.add(patient)
            session.commit()
            session.close()
            click.echo(f"Patient {name} added successfully!")
        else:
            click.echo(f"Ward with ID {ward_id} not found!")
            session.close()
            return
    else:
            click.echo(f"Doctor with ID {doctor_id} not found!")
            session.close()
            return
    
@cli.command()
def list_doctors():
    """
    List all doctors in the database.
    """
    session = Session()
    doctors = session.query(Doctor).all()
    session.close()
    click.echo("Doctors:")
    for doctor in doctors:
        click.echo(doctor)
        click.echo("- Nurses:")
        for nurse in doctor.nurses:
            click.echo(f"  - {nurse.name}")
            click.echo("- Patients:")

            for patient in nurse.patients:
                click.echo(f"      - {patient.name}")
                click.echo(f"      - Doctor: {patient.doctor.name}")
                click.echo(f"      - Ward: {patient.ward.name}")
                click.echo("-")

   





