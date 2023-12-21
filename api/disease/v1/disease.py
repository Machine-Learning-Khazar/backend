from fastapi import APIRouter

from app.disease.schemas import (
    ExceptionResponseSchema,
    PredictDiseaseRequestSchema,
    PredictDiseaseResponseSchema,
)
from app.disease.services import DiseaseService

disease_router = APIRouter()


@disease_router.post(
    "",
    # response_model=PredictDiseaseResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def predict_disease(request: PredictDiseaseRequestSchema):
    prediction = await DiseaseService().predict_disease(**request.dict())
    return {
        "has_disease": not prediction.has_disease,
        "certanity": prediction.certanity
    }
