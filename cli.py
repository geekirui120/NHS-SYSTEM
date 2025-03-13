
import click
from models import Doctor, Nurse, Patient, Ward
from database import Session


def display_menu():
    """Displays the interactive menu for user selection."""
    click.echo("\n🏥  National Health Service System 🏥")
    click.echo("1. Add a Doctor")
    click.echo("2. Add a Nurse")
    click.echo("3. Add a Patient")
    click.echo("4. Add a Nurse_patient")
    click.echo("5. List All Doctors")
    click.echo("6. Exit")
    choice = click.prompt("\nEnter your choice", type=int)
    return choice


def add_doctor():
    """Function to add a doctor."""
    session = Session()
    name = click.prompt("Enter doctor's name")
    specialization = click.prompt("Enter specialization")
    doctor = Doctor(name=name, specialization=specialization)
    session.add(doctor)
    session.commit()
    session.close()
    click.echo(f"✅ Doctor {name} added successfully!\n")


def add_nurse():
    """Function to add a nurse."""
    session = Session()
    name = click.prompt("Enter nurse's name")
    doctor_id = click.prompt("Enter assigned doctor's ID", type=int)
    
    doctor = session.query(Doctor).get(doctor_id)
    if doctor:
        nurse = Nurse(name=name, doctor_id=doctor_id)
        session.add(nurse)
        session.commit()
        click.echo(f"✅ Nurse {name} added successfully!\n")
    else:
        click.echo(f"❌ Doctor with ID {doctor_id} not found!\n")
    
    session.close()

def add_nurse_patient():
    """Function to add a nurse-patient relationship."""
    session = Session()
    nurse_id = click.prompt("Enter nurse's ID", type=int)
    patient_id = click.prompt("Enter patient's ID", type=int)

    nurse = session.query(Nurse).get(nurse_id)
    patient = session.query(Patient).get(patient_id)

    if not nurse:
        click.echo(f"❌ Nurse with ID {nurse_id} not found!\n")
    elif not patient:
        click.echo(f"❌ Patient with ID {patient_id} not found!\n")
    else:
        nurse.patients.append(patient)
        session.commit()
        click.echo(f"❌ Nurse-Patient relationship added successfully!\n")

    session.close()    


def add_patient():
    """Function to add a patient."""
    session = Session()
    name = click.prompt("Enter patient's name")
    doctor_id = click.prompt("Enter doctor's ID", type=int)
    ward_id = click.prompt("Enter ward ID", type=int)

    doctor = session.query(Doctor).get(doctor_id)
    ward = session.query(Ward).get(ward_id)

    if not doctor:
        click.echo(f"❌ Doctor with ID {doctor_id} not found!\n")
    elif not ward:
        click.echo(f"❌ Ward with ID {ward_id} not found!\n")
    else:
        patient = Patient(name=name, doctor_id=doctor_id, ward_id=ward_id)
        session.add(patient)
        session.commit()
        click.echo(f"✅ Patient {name} added successfully!\n")

    session.close()


def list_doctors():
    """Function to list all doctors and their assigned nurses and patients."""
    session = Session()
    doctors = session.query(Doctor).all()

    if not doctors:
        click.echo("No doctors found.\n")
    else:
        click.echo("\n👨‍⚕️ Doctors List:")
        for doctor in doctors:
            click.echo(f"- {doctor.name} ({doctor.specialization})")

            if doctor.nurses:
                click.echo("  - 🏥 Nurses:")
                for nurse in doctor.nurses:
                    click.echo(f"    - {nurse.name}")

            if doctor.patients:
                click.echo("  - 🏥 Patients:")
                for patient in doctor.patients:
                    click.echo(f"    - {patient.name} (Ward: {patient.ward.name})")

    session.close()
    click.echo("\n")


@click.command()
def cli():
    """Runs the interactive hospital management system."""
    while True:
        choice = display_menu()

        if choice == 1:
            add_doctor()
        elif choice == 2:
            add_nurse()
        elif choice == 3:
            add_patient()
        elif choice == 4:
            list_doctors()
        elif choice == 5:
            click.echo("👋 Exiting system. Goodbye!\n")
            break
        else:
            click.echo("❌ Invalid choice! Please select a valid option.\n")


if __name__ == "__main__":
    cli()