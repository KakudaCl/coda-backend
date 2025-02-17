from fastapi import APIRouter

router = APIRouter()


@router.post("/pdfedit", tags=["PDF編集"])
async def edit_pdf():
    return {"kakuda": "test"}
