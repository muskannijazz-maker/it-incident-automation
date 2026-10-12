from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from automation import recommend_action
from database import (
    save_incident,
    get_incidents,
    get_incident_by_id,
    update_incident_status
)

app = FastAPI()


class Incident(BaseModel):
    service: str
    description: str
    severity: Literal["low", "medium", "high"]
    status: str = "open"


def calculate_priority(severity):
    if severity == "high":
        return "P1"
    elif severity == "medium":
        return "P2"
    else:
        return "P3"


@app.get("/")
def home():
    return {"message": "IT Incident Automation API is running"}


@app.post("/incidents")
def create_incident(incident: Incident):
    priority = calculate_priority(incident.severity)
    recommended_action = recommend_action(priority)

    incident_id = save_incident(
        incident.service,
        incident.description,
        incident.severity,
        incident.status,
        priority
    )

    return {
        "id": incident_id,
        "service": incident.service,
        "description": incident.description,
        "severity": incident.severity,
        "status": incident.status,
        "priority": priority,
        "recommended_action": recommended_action
    }


@app.get("/incidents")
def read_incidents():
    return get_incidents()


@app.get("/incidents/{incident_id}")
def read_incident(incident_id: int):
    incident = get_incident_by_id(incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident


@app.patch("/incidents/{incident_id}/status")
def change_incident_status(
    incident_id: int,
    status: Literal["open", "in_progress", "resolved"]
):
    updated = update_incident_status(incident_id, status)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return {
        "id": incident_id,
        "status": status,
        "message": "Incident status updated"
    }