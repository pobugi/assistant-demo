from rapidfuzz import process, fuzz


class FuzzyAnswerService:
	def __init__(self, predefined_answers: dict, threshold: int = 80):
		"""
		Initialize the service with predefined answers and a similarity threshold.

		:param predefined_answers: Dictionary of predefined questions and answers.
		:param threshold: Similarity score threshold for considering a match.
		"""
		self.predefined_answers = predefined_answers
		self.threshold = threshold

	def find_answer(self, user_input: str) -> str | None:
		"""
		Find the best matching predefined answer based on the user input.

		:param user_input: The query from the user.
		:return: The predefined answer if a match is found; otherwise, None.
		"""
		predefined_questions = list(self.predefined_answers.keys())
		match, score, _ = process.extractOne(user_input, predefined_questions, scorer=fuzz.ratio)

		if score >= self.threshold:
			return self.predefined_answers[match]
		return None
