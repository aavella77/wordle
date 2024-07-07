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
		self.current_tries += 1

		if self._is_game_over() is True:
			return "Game is Over"

		deep_copy_counts = copy.deepcopy(self.counts)
		res = []
		for i, char in enumerate(new_word):
			if self.mappings[i] == char:
				res.append("G")
			elif char in deep_copy_counts and deep_copy_counts[char] > 0:
				res.append("Y")
			else:
				res.append("W")
			deep_copy_counts[char] -= 1

		return "".join(res)
