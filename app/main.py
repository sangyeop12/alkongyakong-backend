from fastapi import FastAPI
from app.routes import users, prescription, prescription_drugs, schedules, medication_logs, external

app = FastAPI(title="알콩약콩 API", version="1.0.0")

app.include_router(users.router)
app.include_router(prescription.router)
app.include_router(prescription_drugs.router)
app.include_router(schedules.router)
app.include_router(medication_logs.router)

app.include_router(external.router)