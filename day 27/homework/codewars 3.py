def solution(string, ending):
    return string.endswith(ending)

# Test 
print(solution('abc', 'bc'))
print(solution('abc', 'd'))
