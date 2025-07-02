def solution(s):
    new_s = []
    s = s[2:-2]
    s = s.split('},{')
    for i in s:
        a = set()
        for j in list(map(int,i.split(','))):
            a.add(j)
        new_s.append(a)
    
    new_s.sort(reverse = False, key = lambda x: len(x))

    answer_set = set()
    answer = []
    
    for i in range(len(new_s)):
        new_num = new_s[i] - answer_set
        for i in new_num:
            answer.append(i)
            answer_set.add(i)
    return answer