from twttr import shorten

def test_shorten_word():
    assert shorten("Twitter") == "Twttr"

def test_shorten_sentence():
    assert shorten("The quick brown fox...") == "Th qck brwn fx..."