from sqlalchemy import Column, Unicode, BigInteger, Boolean

from core.db import Base
from core.db.mixins import TimestampMixin


class Prediction(Base, TimestampMixin):
    __tablename__ = "predictions"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    age = Column(Unicode(255), nullable=False)
    blood_pressure = Column(Unicode(255), nullable=False)
    albumin = Column(Unicode(255), nullable=False)
    pus_cellc_cumps = Column(Unicode(255), nullable=False)
    bacteria = Column(Unicode(255), nullable=False)
    blood_glucose_rand = Column(Unicode(255), nullable=False)
    blood_urea = Column(Unicode(255), nullable=False)
    serum_creatinine = Column(Unicode(255), nullable=False)
    hypertension = Column(Unicode(255), nullable=False)
    diabetes_mellitus = Column(Unicode(255), nullable=False)
    caronory_artery_disease = Column(Unicode(255), nullable=False)
    appetite = Column(Unicode(255), nullable=False)
    pedal_edema = Column(Unicode(255), nullable=False)
    anemia = Column(Unicode(255), nullable=False)
    has_disease = Column(Boolean, default=True)
    certanity = Column(Unicode(255), nullable=True)
