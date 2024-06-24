#python program for fibonnaci using

series = lambda n: n if n<=1 else series(n-1) + series (n-2)

fib = lambda n: [series(i) for i in range(n)]

print(fib(4))