def number_of_people(bus_stops):
    total_people = 0
    for on, off in bus_stops:
        total_people += on
        total_people -= off
    return max(0, total_people)

# Test 
print(number_of_people([(10, 0), (3, 5), (5, 8)]))
print(number_of_people([(3, 0), (9, 1), (4, 10), (12, 2), (6, 6)]))
print(number_of_people([(3, 0), (9, 1), (4, 8), (12, 2), (6, 6)]))
