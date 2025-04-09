N = int(input())

# Please write your code here.
def func(N):
    if N == 0:
        return

    print(N,end = ' ')
    func(N-1)
    print(N, end = ' ')

func(N)