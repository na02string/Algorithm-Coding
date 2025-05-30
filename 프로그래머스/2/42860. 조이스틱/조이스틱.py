# # 어느 위치에 있던 가장 최소움직임으로 원하는 알파벳 도달함수
# def reach_alph(alpha):
#     criA = ord('A')# 기준은 A
#     criZ = ord('Z')
#     # 오른쪽 방향으로 움직이면 나오는 횟수
#     right = ord(alpha) - criA
#     left = abs(ord(alpha) - criZ) + 1
#     answer = min(right, left)
#     return answer

# def solution(name):
#     # 위치 변경과 알파벳 변경하는걸 따로 분리해서 생각해줌
#     answer = 0
#     name= list(name)
#     # 각 알파벳 도달 최소 방법 더해주기(알파벳 변경)
#     for i in name:
#         answer += reach_alph(i)
        
#     # 최소 움직여서 각 문자 도달하는 법 더해주기(위치 변경)
#     # -> A 뭉텅이가 나오면 오른쪽으로 진전하는게 빠른지, 왼쪽으로 쭉 가서 맨 마지막문자에 도달해서 가는게 빠른지 판단
#     # 기본은 오른
#     move = 
    
#     return answer
def solution(name):
    # 1. 알파벳 변경 조작 횟수
    change = sum(min(ord(c)-ord('A'), 26 - (ord(c)-ord('A'))) for c in name)

    # 2. 커서 이동 최소화
    move = len(name) - 1  # 일단 오른쪽으로 쭉 가는 기본 전략

    for i in range(len(name)):
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
        
        # 왔다가 되돌아가기 (왼쪽 먼저)
        move = min(move, 2*i + len(name) - j)
        # 끝까지 갔다가 되돌아오기 (오른쪽 먼저)
        move = min(move, i + 2*(len(name) - j))

    return change + move