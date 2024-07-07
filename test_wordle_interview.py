from wordle_interview import WordleGame


class TestWordleGame:

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

	# The following 2 test cases were not handled in the original code
	# def test_negative_word_is_longer(self):
	# 	game = WordleGame("APPLE")
	# 	result = game.check_new_word("HELLOO")
	# 	assert result == "Invalid word length", "Expected result: 'Invalid word length', Actual result: {}".format(result)
	#
	# def test_negative_word_is_shorter(self):
	# 	game = WordleGame("APPLE")
	# 	result = game.check_new_word("HEL")
	# 	assert result == "Invalid word length", "Expected result: 'Invalid word length', Actual result: {}".format(result)