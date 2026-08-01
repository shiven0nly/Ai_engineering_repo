# Functions
# -> /chat
# -> Receive request
# -> Return streaming resposne

import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from app.models.chat import ChatRequest
from app.services.jd_parser import extract_text_from_file, parse_jd_to_json
from app.services.llm_service import generate_jd_match, generate_response

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return StreamingResponse(
        generate_response(req.message),
        media_type="text/event-stream",
    )

@router.post("/chat/match-jd")
async def match_jd_file(file: UploadFile = File(...)):
    if not file.filename or not (
        file.filename.endswith(".pdf")
        or file.filename.endswith((".docx", ".doc"))
    ):
        raise HTTPException(status_code=400, detail="Only .pdf and .docx/.doc files are supported.")

    try:
        file_bytes = await file.read()
        raw_text = extract_text_from_file(file_bytes, file.filename)
        jd_schema = parse_jd_to_json(raw_text)

        return StreamingResponse(
            generate_jd_match(jd_schema.model_dump(), "Compare this JD with the candidate profile."),
            media_type="text/event-stream",
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(exc)}") from exc