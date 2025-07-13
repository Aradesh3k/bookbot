def num_words(text):
    words = text.split()
    return len(words)

def num_characters(text):
    char_count = {}
    text_lower = text.lower()  # Convert entire text to lowercase once
    for char in text_lower:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count