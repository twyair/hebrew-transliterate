import re


SIN_DOT = "\u05c2"
SHIN_DOT = "\u05c1"

char_to_trans = str.maketrans(
    {
        SHIN_DOT: "",  # NOTE: shin is the default
        "\u05f3": "'",  # geresh
        "\u05f4": "",  # ignore gershayim
        '"': "",  # ignore gershayim
        "\u05bc": "_",
        "א": "Q",
        "ב": "v",
        "ג": "g",
        "ד": "d",
        "ה": "h",
        "ו": "w",
        "ז": "z",
        "ח": "c",
        "ט": "7",
        "י": "y",
        "כ": "x",
        "ך": "x",
        "ל": "l",
        "ם": "m",
        "מ": "m",
        "ן": "n",
        "נ": "n",
        "ס": "s",
        "ע": "j",
        "ף": "f",
        "פ": "f",
        "ץ": "Z",
        "צ": "Z",
        "ק": "q",
        "ר": "r",
        "ש": "S",
        "ת": "t",
        "\u05b8": "a",
        "\u05b5": "e",
        "\u05b9": "o",
        "\u05b7": "A",
        "\u05b4": "I",
        "\u05bb": "U",
        "\u05b6": "E",
        "\u05c7": "O",
        "\u05b2": "á",
        "\u05b1": "é",
        "\u05b3": "ó",
        "\u05b0": "3",
    }
)

NIQUD_VOWELS = "3áéóAIUEOaeo"
CONSONANTS = "QbvGgDdhwzc7ykxlmnsjpfZqrS5TtXJCV"

LETTERS_WITH_GERESH = {
    "g": "X",
    "z": "J",
    "Z": "C",
    "w": "V",
}
LETTERS_WITH_DAGESH = {
    "v": "b",
    "g": "G",
    "d": "D",
    "x": "k",
    "f": "p",
    "t": "T",
}


def convert(word: str) -> str:
    word = word.translate(char_to_trans)
    word = re.sub(rf"S(?=[{NIQUD_VOWELS}_]*{SIN_DOT})", "5", word).replace(SIN_DOT, "")
    word = re.sub(
        rf"[{''.join(LETTERS_WITH_GERESH)}](?=[{NIQUD_VOWELS}_]*')",
        lambda m: LETTERS_WITH_GERESH[m[0]],
        word,
    ).replace("'", "")
    word = re.sub(r"h$", "H", word)
    word = re.sub(r"h_$", "h", word)
    word = re.sub(rf"([{CONSONANTS}])([{NIQUD_VOWELS}]*)_", r"_\1\2", word)
    word = re.sub(rf"_w(?=[_{CONSONANTS}]|$)", "u", word)
    word = re.sub(rf"wo(?=[_{CONSONANTS}]|$)", "W", word)
    word = re.sub(
        rf"(?<=_)[{''.join(LETTERS_WITH_DAGESH)}]",
        lambda m: LETTERS_WITH_DAGESH[m[0]],
        word,
    )
    word = re.sub(r"^_", "", word)
    word = re.sub(rf"(?<=[{CONSONANTS}])3?_", "", word)
    word = re.sub(rf"Iy(?=[{CONSONANTS}]|$)", "i", word)
    word = re.sub(r"(?<=[jch])A$", "Á", word)
    word = re.sub(r"3$", "", word)
    return word
