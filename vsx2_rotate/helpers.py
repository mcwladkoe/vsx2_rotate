from .mapping import ROTATE_MAP


def get_rotated_string(input_str: 'str', invert: 'bool'=True) -> 'str':
    direction = 1
    if invert:
        direction = -1
    res = ''
    for char in input_str[::direction]:
        rotated_char = ROTATE_MAP.get(char)
        if not rotated_char and 1040 <= ord(char) <= 1071:
            rotated_char = ROTATE_MAP.get(chr(ord(char) + 32))
        elif not rotated_char:
            rotated_char = char
        res += rotated_char
    return res
