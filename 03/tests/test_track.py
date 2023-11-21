from lib.track import *

def test_matches_returns_true_when_keyword_equals_title():
    track = Track("title1", "artist1")
    assert track.matches("title1") == True


def test_matches_returns_true_when_keyword_equals_artist():
    track = Track("title1", "artist1")
    assert track.matches("artist1") == True

def test_matches_returns_true_when_keyword_does_not_equals_title_or_artist():
    track = Track("title1", "artist1")
    assert track.matches("title2") == False