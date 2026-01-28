def fib(n):
    if n<=1:
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(6))


# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[n]

# print(fib(6))



# O(2^n)



