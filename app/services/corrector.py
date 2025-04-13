import json
import difflib
from typing import List


with open("index.json", "r", encoding="utf-8") as f:
    FRENCH_WORDS = json.load(f)

def is_valid_word(word: str) -> bool:

    return word.lower() in FRENCH_WORDS

def suggest_corrections(word: str, n=3, cutoff=0.75) -> List[str]:
  
    return difflib.get_close_matches(word.lower(), FRENCH_WORDS, n=n, cutoff=cutoff)

def correct_text(text: str) -> dict:
    
    words = text.strip().split()
    corrections = {}

    for word in words:
        if not is_valid_word(word):
            suggestions = suggest_corrections(word)
            if suggestions:
                corrections[word] = suggestions

    return corrections
