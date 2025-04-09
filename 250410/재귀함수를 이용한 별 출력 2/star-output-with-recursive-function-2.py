n = 5

# Please write your code here.
def fun(n):
    if n == 0:
        return
    
    print('* '*n)
    fun(n-1)
    print('* '*n)



fun(n)

    