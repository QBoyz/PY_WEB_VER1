def solution (arr):
    answer=0
    calc=0

    for x in range(1, len(arr)):
        calc = arr[x-1] + arr[x]
        answer = calc / len(arr)

    if answer % 1 ==0:
        answer=int(answer)
    return answer
print(solution([5,5]))