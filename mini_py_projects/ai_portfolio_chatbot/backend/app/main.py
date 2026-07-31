# Functions
# -> Create FastAPI app
# -> Register routes
# -> Start server

import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parent.parent
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from fastapi import FastAPI
from app.api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='AI Portfolio APP',
    version='1.0.0'
)
# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register all chat routes

app.include_router(chat_router)

@app.get('/')
def home():
    return {"message":"AI Portfolio APP is running"}