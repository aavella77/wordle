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

	def test_word_double_letter_words_where_the_match_is_in_the_second_letter(self):  # This test case fails in the original implementation
		game = WordleGame("APPLE")
		result = game.check_new_word("HELLO")
		print("The result is: ", result)
		assert result == "WWYGW", "Expected result: 'WWYGW', Actual result: {}".format(result)

	def test_word_double_letter_words_where_the_match_is_in_the_second_letter_2(self):
		game = WordleGame("APPLE")
		result = game.check_new_word("HEOLL")
		assert result == "WYWGW", "Expected result: 'WYWGW', Actual result: {}".format(result)

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
