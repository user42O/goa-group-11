def longest_palindrome(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    longest = 1
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            longest = 2

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                longest = max(longest, length)

    return longest

print(longest_palindrome("a"))
print(longest_palindrome("aab"))
print(longest_palindrome("abcde"))
print(longest_palindrome("zzbaabcd"))
print(longest_palindrome(""))
print(longest_palindrome("I like racecars that go fast"))






def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x, y = 0, 0
    
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1

    return x == 0 and y == 0

print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n', 'n', 'n', 's', 's', 's', 'e', 'e', 'e', 'w']))







def bouncing_ball(h, bounce, window):
    if h <= 0 or not (0 < bounce < 1) or window >= h:
        return -1
    
    count = 0
    
    while h > window:
        count += 1
        h *= bounce
        
        if h > window:
            count += 1
    
    return count

print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(3, 1, 1.5))
print(bouncing_ball(10, 0.5, 2))
print(bouncing_ball(5, 0.8, 1))
print(bouncing_ball(2, 0.4, 1))



