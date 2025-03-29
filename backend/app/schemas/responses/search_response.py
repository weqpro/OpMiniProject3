from typing import List
from ..aid_request import AidRequest
from pydantic import BaseModel


class AidRequestSearchResponse(BaseModel):
    result: List[AidRequest]

