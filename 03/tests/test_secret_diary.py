from lib.secret_diary import *
from unittest.mock import Mock
import pytest

def test_diary_is_locked():
    secret_diary = SecretDiary(Mock())
    assert secret_diary.locked == True

def test_diary_is_unlocked():
    secret_diary = SecretDiary(Mock())
    secret_diary.unlock()
    assert secret_diary.locked == False

def test_read_raises_error_when_locked():
    secret_diary = SecretDiary(Mock())
    with pytest.raises(Exception) as e:
        assert str(e.value) == "Go away!"

def test_read_returns_diary_contents_when_unlocked():
    secret_diary = SecretDiary(Mock())
    secret_diary.diary = "diary entry"
    secret_diary.unlock()
    assert secret_diary.read() == "diary entry"

