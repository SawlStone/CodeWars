def vowel_indices(word):
    return [pos + 1 for pos, v in enumerate(word.lower()) if v in "aeiouy"]