"""

- The functions that works with case converting are 

"""


LATIN_LOWERCASE = (97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 
                   108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
                   118, 119, 120, 121, 122)

LATIN_UPPERCASE = (65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
                   78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90)

RUS_UKR_LOWERCASE = (1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 
                     1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 
                     1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 
                     1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 
                     1105, 1108, 1110, 1111, 1169)

RUS_UKR_UPPERCASE = (1025, 1028, 1030, 1031, 1040, 1041, 1042, 1043, 
                     1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 
                     1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 
                     1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 
                     1068, 1069, 1070, 1071, 1168)

ARABIC_NUMBERS = (48, 49, 50, 51, 52, 53, 54, 55, 56)

SPACES = (9, 10, 11, 12, 13, 28, 29, 30, 31, 32, 133, 160, 5760, 8192, 
          8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200, 8201, 8202, 
          8232, 8233, 8239, 8287, 12288)


MAIN_PUNCTUATION = (33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
                    46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 
                    95, 96, 123, 124, 125, 126)


# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Check the type of string


def isalpha_(string):
    for i in string:
        if not (ord(i) in LATIN_LOWERCASE or 
                ord(i) in LATIN_UPPERCASE or
                ord(i) in RUS_UKR_LOWERCASE or
                ord(i) in RUS_UKR_UPPERCASE)
            return False
    return True


def isdigit_(string):
    for i in string:
        if not ord(i) in ARABIC_NUMBERS:
            return False
    return True


def isspace_(string):
    for i in string:
        if ord(i) not in SPACES:
            return False
    return True

# My own function
def is_punctuation(string):
    for i in string:
        if ord(i) not in MAIN_PUNCTUATION:
            return False
    return True


# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Works with the case of the letters


# Checkers

def isupper_(string):
    for i in string:
        if not (ord(i) in LATIN_UPPERCASE or
                ord(i) in RUS_UKR_UPPERCASE):
            return False
    return True


def islower_(string):
    for i in string:
        if not (ord(i) in LATIN_LOWERCASE or 
                ord(i) in RUS_UKR_LOWERCASE):
            return False
    return True


def istitle_(string):
    cache = ''
    for i in string:
        if isalpha_(i):
            cache += i
        elif isupper_(cache[:1]) and islower_(cache[1:]):  
            cache = ''
        else:
            return False
    return True


# Case-converters

def upper_(string):
    result = ''
    for i in string:
        if ord('a') <= ord(i) <= ord('z'):
            result += chr(ord(i) - 32)
        else:
            result += i
    return result


def lower_(string):
    result = ''
    for i in string:
        if ord('A') <= ord(i) <= ord('Z'):
            result += chr(ord(i) + 32)
        else:
            result += i
    return result


def capitalize_(string):
    return upper_(string[:1]) + lower_(string[1:])


def title_(string):
    result = ''
    cache = ''
    for i in string:
        if isalpha_(i):
            cache += i
        else:
            result += capitalize_(cache) + i
            cache = ''
    return result


def swapcase_(string):
    result = ''
    for i in string:
        if isupper_(i):
            result += lower_(i)
        else:
            result += upper_(i)
    return result


# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Justify and filling 

def ljust_(string, length, fill=' '):
    if len(string) < length:
        return string + fill * (length - len(string))
    return string

def rjust_(string, length, fill=' '):
    if len(string) < length:
        return fill * (length - len(string)) + string
    return string

def center_(string, length, fill=' '):
    if len(string) < length:
        avg = (length - len(string)) / 2
        return fill * int(avg + 0.5)  + string + fill * int(avg)
    return string


# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


def count_(string, sub, start=None, end=None):
    substring = string[start:end]
    how_many_times = 0
    ind = 0
    while ind <= len(substring):
        step = 1
        if substring[ind:ind+len(sub)] == sub:
            how_many_times += 1
            step = len(sub)
        ind += step
    return how_many_times


# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

def replace_(string, old, new):
    result = ''
    i = 0
    while i <= len(string):
        step = 1
        addition = string[i:i+1]
        if string[i:i+len(old)] == old:
            addition = new
            step = len(old)
        if step == 0:
            step = 1
            addition += string[i:i+1]
        result += addition
        i += step
    return result
