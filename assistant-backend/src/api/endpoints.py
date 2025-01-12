from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.ai_service import process_query

router = APIRouter()


# Define a Pydantic model for the request body
class QueryRequest(BaseModel):
    user_input: str


@router.post("/query")
async def handle_query(request: QueryRequest):
    try:
        response = await process_query(request.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
