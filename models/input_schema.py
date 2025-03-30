from pydantic import BaseModel

class MSMEInput(BaseModel):
    land_cents: float
    floors: int
    use_case: str
    budget_lakhs: float
    solar_required: bool = True
