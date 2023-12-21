import joblib
import numpy as np

from typing import Optional, List

from sqlalchemy import select

from app.disease.models import Prediction
from core.db import session


class DiseaseService:
    def __init__(self):
        ...

    async def get_disease_list(
        self,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[Prediction]:
        query = select(Prediction)

        if prev:
            query = query.where(Prediction.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    async def predict_disease(
        self, age: int, blood_pressure: int, albumin: int,
        pus_cellc_cumps: int, bacteria: int, blood_glucose_rand: int,
        blood_urea: int, serum_creatinine: int, hypertension: int,
        diabetes_mellitus: int, caronory_artery_disease: int, appetite: int,
        pedal_edema: int, anemia: int
    ) -> None:
        features = [age, blood_pressure, albumin, pus_cellc_cumps,
                    bacteria, blood_glucose_rand, blood_urea, serum_creatinine,
                    hypertension, diabetes_mellitus,
                    caronory_artery_disease, appetite, pedal_edema, anemia]
        user_input = np.array(features).reshape(1, -1)
        prediction, proba = self.make_prediction(
            "Logistic_Regression_model.joblib", user_input)
        instance = Prediction(
            age=str(age), blood_pressure=str(blood_pressure), albumin=str(albumin),
            pus_cellc_cumps=str(pus_cellc_cumps), bacteria=str(bacteria),
            blood_glucose_rand=str(blood_glucose_rand), blood_urea=str(blood_urea),
            serum_creatinine=str(serum_creatinine), hypertension=str(hypertension),
            diabetes_mellitus=str(diabetes_mellitus),
            caronory_artery_disease=str(caronory_artery_disease), appetite=str(appetite),
            pedal_edema=str(pedal_edema), anemia=str(anemia),
            has_disease=prediction, certanity=str(proba))
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        return instance

    def make_prediction(self, model_filename, user_input):
        model = joblib.load(model_filename)
        prediction = model.predict(user_input)[0]
        proba = model.predict_proba(user_input).max()
        return prediction, proba
