from pydantic import BaseModel
from typing import Dict, List

class TextInput(BaseModel):
    text: str

class CorrectionResponse(BaseModel):
    corrections: Dict[str, List[str]]
