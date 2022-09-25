from fastapi import APIRouter, Depends


router = APIRouter()


@router.get("/health/")
async def health() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    
