from lib.music_library import MusicLibrary
from lib.track import Track


# test add() adds multiple track to the list
def test_adds_and_lists_multiple_tracks():
    mlib = MusicLibrary()
    track1 = Track("track1", "artist1")
    track2 = Track("track2", "artist2")
    mlib.add(track1)
    mlib.add(track2)
    assert mlib.tracks == [track1, track2]


# test seacrh() returns the track containing part of the searched word
def test_search_for_track():
    mlib = MusicLibrary()
    track1 = Track("one", "two")
    track2 = Track("three", "four")
    mlib.add(track1)
    mlib.add(track2)
    assert mlib.search("thr") == [track2]
