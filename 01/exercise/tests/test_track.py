from lib.track import Track


# test matches() returns True when given a
# search word and a relevant track is found
def test_matches_finds_a_full_title():
    track = Track("title", "artist")
    assert track.matches("title") == True


# test matches finds a partial title searched
def test_matches_finds_a_partial_title():
    track = Track(" my title", "artist")
    assert track.matches("itle") == True


# test matches finds a full artist
def test_matches_finds_a_full_artist():
    track = Track("title", "artist")
    assert track.matches("artist") == True


# test matches finds a partial artist
def test_matches_finds_a_partial_artist():
    track = Track("title", "my artist")
    assert track.matches("rti") == True


# test matches returns false if no matches
def test_matches_returns_false_if_no_matches():
    track = Track("title", "artist")
    assert track.matches("song") == False
