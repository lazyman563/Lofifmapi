from fastapi import APIRouter, Depends, HTTPException
from app.services.yt_service import YTService

router = APIRouter()

@router.get("/search")
async def search(q: str, service: YTService = Depends()):
    if not q:
        raise HTTPException(status_code=400, detail="Search query is required")
    return service.search(q)

@router.get("/stream/{track_id}")
async def stream(track_id: str, service: YTService = Depends()):
    return service.get_stream(track_id)
