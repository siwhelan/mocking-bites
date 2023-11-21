from lib.diary import *
from unittest.mock import Mock
import pytest

def test_error_is_raised_if_contents_not_string():
    with pytest.raises(TypeError):
        diary = Diary(10)

def test_read_returns_contents_of_diary():
    diary = Diary("diary entry")

    assert diary.read() == "diary entry"
    