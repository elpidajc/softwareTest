"""Test cases for palindrome detection."""

import pytest
from palindrome import is_palindrome


def test_basic_palindrome():
    """Test basic palindrome 'aba' and non-palindrome 'abc'."""
    assert is_palindrome("aba")
    assert not is_palindrome("abc")


def test_case_insensitive():
    """Test case-insensitive palindromes."""
    assert is_palindrome("Aba")
    assert is_palindrome("AbBa")


def test_with_punctuation():
    """Test palindrome with spaces and punctuation."""
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("race a car")


def test_empty_string():
    """Test empty string is considered palindrome."""
    assert is_palindrome("")


def test_single_char():
    """Test single character is palindrome."""
    assert is_palindrome("a")


def test_non_string_raises_error():
    """Test non-string input raises ValueError."""
    with pytest.raises(ValueError):
        is_palindrome(123)