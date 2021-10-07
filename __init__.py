import re

scheme = str.maketrans({
    "J": "ז",
    "C": "צ",
    "X": "ג",
    "V": "ו",
    "Q": "א",
    "b": "בּ",
    "v": "ב",
    "g": "ג",
    "d": "ד",
    "h": "ה",
    "w": "ו",
    "z": "ז",
    "j": "ח",
    "7": "ט",
    "y": "י",
    "k": "כּ",
    "x": "כ",
    "l": "ל",
    "m": "מ",
    "n": "נ",
    "s": "ס",
    "R": "ע",
    "p": "פּ",
    "f": "פ",
    "Z": "צ",
    "q": "ק",
    "r": "ר",
    "c": "שׁ",
    "t": "ת",
    "S": "שׂ",
    "G": "גּ",
    "D": "דּ",
    "T": "תּ",
    "H": "ה",
    "Y": "י",
    "N": "א",
    "W": "וֹ",
    "a": " ָ",
    "i": "י ִ",
    "u": "וּ",
    "e": " ֵ",
    "o": " ֹ",
    "A": " ַ",
    "I": " ִ",
    "U": " ֻ",
    "E": " ֶ",
    "O": " ׇ",
    "3": " ְ",
    "á": " ֲ",
    "é": " ֱ",
    "ó": " ֳ",
    "Á": " ַ",
})

CONSONANTS = "QbvgGdDhwzj7ykxlmnsRpfZqrcStT"
FINALS = {
    "מ": "ם",
    "כ": "ך",
    "פ": "ף",
    "צ": "ץ",
    "נ": "ן",
}

def trans2heb(w: str) -> str:
    w = w.replace("!", "")
    w = re.sub(r"_(.)", r"\1_", w)
    w = re.sub(r"([bkpGDT])_", r"\1", w)
    w = re.sub(f"(?<=[{CONSONANTS}])(?=[{CONSONANTS}])", "3", w)
    w = w.translate(scheme)
    dagesh = "ּ"
    return re.sub("[" + "".join(FINALS) + f"](?=[^{dagesh}]?$)", lambda m: FINALS.get(m[0]), w)
