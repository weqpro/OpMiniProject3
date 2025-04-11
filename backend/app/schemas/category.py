from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str
    request_id: int
