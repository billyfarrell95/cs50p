from twttr import shorten

def test_shorten_word():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Twitter 123") == "Twttr 123"

def test_shorten_sentence():
    assert shorten("The quick brown fox...") == "Th qck brwn fx..."
    assert shorten("THE QUICK BROWN FOX...") == "TH QCK BRWN FX..."