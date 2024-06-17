print("davaleba 1")
def manual_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

my_list = [1, 2, 3, 4, 5]
print(manual_sum(my_list)) 


print("davaleba 2")
def manual_max(lst):
    max_value = float('-inf') 
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

my_list = [1, 6, 3, 9, 4]
print(manual_max(my_list))  


print("davaleba 3")
def manual_min(lst):
    min_value = float('inf')  
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

my_list = [5, 2, 8, 1, 4]
print(manual_min(my_list))


print("davaleba 4")
def manual_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

my_list = [1, 2, 3, 4, 5]
print(manual_len(my_list)) 





