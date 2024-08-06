def is_valid_braces(s: str) -> bool:
    matching_braces = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char in matching_braces.values():
            stack.append(char)
        elif char in matching_braces.keys():
            if stack == [] or matching_braces[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

print(is_valid_braces("(){}[]"))
print(is_valid_braces("([{}])"))
print(is_valid_braces("(}"))
print(is_valid_braces("[(])"))
print(is_valid_braces("[({})](]"))









def alphabet_position(text: str) -> str:
    positions = []

    for char in text:
        if char.isalpha():

            position = ord(char.lower()) - ord('a') + 1
            positions.append(str(position))

    return ' '.join(positions)

input_text = "The sunset sets at twelve o' clock."
output = alphabet_position(input_text)
print(output)








def split_into_pairs(s: str) -> list:
    if len(s) % 2 != 0:
        s += '_'

    pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    return pairs

print(split_into_pairs('abc'))
print(split_into_pairs('abcdef'))
print(split_into_pairs('abcd'))
print(split_into_pairs('a'))
print(split_into_pairs(''))









def time_to_words(time_str: str) -> str:
    numbers = ["twelve", "one", "two", "three", "four", "five", "six", 
               "seven", "eight", "nine", "ten", "eleven", "twelve", "one", 
               "two", "three", "four", "five", "six", "seven", "eight", 
               "nine", "ten", "eleven"]
    
    minutes_words = ["o' clock", "one", "two", "three", "four", "five", 
                     "six", "seven", "eight", "nine", "ten", "eleven", 
                     "twelve", "thirteen", "fourteen", "quarter", "sixteen", 
                     "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
                     "twenty two", "twenty three", "twenty four", "twenty five", 
                     "twenty six", "twenty seven", "twenty eight", "twenty nine", 
                     "half"]
    
    hours, minutes = map(int, time_str.split(':'))

    if minutes == 0:
        if hours == 0:
            return "midnight"
        elif hours == 12:
            return "twelve o' clock"
        else:
            return f"{numbers[hours]} o' clock"
    elif minutes <= 30:
        if minutes == 15:
            return f"quarter past {numbers[hours]}"
        elif minutes == 30:
            return f"half past {numbers[hours]}"
        elif hours == 0 and minutes <= 30:
            return f"{minutes_words[minutes]} minutes past midnight"
        else:
            return f"{minutes_words[minutes]} minutes past {numbers[hours]}"
    else:
        if minutes == 45:
            return f"quarter to {numbers[hours + 1]}"
        elif hours == 23 and minutes > 30:
            return f"{minutes_words[60 - minutes]} minutes to midnight"
        else:
            return f"{minutes_words[60 - minutes]} minutes to {numbers[hours + 1]}"

print(time_to_words("13:00"))
print(time_to_words("13:09"))
print(time_to_words("13:15"))
print(time_to_words("13:29"))
print(time_to_words("13:30"))
print(time_to_words("13:31"))
print(time_to_words("13:45"))
print(time_to_words("00:48"))
print(time_to_words("00:08"))
print(time_to_words("12:00"))
print(time_to_words("00:00"))









def merge_strings(str1: str, str2: str) -> str:
    max_overlap = 0

    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1[-i:] == str2[:i]:
            max_overlap = i
    

    return str1 + str2[max_overlap:]

print(merge_strings("abcde", "cdefgh"))
print(merge_strings("abaab", "aabab"))
print(merge_strings("abc", "def"))
print(merge_strings("abc", "abc"))
print(merge_strings("abaabaab", "aabaabab"))









def factorial_division(n: int, d: int) -> int:
    result = 1
    for i in range(d + 1, n + 1):
        result *= i
    return result

print(factorial_division(5, 3))
print(factorial_division(10, 5))
print(factorial_division(7, 2))
