def get_num_words(text):
	return len(text.split())

def get_char_count(text: str) -> dict:
    """Return a dictionary of character counts (case-insensitive)."""
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


