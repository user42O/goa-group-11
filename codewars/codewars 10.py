num = input("enter a positive natural number")
multiples = []
try:
    num = int(num)
    if num <= 0:
        print("0") 
    else:
        for i in range(1, num):
            if (i % 3 == 0) or (i % 5 == 0):
                multiples.append(i)
        print(multiples)

except ValueError:
    print("the number must be a positive integer")
