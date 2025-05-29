def solution(array, commands):
    answer = []
    for case in commands:
        start = case[0]-1; end = case[1]-1; th = case[2]-1
        
        li = array[start:end+1]
        li = sorted(li)
        # print(li)
        answer.append(li[th])
        
    return answer