def solution(clothes):
    clothes.sort(key=lambda x: x[1])
    count = 0
    parts = clothes[0][1]
    parts_count = []
    for idx in clothes:
        if parts != idx[1]:
            parts_count.append(count)
            count = 1
            parts = idx[1]
        else:
            count += 1
    parts_count.append(count)
    answer = 1
    for idx in parts_count:
        answer *= idx + 1
    return answer - 1