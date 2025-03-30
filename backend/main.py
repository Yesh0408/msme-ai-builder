from fastapi import FastAPI
from pydantic import BaseModel
from layout_engine.layout_rules import generate_layout

app = FastAPI()

class MSMEInput(BaseModel):
    land_cents: float
    floors: int
    use_case: str
    budget_lakhs: float
    solar_required: bool = True

@app.post('/generate_layout')
def layout(input: MSMEInput):
    return generate_layout(input.dict())
