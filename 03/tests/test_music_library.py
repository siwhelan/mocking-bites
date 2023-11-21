from lib.music_library import *
from unittest.mock import Mock

def test_add_adds_tracks_to_library_correctly():
    music_library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    track3 = Mock()
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.tracks == [track1, track2, track3]


def test_search_returns_true_if_relevant_track_is_found():
    music_library = MusicLibrary()
    fake_track = Mock()
    fake_track.matches.return_value = True
    fake_track2 = Mock()
    fake_track2.matches.return_value = False
    music_library.add(fake_track)
    music_library.add(fake_track2)
    assert music_library.search("test") == [fake_track]

def test_search_returns_partial_match_title():
    music_library = MusicLibrary()
    track1 = Track("title1", "artist1")
    track2 = Track("title2", "artist2")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search('tle1') == [track1]

def test_search_returns_partial_match_artist():
    music_library = MusicLibrary()
    track1 = Track("title1", "artist1")
    track2 = Track("title2", "artist2")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search('ist1') == [track1]

def test_search_returns_full_match_title():
    music_library = MusicLibrary()
    track1 = Track("title1", "artist1")
    track2 = Track("title2", "artist2")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search('title1') == [track1]

def test_search_returns_full_match_artist():
    music_library = MusicLibrary()
    track1 = Track("title1", "artist1")
    track2 = Track("title2", "artist2")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search('artist1') == [track1]