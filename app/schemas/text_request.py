from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
    isWord: bool