"""volunteer request schema"""
from pydantic import BaseModel


class VolunteerRequest(BaseModel):

    id: int
    volunteer_id: int
    aid_request_id: int

    volunteer: Volunteer
    aid_request: AidRequest
