def first_non_repeating_letter(s):
    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return ''


print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter("moonmen"))
print(first_non_repeating_letter("abba"))




















































