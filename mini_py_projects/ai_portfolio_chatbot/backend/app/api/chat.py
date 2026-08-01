# Functions
# -> /chat
# -> Receive request
# -> Return streaming resposne

import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat import ChatRequest, ChatResponse
from app.services.llm_service import generate_response
from app.services.memory import store_memory

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return StreamingResponse(
        generate_response(req.message),
        media_type="text/event-stream",
    )
