import logging

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import database
import models
import schemas

# Custom logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


app = FastAPI(
    title="DB-updater",
)

models.database.Base.metadata.create_all(bind=database.engine)


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health", tags=["health_check"])
async def root():
    return {"message": "app is running"}

@app.get("/dental_patients", tags=["patients"])
async def get_patients(db: Session = Depends(get_db)):
    patients = crud.get_all_patients(db)
    return patients

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
