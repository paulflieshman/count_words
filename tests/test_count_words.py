from lib.count_words import *
import pytest

def test_count_words():
    assert count_words('the quick brown fox jumps over the lazy fox when the rain in Spain falls mainly on the plain') == 19

def test_count_words_empty_string():
    assert count_words("") == 1


# def test_count_words_wrong_type():
# # def test_count_words_wrong_type():
#     # pytest.raises(Exception) as e:
#     assert count_words(True) == ("")
# # interesting! Not sure why this does this!
# # 
# #   



