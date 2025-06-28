n,k = map(int,input().split())
coin =[]
for _ in range(n):
    coin.append(int(input()))
    coin.sort(reverse = True)
answer = 0   
if len(coin)>=2:
    a2 = coin[-2]
    answer+=k%a2 # 나머지는 1 코인으로 횟수
k -= answer

for i in coin: # 큰수부터 순회
    if i>k:
        continue
    else:
        add_answer = k//i # k가 4200일때 i 는 1000
        k-=add_answer*i # k 200됨
        answer+=add_answer
        if k == 0:
            break
            
print(answer)
    
