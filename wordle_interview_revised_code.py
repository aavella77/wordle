from collections import Counter
import copy


class WordleGame:
	def __init__(self, answer):
		self.max_tries = 6
		self.answer = answer
		self.current_tries = 0
		self._internal_representation()

	def _is_game_over(self):
		if self.current_tries > self.max_tries:
			return True
		return False

	def _internal_representation(self):
		# create map of index or to char
		self.mappings = {}
		for i, char in enumerate(self.answer):
			self.mappings[i] = char

		self.counts = Counter(self.answer)
		return

	def check_new_word(self, new_word):
		# 2. Handling of Guesses Longer or Shorter than the Answer
		if len(new_word) != len(self.answer):
			return "Invalid word length"

		self.current_tries += 1

		if self._is_game_over() is True:
			return "Game is Over"

		deep_copy_counts = copy.deepcopy(self.counts)
		res = []

		# First pass for greens
		for i, char in enumerate(new_word):
			if self.mappings[i] == char:
				res.append("G")
				deep_copy_counts[char] -= 1
			else:
				res.append(None)  # Placeholder for non-green characters

		# Second pass for yellows and wrongs
		for i, char in enumerate(new_word):
			if res[i] is None:  # Only process if not already marked as green
				if char in deep_copy_counts and deep_copy_counts[char] > 0:
					res[i] = "Y"
					deep_copy_counts[char] -= 1
				else:
					res[i] = "W"

		return "".join(res)

