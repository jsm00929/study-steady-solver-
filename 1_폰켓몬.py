def solution(nums):
    s1 = set(nums)
    if len(nums) / 2 >= len(s1):
        answer = len(s1)
    else:
        answer = len(nums) / 2
    return answer