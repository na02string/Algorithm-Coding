N = int(input())

# Please write your code here.
def fun(n):
    if n<= 0:
        return 0
    
    return fun(n-2) + n

print(fun(N))