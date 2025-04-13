from re import match
from fastapi import APIRouter, FastAPI , HTTPException
import language_tool_python
from app.schemas.correction import TextInput , CorrectionResponse
from app.services.corrector import correct_text
from app.schemas.text_request import TextRequest


tool = language_tool_python.LanguageTool('fr')

router = APIRouter()

@router.post("/correct", response_model=CorrectionResponse)
def correct_text_endpoint(input_data: TextInput):
    corrections = correct_text(input_data.text)
    return {"corrections": corrections}

@router.post("/correct-text")
def correct_text(request: TextRequest):
    text = request.text
    is_word = request.isWord

    if is_word:
        matches = tool.check(text)
        corrections = {match.context: [match.replacement for match in matches]}
    else:

        matches = tool.check(text)
        corrections = {match.context: [match.replacement for match in matches]}

    if not corrections:
        return {"corrections": {}}

    return {"corrections": corrections}