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

from app.models.chat import ChatRequest, ChatResponse
from app.services.llm_service import generate_response

router = APIRouter()

@router.post("/chat",response_model=ChatResponse)
def chat(req: ChatRequest):
    answer=generate_response(req.message)
    
    return ChatResponse(response=answer)