#codewars 01 

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


input_string = "hello world"
print(count_vowels(input_string)) 


#codewars 02
def descending_order(num):
    digits = [int(digit) for digit in str(num)]
    sorted_digits = sorted(digits, reverse=True)
    return int(''.join(map(str, sorted_digits)))

input_number = 123456789
print(descending_order(input_number))  


#codewars 03
def filter_list(lst):
    return [item for item in lst if isinstance(item, int)]

input_list = [1, 2, 'a', 'b', 3, 'c']
print(filter_list(input_list))


#codewars 04
def find_odd_occurrence(arr):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    for num, count in count_dict.items():
        if count % 2 != 0:
            return num

input_array = [1, 2, 2, 1, 3, 3, 4]
print(find_odd_occurrence(input_array))

#codewars 05
def digital_root(n):
    if n < 10:
        return n
    digits = [int(digit) for digit in str(n)]
    digit_sum = sum(digits)
    return digital_root(digit_sum)
input_number = 12345
print(digital_root(input_number))
