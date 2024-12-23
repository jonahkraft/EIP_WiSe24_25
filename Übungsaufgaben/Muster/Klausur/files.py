from typing import Dict, List
import string


def extract_headers(path: str) -> List[str]:
    output: List[str] = []
    with open(path, "r") as file:
        for line in file:
            edited_line = line.strip()
            if edited_line.startswith("<h"):
                split_line = edited_line.split("<")
                header = split_line[1].split(">")[1]
                if header:
                    output.append(header)
    return output


def count_words_from_file(path: str) -> Dict[str, int]:
    with open(path, "r") as file:

        amount_words: Dict[str, int] = {}

        for index, line in enumerate(file):
            if index < 24:
                continue

            edited_line = line.strip().lower()
            for char in string.punctuation:
                edited_line = edited_line.replace(char, "")
            for word in edited_line.split():
                if word:
                    amount_words[word] = amount_words.get(word, 0) + 1
    return amount_words


def get_most_common_words(amount_words: Dict[str, int]) -> List[str]:
    return sorted(amount_words, key=amount_words.get, reverse=True)[:100]
