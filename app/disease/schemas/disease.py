from pydantic import BaseModel, Field


class PredictDiseaseRequestSchema(BaseModel):
    age: int = Field(..., description="Age")
    blood_pressure: int = Field(..., description="Blood pressure")
    albumin: int = Field(..., description="Albumin")
    pus_cellc_cumps: int = Field(..., description="Pus cellc cumps")
    bacteria: int = Field(..., description="Bacteria")
    blood_glucose_rand: int = Field(..., description="Blood glucose rand")
    blood_urea: int = Field(..., description="Blood urea")
    serum_creatinine: int = Field(..., description="Serum creatinine")
    hypertension: int = Field(..., description="Hypertension")
    diabetes_mellitus: int = Field(..., description="Diabetes mellitus")
    caronory_artery_disease: int = Field(...,
                                         description="Caronory artery disease")
    appetite: int = Field(..., description="Appetite")
    pedal_edema: int = Field(..., description="Pedal edema")
    anemia: int = Field(..., description="Anemia")


class PredictDiseaseResponseSchema(BaseModel):
    has_disease: bool = Field(..., description="Has disease")
    certanity: float = Field(..., description="Certanity")

    class Config:
        orm_mode = True
