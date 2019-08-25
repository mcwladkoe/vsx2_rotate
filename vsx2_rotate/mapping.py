from itertools import chain
from collections import OrderedDict

russian_map = OrderedDict({
    "а": "ɐ",
    "б": "ƍ",
    "в": "ʚ",  # TODO
    "г": "ɹ",  # TODO
    "д": "ɓ",  # TODO
    "е": "ǝ",
    "ё": "ǝ̤",
    "ж": "ж",
    "з": "ε",
    "и": "и",
    "й": "ņ",  # TODO
    "к": "ʞ",  # TODO
    "л": "v",  # TODO
    "м": "w",  # TODO
    "н": "н",
    "о": "о",
    "п": "u",
    "р": "d",
    "с": "ɔ",
    "т": "⊥",
    "у": "ʎ",
    "ф": "ȸ",
    "х": "х",
    "ц": "ǹ",  # TODO
    "ч": "Һ",
    "ш": "m",
    "щ": "m",  # TODO
    "ь": "q",
    "ы": "ıq",  # TODO
    "ъ": "q_",  # TODO
    "є": "э",
    "ю": "oı",  # TODO
    "я": "ʁ",
})

ukrainian_map = OrderedDict({
    "э": "є",
    "ї": "ᴉ",
    "і": "ᴉ",  # TODO
})

english_lower_map = OrderedDict({
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",  # TODO
    "g": "ɓ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
})

english_upper_map = OrderedDict({
    "A": "Ɐ",
    "B": "ᗺ",
    "C": "Ɔ",
    "D": "ᗡ",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "⅁",
    "H": "H",
    "I": "I",
    "J": "ᒋ",
    "K": "ꓘ",
    "L": "⅂",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "ტ",
    "R": "ᴚ",
    "S": "S",
    "T": "⊥",
    "U": "∩",
    "V": "Λ",
    "W": "ʍ",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
})

digits_map = OrderedDict({
    "0": "0",
    "1": "⇂",
    "2": "ᘔ",
    "3": "Ɛ",
    "4": "߈",
    "5": "ϛ",  # TODO
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
})

symbols_map = OrderedDict({
    "&": "⅋",
    "_": "‾",
    "?": "¿",
    "!": "¡",
    "\"": "„",
    "\'": ",",
    ".": "˙",
    ",": "'",
    ";": "؛",
    ":": ":",
})

ROTATE_MAP = OrderedDict(chain(
    russian_map.items(),
    ukrainian_map.items(),
    english_lower_map.items(),
    english_upper_map.items(),
    digits_map.items(),
    symbols_map.items()
))

ROTATE_MAP = OrderedDict(chain(
    ROTATE_MAP.items(),
    {v: k for k, v in ROTATE_MAP.items() if len(v) == 1}.items()
))
