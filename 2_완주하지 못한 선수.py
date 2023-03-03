def solution(participant, completion):
    answer = []
    new_p = sorted(participant)
    new_c = sorted(completion)
    i = 0
    for idx in range(len(new_p)):
        if i >= len(new_c):
            answer.append(new_p[idx])
        elif new_p[idx] == new_c[i]:
            i += 1
            continue
        else:
            answer.append(new_p[idx])
    
    return answer[0]