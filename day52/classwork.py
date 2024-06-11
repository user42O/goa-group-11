def sort_array(source_array):
    odd_list = sorted([x for x in source_array if x % 2 != 0])
    index = 0
    result = []
    for x in source_array:
        if x % 2 != 0:
            result.append(odd_list[index])
            index += 1
        else:
            result.append(x)
    return result

source_array = [5, 3, 2, 8, 1, 4]
sorted_array = sort_array(source_array)
print(sorted_array)
