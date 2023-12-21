from .disease import *  # noqa


class ExceptionResponseSchema(BaseModel):  # noqa
    error: str
