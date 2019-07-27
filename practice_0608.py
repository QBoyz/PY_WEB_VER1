def solution (s):
    answer = ''
    print(len(s))
    if int(len(s)) % 2 == 0:
        answer = s[int(len(s/2)) + 1]
    else:
        answer = s[int(len(s/2))] + s[int(len(s/2) +1)]
    return answer
solution("abcde")