def solution(clothes):
    from collections import defaultdict
    cloth_dict = defaultdict(int)
    for i in clothes:
        cloth_dict[i[1]] += 1
    # print(cloth_dict)
    answer = 1
    for num in cloth_dict:
        answer *= (cloth_dict[num]+1)
    answer -= 1
    # 각 원소 리스트 요소 개수 +1 해서 다 곱하고 -1 하면 답 나옴
    
    return answer