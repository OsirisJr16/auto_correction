from fastapi import APIRouter, FastAPI
from app.schemas.correction import TextInput , CorrectionResponse
from app.services.corrector import correct_text

router = APIRouter()

@router.post("/correct", response_model=CorrectionResponse)
def correct_text_endpoint(input_data: TextInput):
    corrections = correct_text(input_data.text)
    return {"corrections": corrections}