from wordle_interview_revised_code import WordleGame


class TestWordleGameRevisedCode:

	def test_word_matches(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("APPLE")
		assert result == "GGGGG", "Expected result: 'GGGGG', Actual result: {}".format(result)

	def test_word_does_not_match(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("CORDY")
		assert result == "WWWWW", "Expected result: 'WWWWW', Actual result: {}".format(result)

	def test_word_partial_match(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("ANGER")
		assert result == "GWWYW", "Expected result: 'GWWYW', Actual result: {}".format(result)

	def test_game_is_over(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("ANGER")
		result = game.check_new_word("ANGER")
		result = game.check_new_word("ANGER")
		result = game.check_new_word("ANGER")
		result = game.check_new_word("ANGER")
		result = game.check_new_word("ANGER")
		result = game.check_new_word("ANGER")
		assert result == "Game is Over", "Expected result: 'Game is Over', Actual result: {}".format(result)

	def test_negative_word_is_longer(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("HELLOO")
		assert result == "Invalid word length", "Expected result: 'Invalid word length', Actual result: {}".format(result)

	def test_negative_word_is_shorter(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("HEL")
		assert result == "Invalid word length", "Expected result: 'Invalid word length', Actual result: {}".format(result)

	# Testing at scale
	def test_wordle_game_anagram(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("PPALE")
		assert result == "YGYGG", "Expected result: 'YGYGG', Actual result: {}".format(result)

	def test_wordle_game_anagram_with_duplicate_letter(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("APPLA")  # Anagrams are APPAL, PAPAL
		assert result == "GGGGW", "Expected result: 'GGGGW', Actual result: {}".format(result)

	def test_wordle_game_duplicate_letter_in_guess(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("PPPPP")
		assert result == "WGGWW", "Expected result: 'WGGWW', Actual result: {}".format(result)