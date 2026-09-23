from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ============================================================
# VALID KEYS
# ============================================================

VALID_KEYS = {
    "GAME-2026-001",
    "GAME-2026-002",
    "GAME-2026-003",
}


# ============================================================
# REQUEST MODEL
# ============================================================

class KeyRequest(BaseModel):
    key: str


# ============================================================
# KEY VALIDATION
# ============================================================

@app.post("/validate")
def validate_key(data: KeyRequest):

    key = data.key.strip()

    if key in VALID_KEYS:
        return {
            "valid": True,
            "message": "Key is valid"
        }

    return {
        "valid": False,
        "message": "Invalid key"
    }


# ============================================================
# SERVER STATUS
# ============================================================

@app.get("/")
def home():
    return {
        "status": "online",
        "service": "GAME LAUNCHER AUTH"
    }