from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)

    nurses = relationship("Nurse", back_populates="doctor")
    patients = relationship("Patient", back_populates="doctor")

    def __repr__(self):
        return f"Doctor(id={self.id}, name='{self.name}', specialization='{self.specialization}')"


class Nurse(Base):
    __tablename__ = "nurses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    doctor = relationship("Doctor", back_populates="nurses")

    def __repr__(self):
        return f"Nurse(id={self.id}, name='{self.name}', doctor_id={self.doctor_id})"


class Ward(Base):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    patients = relationship("Patient", back_populates="ward")

    def __repr__(self):
        return f"Ward(id={self.id}, name='{self.name}')"


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    ward_id = Column(Integer, ForeignKey("wards.id"))

    doctor = relationship("Doctor", back_populates="patients")
    ward = relationship("Ward", back_populates="patients")

    def __repr__(self):
        return f"Patient(id={self.id}, name='{self.name}', doctor_id={self.doctor_id}, ward_id={self.ward_id})"