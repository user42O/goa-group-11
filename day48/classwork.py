print("1 codewars")
number = int(input("enter a numnber"))
if number % 2 == 0:
    print("even")
else:
    print("odd")


print("2 codewars")  
def max_multiple(divisor, bound):
    return (bound // divisor) * divisor
divisor = 3
bound = 10
result = max_multiple(divisor, bound)
print("The largest integer N:", result)


print("3 codewars")
def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]
print(get_even_numbers([2, 4, 5, 6])) 


print("4 codewars")
def score_answers(correct_answers, student_answers):
    score = 0
    for i in range(len(correct_answers)):
        if student_answers[i] == "":
            continue 
        elif student_answers[i] == correct_answers[i]:
            score += 4
        else:
            score -= 1
    return max(0, score)
print(score_answers(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(score_answers(["a", "a", "c", "b"], ["a", "a", "b", ""]))
print(score_answers(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(score_answers(["b", "c", "b", "a"], ["", "a", "a", "c"]))


print("5 codewars")
def balance_teams(weights):
    team1_weight = sum(weights[::2])
    team2_weight = sum(weights[1::2])
    return (team1_weight, team2_weight)
print(balance_teams([1, 2, 3, 4, 5]))
print(balance_teams([10, 20, 30, 40, 50]))









