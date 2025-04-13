import json
import difflib
from typing import List
import re

with open("index.json", "r", encoding="utf-8") as f:
    FRENCH_WORDS = json.load(f)

def is_valid_word(word: str) -> bool:
  
    return word.lower() in FRENCH_WORDS

def suggest_corrections(word: str, n=3, cutoff=0.75) -> List[str]:
   
    word = word.lower()  
    suggestions = difflib.get_close_matches(word, FRENCH_WORDS, n=n, cutoff=cutoff)
 
    if not suggestions:
        suggestions = difflib.get_close_matches(word, FRENCH_WORDS, n=n, cutoff=0.6)

    return suggestions

def correct_text(text: str) -> dict:
   
    words = text.strip().split()
    corrections = {}

    for word in words:
        word_clean = re.sub(r'[^\w\s]', '', word)  
        if not is_valid_word(word_clean):  
            suggestions = suggest_corrections(word_clean)  
            if suggestions:
                corrections[word] = suggestions

    return corrections
