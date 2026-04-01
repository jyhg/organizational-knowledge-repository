from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """Authenticate user and return access token."""
    # TODO: implement real authentication
    return TokenResponse(access_token="placeholder-token")


@router.get("/me")
async def get_current_user():
    """Get current user info."""
    # TODO: implement JWT validation
    return {"username": "demo", "role": "employee"}
