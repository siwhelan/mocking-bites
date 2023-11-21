from lib.music_library import MusicLibrary
from unittest.mock import Mock


# ========== Solution 1 ========== #


# test adding multiple tracks, searching a keyword returns
# tracks matching that word
def test_search_by_keyword():
    ml = MusicLibrary()
    fake_match = FakeMatchingTrack()
    fake_mismatch = FakeTrackNotMatching()
    ml.add(fake_match)
    ml.add(fake_mismatch)
    assert ml.search("Song") == [fake_match]


class FakeMatchingTrack:
    def matches(self, keyword):
        return True


class FakeTrackNotMatching:
    def matches(self, keyword):
        return False


# ========== Solution 2 ========== #


# test adding multiple tracks, searching a keyword returns
# tracks matching that word
def test_searches_tracks_by_keyword():
    ml = MusicLibrary()
    fake_match = Mock()
    fake_match.matches.return_value = True
    ml.add(fake_match)
    fake_mismatch = Mock()
    fake_mismatch.matches.return_value = False
    ml.add(fake_mismatch)
    assert ml.search("Song") == [fake_match]


# test adding multiple tracks using mock()
def test_adding_tracks_list_comes_back():
    ml = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    track3 = Mock()
    ml.add(track1)
    ml.add(track2)
    ml.add(track3)
    assert ml.tracks == [track1, track2, track3]
