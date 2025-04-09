n = int(input())

# Please write your code here.
def rec(n):
    if n == 0:
        return

    rec(n-1)
    print("HelloWorld")


rec(n)