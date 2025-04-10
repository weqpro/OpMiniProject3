from pydantic import BaseModel


class SearchOptions(BaseModel):
    text: str
    tags: list[str]
