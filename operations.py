import math


def is_operator(operator):
    return operator in PRIORITY_OPERATORS


OPENED_BRACKET = '('
CLOSED_BRACKET = ')'
EXPONENTIATION = '^'
MULTIPLICATION = '*'
DIVISION = '/'
DDIVISION = 'D'
MDIVISION = '%'
MINUS = '-'
PLUS = '+'

COS = "cos"
SIN = "sin"
TAN = "tan"
ASIN = "asin"
ACOS = "acos"
ATAN = "atan"
ATAN2 = "atan2"

SQRT = "sqrt"
ABS = "abs"
LOG = "log"
LOG10 = "log10"


# float("inf") will get infinity
PRIORITY_OPERATORS = {
    OPENED_BRACKET: float("inf"),
    CLOSED_BRACKET: float("inf"),
    ABS: 4,
    COS: 4,
    SIN: 4,
    TAN: 4,
    ASIN: 4,
    ACOS: 4,
    ATAN: 4,
    ATAN2: 4,

    LOG: 3,
    SQRT: 3,
    LOG10: 3,
    EXPONENTIATION: 3,

    DIVISION: 2,
    DDIVISION: 2,
    MDIVISION: 2,
    MULTIPLICATION: 2,

    PLUS: 1,
    MINUS: 1,

}

MAP_OPERATORS = {
    EXPONENTIATION: lambda x, y: x ** y,
    MULTIPLICATION: lambda x, y: x * y,
    DDIVISION: lambda x, y: x // y,
    MDIVISION: lambda x, y: x % y,
    MINUS: lambda x, y: x - y,
    PLUS: lambda x, y: x + y,
    DIVISION: lambda x, y: x / y,
}

MATH_FUNCTIONS = {
    ATAN2: lambda x: math.atan2(x),
    ATAN: lambda x: math.atan(x),
    ACOS: lambda x: acos(x),
    ASIN: lambda x: asin(x),
    COS: lambda x: math.cos(x),
    SIN: lambda x: math.sin(x),
    TAN: lambda x: math.tan(x),
    SQRT: lambda x: sqrt(x),
    LOG10: lambda x: log10(x),
    LOG: lambda x: log(x),

}


def sqrt(val):
    try:
        return math.sqrt(val)
    except ValueError:
        print('Value error.')
        return 0


def log(val):
    try:
        return math.log(val)
    except ValueError:
        print('Value error.')
        return 0


def log10(val):
    try:
        return math.log10(val)
    except ValueError:
        print('Value error.')
        return 0


def asin(val):
    try:
        return math.asin(val)
    except ValueError:
        print('Value error.')
        return 0


def acos(val):
    try:
        return math.acos(val)
    except ValueError:
        print('Value error.')
        return 0
