def solution(n):
    answer = 0
    answer_list = []
    for x in range(1, n + 1):
        if n % x == 0:
            answer_list.append(x)
    """
    for y in range(1, len(answer_list)):
        print(y)
        answer = answer_list[y-1] + answer_list[y]
        print(answer)
    """
    for i in answer_list:
        answer+=i

    return answer
print(solution(12))