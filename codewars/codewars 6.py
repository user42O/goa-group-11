def solution(string: str) -> str:
    res = ''
    for symbol in string:
        if symbol.upper() == symbol:
            res = res + ' ' + symbol
        else:
            res = res + symbol
    return res 