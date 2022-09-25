from fastapi import APIRouter, Depends
from api.auth.token import oauth2_scheme

router = APIRouter()


@router.get("/health/")
async def health(token: str = Depends(oauth2_scheme)) -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    
