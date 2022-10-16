# based on https://hebrew-academy.org.il/wp-content/uploads/Klaley-Ktiv-Male.pdf

import re


CONSONANTS = "QbvgGdDhwzc7ykxlmnsjpfZqrS5tTXJCV"
VOWELS = "aiueoAIUEOWáéó"
CATAF_QAMATZ = "ó"
MATRES_LECTIONIS = "YH"
ALL_CHARS = CONSONANTS + VOWELS + MATRES_LECTIONIS


FINAL_TRANS = str.maketrans(
    {
        "i": "y",
        "Y": "y",
        "W": "w",
        "H": "h",
    }
)

exceptions = {
    "loQ": "lQ",
    "jIm": "jm",
    "QIm": "Qm",
    "kOl": "kl",
}


def convert(word: str) -> str:
    word = word.replace("!", "")
    word = word.replace("_", "")
    assert set(word).issubset(ALL_CHARS)

    # exceptions
    if word in exceptions:
        return exceptions[word]
    # more exceptions: mishqal qAyIl (e.g. bayit)
    if re.fullmatch(".AyI.", word):
        return word[0] + "y" + word[-1]

    # klal bet-1
    word = re.sub(f"(?<=^.){CATAF_QAMATZ}", "W", word)

    # klal alef:
    word = re.sub("[uU]", "W", word)

    # klal bet-2
    word = re.sub("[oO](?=[^HQY])", "W", word)
    word = re.sub(f"[oO](?=Q[{VOWELS}])", "W", word)
    if word != "loQ":
        word = re.sub("[oO](?=Q$)", "W", word)

    # klal gimel-2
    # replacing "i" with "a" so it would be removed later
    word = re.sub("I(?=y[oOWuU])", "a", word)
    word = re.sub(f"I(?=.[3{VOWELS}])", "i", word)

    # kal he-{2,4}
    word = re.sub("(?<=.)w(?=.)", "ww", word)

    # klal waw
    word = re.sub("(?<=[^HYW])y(?=[^HYW])", "yy", word)

    # NOTE: start removing vowels

    # klal bet-1
    word = word.replace(CATAF_QAMATZ, "")

    # klal gimel-3
    word = word.replace("I", "")

    word = word.translate(FINAL_TRANS)
    word = re.sub(f"[aeAEáé]", "", word)

    word = re.sub("(?<=ww)w+", "", word)
    word = re.sub("(?<=yy)y+", "", word)

    assert set(word).issubset(CONSONANTS)
    return word
