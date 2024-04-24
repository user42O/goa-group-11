def friend(names):
    return [name for name in names if len(name) == 4]

# Test 
print(friend(["Ryan", "Kieran", "Jason", "Yous"])) 