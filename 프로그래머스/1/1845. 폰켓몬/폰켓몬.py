def solution(nums):
    num_pok = len(nums) / 2 # 가져가는 폰켓몬 수
    a = len(set(nums))
    if a >= num_pok:
        return num_pok
    else:
        return a
