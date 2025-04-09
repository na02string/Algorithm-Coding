n = int(input())

# Please write your code here.
def fun(n):
    if n == 0:
        return
    li = ['*']*n
    print(' '.join(li))
    fun(n-1)
    print(' '.join(li))



fun(n)

    