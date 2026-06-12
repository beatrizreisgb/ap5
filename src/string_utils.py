import re

def reverse_string(text: str) -> str:
    """Reverses the given string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return ""

def is_palindrome(text: str) -> bool:
    """Checks if a string reads the same backward as forward, ignoring spaces and capitalization."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return clean_text == clean_text[::-1]

def truncate_string(text: str, max_length: int) -> str:
    """Truncates text to a max length and appends '...' if it exceeds it."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if max_length < 0:
        raise ValueError("Max length cannot be negative")
        
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."