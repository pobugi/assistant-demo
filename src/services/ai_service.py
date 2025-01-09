from openai import OpenAI

from config import settings
from src.services.fuzzy_answer_service import FuzzyAnswerService


client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Initialize the service with predefined answers and a threshold
predefined_answers = {
	"How do I create an invoice?": "To create an invoice, go to the Invoices module, click 'New', and fill in the required fields.",
	"Where can I see my inventory?": "You can view your inventory in the Inventory module under the 'Stock Overview' tab.",
	"How do I reset my password?": "Click on 'Forgot Password' at the login screen and follow the instructions."
}

fuzzy_service = FuzzyAnswerService(predefined_answers, threshold=80)


async def process_query(user_input: str) -> str:
	# Step 1: Check for a predefined answer using the service
	predefined_answer = fuzzy_service.find_answer(user_input)
	if predefined_answer:
		return predefined_answer

	# Step 2: Fallback to OpenAI for other queries
	predefined_context = "\n".join(
		[ f"{q} -> {a}" for q, a in predefined_answers.items() ]
	)
	prompt = f"""
	You are an ERP assistant. Use the following predefined answers whenever possible:
	{predefined_context}

	Now, answer this question:
	{user_input}
	"""

	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[ {"role": "system", "content": "You are an ERP assistant."}, {"role": "user", "content": prompt} ],
		max_tokens=150,
		temperature=0.7
	)
	res = response.choices[ 0 ].message.content.strip()
	return res
