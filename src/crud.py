from dateutil.relativedelta import *
from sqlalchemy.orm import Session

import models
import schemas


def get_all_patients(db: Session):
    all_patients = db.query(models.dental_patients).all()
    return all_patients


def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.dental_patients(
        fname=patient.fname,
        lname=patient.lname,
        email=patient.email,
        dob=patient.dob,
        address=patient.address,
        state=patient.state,
        gender=patient.gender,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
