n = int(input())
people_set = set()
for _ in range(n):
    people, state = map(str,input().split())
    if state == 'enter':
        people_set.add(people)
    else:
        people_set.discard(people)

for name in sorted(people_set, reverse = True):
    print(name)
        
