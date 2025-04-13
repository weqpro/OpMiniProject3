from pydantic import BaseModel


class SearchOptionsSchema(BaseModel):
    text: str
    tags: list[str]
