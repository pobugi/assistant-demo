from fastapi import APIRouter, HTTPException

from src.services.ai_service import process_query

router = APIRouter()


@router.post("/query")
async def handle_query(user_input: str):
	try:
		response = await process_query(user_input)
		return {"response": response}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
