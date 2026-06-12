import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.string_utils import is_palindrome, reverse_string, truncate_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    with pytest.raises(TypeError):
        reverse_string(123)

def test_is_palindrome_valid():
    assert is_palindrome("radar") is True
    assert is_palindrome("A man a plan a canal Panama") is True 
    assert is_palindrome("hello") is False

def test_truncate_string():
    assert truncate_string("GitHub Actions", 6) == "GitHub..."
    assert truncate_string("Short", 10) == "Short"
    with pytest.raises(ValueError):
        truncate_string("Error", -1)