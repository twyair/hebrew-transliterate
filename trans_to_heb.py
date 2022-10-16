import re

DAGESH = "\u05bc"
WAW = "ו"
YUD = "י"

FINAL_LETTERS = {
    "m": "ם",
    "n": "ן",
    "f": "ף",
    "Z": "ץ",
    "x": "ך",
    "k": "ך",
}

TAGGED_LETTERS = "XCJV"

char_to_heb = str.maketrans(
    {
        "_": DAGESH,
        "Q": "א",
        "b": "ב" + DAGESH,
        "v": "ב",
        "G": "ג" + DAGESH,
        "g": "ג",
        "D": "ד" + DAGESH,
        "d": "ד",
        "h": "ה",
        "w": WAW,
        "z": "ז",
        "c": "ח",
        "7": "ט",
        "y": YUD,
        "k": "כ" + DAGESH,
        "x": "כ",
        "l": "ל",
        "m": "מ",
        "n": "נ",
        "s": "ס",
        "j": "ע",
        "p": "פ" + DAGESH,
        "f": "פ",
        "Z": "צ",
        "q": "ק",
        "r": "ר",
        "S": "ש" + "\u05c1",
        "5": "ש" + "\u05c2",
        "T": "ת" + DAGESH,
        "t": "ת",
        "X": "ג",
        "C": "צ",
        "J": "ז",
        "V": WAW,
        "a": "\u05b8",
        "i": "\u05b4" + YUD,
        "u": WAW + DAGESH,
        "e": "\u05b5",
        "o": "\u05b9",
        "A": "\u05b7",
        "I": "\u05b4",
        "U": "\u05bb",
        "E": "\u05b6",
        "O": "\u05b8",
        "W": WAW + "\u05ba",
        "á": "\u05b2",
        "é": "\u05b1",
        "ó": "\u05b3",
        "Á": "\u05b7",
        "3": "\u05b0",
        "Y": YUD,
        "H": "ה",
    }
)


CONSONANTS_EXCEPT_ALEF = "bvGgDdhwzc7ykxlmnsjpfZqrS5TtXJCV"
CONSONANTS = f"Q{CONSONANTS_EXCEPT_ALEF}"


dagesh_and_letter_regex = re.compile(r"_(\w)")
dagesh_and_bgdkpt = re.compile(r"_(?=[TGDkpb])")
final_he_regex = re.compile(r"h$")
final_letter_regex = re.compile(rf"([{''.join(FINAL_LETTERS)}])([Aa]?)$")
tagged_letters_regex = re.compile(f"([{TAGGED_LETTERS}])([aeoAIUEO3]?)")
letter_in_coda = re.compile(f"(?<=[{CONSONANTS_EXCEPT_ALEF}])(?=[{CONSONANTS}])")


def convert(word: str) -> str:
    assert not (set(word) & set(" -"))
    word = word.replace("!", "")
    word = dagesh_and_bgdkpt.sub("", word)
    word = dagesh_and_letter_regex.sub(r"\1_", word)
    word = final_he_regex.sub("h_", word)
    word = final_letter_regex.sub(lambda m: FINAL_LETTERS[m[1]] + m[2], word)
    word = tagged_letters_regex.sub(r"\1\2'", word)
    word = letter_in_coda.sub("3", word)
    return word.translate(char_to_heb)



